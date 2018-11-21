subject_name <- c('Jone', 'Jane', 'Steve')
# subject_name

temperature <- c(98.1, 98.6, 101.4)
temperature[2]
flu_status <- c(FALSE, FALSE, TRUE)
flu_status[2:3]
flu_status[-3]

temperature[c(FALSE, FALSE, TRUE)]

## 범주형 ##
gender <- factor(c('MALE', 'FEMALE', 'MALE'))
gender
blood <- factor(c('B','AB','O'), levels=c('A','B','O','AB'))
blood

## 순서있는 팩터형 ##
symptoms <- factor(c('severe', 'mild', 'moderate'), 
                   levels=c('mild', 'severe', 'moderate'),
                   ordered=TRUE)
symptoms

## list ##
gender[1]

subject1 <- list(fullname=subject_name[1],
                 temperature=temperature[1],
                 flu_status=flu_status[1],
                 gender=gender[1],
                 blood=blood[1],
                 symptoms=symptoms[1])
subject1[2]
subject1[[2]]
subject1$tempeartrue

## data Frame ##: 같은 type, 2차원 array
df <- data.frame(subject_name, temperature, gender, blood, symptoms, stringsAsFactors=FALSE)
df
df[,1]
df[1,]
df[,]
df[c(1,3)]
df[-2,c(-1,-3,-5)]

## matrix ##: 다양한 type
m <- matrix(c(1,2,3,4), nrow=2)
m <- matrix(c(1,2,3,4,5,6), ncol=2)
m

ls()
rm(m, subject1)
ls()
rm(list=ls())


















