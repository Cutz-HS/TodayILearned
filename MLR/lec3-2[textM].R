### 감성 분석 ###
install.packages("rvest")
install.packages("tidytext") # 형태소 분석 & 감성분석 사전
install.packages("tidyr") # tidyR
library(rvest)
library(stringr)
library(tidytext)
library(tidyr)
paper2016 <- read_html("http://www.dbpia.co.kr/Journal/ArticleDetail/NODE07079332")
k.title <- paper2016 %>% html_node("h3") %>% html_text()
k.title

e.title <- paper2016 %>% html_node(".h3_sub_scr") %>% html_text()
e.title

author <- paper2016 %>% html_node(".writeInfo") %>% html_text()
author <- str_replace_all(author, "\r\n[[:space:]]+", "")
author

body <- paper2016 %>% html_node(".con_txt") %>% html_text()
body
body_split <- strsplit(body, "\r\n")
k.abstract <- body_split[[1]][2]
e.abstract <- body_split[[1]][3]

## AFINN 감정 어휘 사전 ##
afinn <- data.frame(get_sentiments("afinn"))
tail(afinn)
hist(afinn$score, breaks=20, col='blue')

## lexicon ##
get_sentiments("bing")
get_sentiments("nrc")

oplex <- data.frame(get_sentiments("bing"))
table(oplex$sentiment)

























