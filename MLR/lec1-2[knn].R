install.packages("gmodels")
library(gmodels)


usedcars <- read.csv("d:/data/prac/usedcars.csv", stringsAsFactors = FALSE)
head(usedcars)
str(usedcars)
summary(usedcars)
summary(usedcars[c("price","mileage")])
mean(c(36000, 44000, 56000))
median(c(36000, 44000, 56000))
range(usedcars$price)
diff(range(usedcars$price))

## 분위수 ##
IQR(usedcars$price)
quantile(usedcars$price)
quantile(usedcars$price, probs=c(0.01, 0.99))
quantile(usedcars$price, seq(from=0, to=1, by=0.20))

boxplot(usedcars$price, main="Boxplot of UCP", ylab="price")
boxplot(usedcars$mileage, main="Boxplot of UCM", ylab="mile")

## histogram ##
hist(usedcars$price, main="histogram", ylab="price")

## 산포도 ##
var(usedcars$price) # 숫자 데이터가 평균 주변에 넓게 퍼져있음을 나타내는 것
sd(usedcars$price) # 분산의 루트 // 각각이 평균과 얼마나 다른 지

table(usedcars$year)
hist(usedcars$year)
table(usedcars$model)
color_table = table(usedcars$color)

model_table <- table(usedcars$model)
prob = prop.table(model_table)
pie(prob)

color_pct <- prop.table(color_table) * 100
color_pct
pie(color_pct)
round(color_pct, digits=1)
plot(x=usedcars$mileage, y=usedcars$price, main="scatterplot", xlab="uso", ylab='usp')
str(usedcars)
usedcars$conservative <- usedcars$color %in% c("Black", "Gray", "Silver", "White")
head(usedcars)
table(usedcars$conservative)

CrossTable(x=usedcars$model, y=usedcars$conservative)
