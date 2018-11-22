### naive bayes classifier ###
install.packages("tm")
install.packages("SnowballC")
install.packages("e1071")
library(tm)
library(SnowballC)
library(wordcloud)
library(e1071)
library(gmodels)

sms = read.csv("d:/data/prac/sms_test.txt", stringsAsFactors=FALSE)
str(sms)
sms$type = factor(sms$type) # type col을 factor로 변호
str(sms)
head(sms)

table(sms$type)
sms_corpus <- VCorpus(VectorSource(sms$text))
sms_corpus # content: traindata -> 60
str(sms_corpus)

## inspect ##
inspect(sms_corpus[1:2])

# 실제 텍스트 내용 # --> character function
as.character(sms_corpus[[1]])
lapply(sms_corpus[1:2], as.character)

# remove puntuation & etc ... #
sms_corpus_clean <- tm_map(sms_corpus, content_transformer(tolower))
as.character(sms_corpus_clean[[1]])
sms_corpus_clean<-tm_map(sms_corpus_clean, removeNumbers)

# remove 불용어 #
sms_corpus_clean <- tm_map(sms_corpus_clean, removewords, stopwords())
sms_corpus_clean <- tm_map(sms_corpus_clean, removePunctuation)
as.character(sms_corpus_clean[[1]])

replacePunctuation <- function(x) {
  gsub("[[:punct:]]", " ", x)
}

replacePunctuation("hi,hello...world!")

## stemming ##
wordStem(c("learning", "learn", "learned", "learns"))

sms_corpus_clean <- tm_map(sms_corpus_clean, stemDocument)
as.character(sms_corpus_clean[[1]])

sms_corpus_clean <- tm_map(sms_corpus_clean, stripWhitespace)
as.character(sms_corpus_clean[[1]])

## text를 단어로 나누는 작업 (Tokenize)
# 문서 -> 단어(토큰) # TermDocumentMatrix() --> 반대\
sms_dtm <- DocumentTermMatrix(sms_corpus_clean) 

# 파라미터를 설정하여 단어-문서행렬로 변환, 전처리 수행
# sms_dtm2 <- DocumentTermMatrix(sms_corpus, control=list(tolower=TRUE, removeNumbers=TRUE, stopwords=function(x){removewords(x, stopwords())},
                                            # removePunctuation=TRUE, stemming=TRUE))

sms_dtm2

inspect(sms_dtm)

## train-test split ##
sms_data_train <- sms_dtm[1:50,]
sms_data_test <- sms_dtm[51:60,]

y_train <- sms[1:50,]$type
y_test <- sms[51:60,]$type

table(y_train)
prop.table(table(y_train))
wordcloud(sms_corpus_clean, random.order=FALSE, random.color=T, colors=brewer.pal(9, "Set1"))

# 부분집합: subset #
spam <- subset(sms, type=='spam')
ham <- subset(sms, type=='ham')

wordcloud(spam$text, random.order=FALSE, random.color=T, colors=brewer.pal(9, "Set1"))
wordcloud(ham$text, random.order=FALSE, random.color=T, colors=brewer.pal(9, "Set1"))

## dtm 최소 지지도 ##
sms_freq_words <- findFreqTerms(sms_data_train, lowfreq=2)
sms_dtm_freq_train <- sms_data_train[,sms_freq_words]
sms_dtm_freq_test <- sms_data_test[,sms_freq_words]
## 최소 2개 이상의 단어들만 추출 ##

## 나이브 베이즈 분류기는 범주형 데이터만 훈련 #
inspect(sms_dtm_freq_train)

convert_counts <- function(x){
  x <- ifelse(x > 0, "YES", "NO")
}

sms_train <- apply(sms_dtm_freq_train, MARGIN=2, FUN=convert_counts)
sms_test <- apply(sms_dtm_freq_test, MARGIN=2, FUN=convert_counts)

sms_classifier <- naiveBayes(sms_train, y_train, laplace=1)
sms_pred <- predict(sms_classifier, sms_test)
sms_pred

CrossTable(sms_pred, y_test, dnn=c('predicted', 'actual'))














