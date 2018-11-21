install.packages("arules")
library(arules)

# all_data <- read.csv("d:/data/prac/groceries.csv", stringsAsFactors=FALSE, header=FALSE)

groceries <- read.transactions("d:/data/prac/groceries.csv", sep=",")
summary(groceries)
inspect(groceries[1:5])

itemFrequencyPlot(groceries, support=0.1)
itemFrequencyPlot(groceries, topN=15)
image(sample(groceries, 100))

## apriori ##
apriori(groceries) # support=0.1, confidence=0.8
rules <- apriori(groceries, parameter=list(support=0.006, confidence=0.25, minlen=2))
rules
summary(rules)
inspect(rules[1:3])
inspect(sort(rules, by="lift")[1:10])

# 부분집합 # 연관규칙
# berry가 다른 어떤 아이템과 자주 구매되는지 #
berry_rules <- subset(rules, items %in% "berries")
inspect(berry_rules)

# 저장 #
write(rules, file="d:/data/prac/groceryrules.csv", sep=",", quote=TRUE, row.names=FALSE)

rules_df <- as(rules, "data.frame")
str(rules_df)
