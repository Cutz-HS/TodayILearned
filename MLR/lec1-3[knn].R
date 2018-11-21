install.packages("class")
library(class)
library(gmodels)

wbc <- read.csv("d:/data/prac/wisc_bc_data.csv", stringsAsFactors=FALSE)
getwd()

structure(wbc)
head(wbc)
wbc <- wbc[-1]
str(wbc)
table(wbc$diagnosis)
str(wbc$diagnosis)
wbc$diagnosis <- factor(wbc$diagnosis, levels=c("B", "M"), labels=c('Benign', 'Malignant'))
wbc$diagnosis
str(wbc$diagnosis)

round(prop.table(table(wbc$diagnosis))*100, digits=1)
summary(wbc[c("radius_mean", "perimeter_worst")])

## 정규화 함수 생성 ##
normalize <- function(x){
  return ((x - min(x)) / (max(x) - min(x)))
}

wbc_x <- lapply(wbc[2:31], normalize)
head(wbc_x)
str(wbc_x)
wbc_x <- as.data.frame(wbc_x)
str(wbc_x)
head(wbc_x)
summary(wbc_x$area_mean)

# train: 1~469, test: 470~569 #
x_train <- wbc_x[1:469,]
x_test <- wbc_x[470:569,]

y_train <- wbc[1:469,1]
y_test <- wbc[470:569, 1]

head(x_train)
head(x_test)
head(y_train)
head(y_test)

## modeling ## KNN -> 입력데이터를 구조화된 형식으로 저장
wbc_test_pred <- knn(train=x_train, test=x_test, cl=y_train, k=21)
wbc_test_pred
y_test

CrossTable(x=y_test, y=wbc_test_pred, prop.chisq=FALSE)

















