library(tidytext)
library(tidyr)
library(ggplot2)
library(stringr)
library(tm)
# install.packages("dplyr")
library(dplyr)

get_sentiments("afinn")
affinn <- data.frame(get_sentiments("afinn"))
hist(affinn$score, breaks=20, col='blue')
get_sentiments("nrc")
get_sentiments("bing")

my.text.location <- "d:/data/prac/papers"
mypaper <- VCorpus(DirSource(my.text.location), readerControl=list(language='en'))
inspect(mypaper)
mytxt <- c(rep(NA), 24)
for (i in  1:24){
  mytxt[[i]] <- as.character(mypaper[[i]][1])
}

mytxt

my.df.text <- data_frame(paper.id=1:24, doc=mytxt)
my.df.text

## 문서-단어 행렬 구성 ##
my.df.text.word <- my.df.text %>% unnest_tokens(word, doc)
my.df.text.word
res <- my.df.text.word %>% 
  inner_join(get_sentiments("bing"))
res

myres.sa <- my.df.text.word %>% inner_join(get_sentiments("bing")) %>% 
  count(word, paper.id, sentiment) %>% spread(sentiment, n, fill=0)
myres.sa

myagg <- summarise(group_by(myres.sa, paper.id),
          pos.sum=sum(positive),
          neg.sum=sum(negative),
          pos.sent=pos.sum - neg.sum)

## 메타데이터와 분석결과 결합 ##
myfilenames <- list.files(path=my.text.location, pattern=NULL, all.files=TRUE)
# . / .. 삭제 #
paper.names <- myfilenames[3:26]

# 정규식 -> [[:upper:]]{1} (첫 문자 대문자) / [[:upper:]]{1}[[:alpha:]]{1}
str(paper.names)
pub.year <- as.numeric(unlist(str_extract_all(paper.names, "[[:digit:]]{4}")))
paper.id <- 1:24
pub.year.df <- data.frame(paper.id, paper.names, pub.year)
pub.year.df

myagg <- merge(myagg, pub.year.df, by='paper.id', all=TRUE)

## 시각화 ##
myagg.long <- reshape(myagg, idvar='paper.id', varying=list(2:4), timevar='category', v.names='value',
        direction='long')
myagg.long$cate[myagg.long$category==1] <- 'positive words'
myagg.long$cate[myagg.long$category==2] <- 'negative words'
myagg.long$cate[myagg.long$category==3] <- 'positive score'

ggplot(data=myagg.long, aes(x=pub.year, y=value))+ geom_bar(stat='identity')+
  labs(x='publication year', y='value')+
  scale_x_continuous(limits=c(2009,2015))+
  facet_grid(cate~.)









