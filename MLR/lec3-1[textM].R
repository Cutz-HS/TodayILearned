myvec <- c(1:6, 'a')
myvec
str(myvec)

obj1 <- 1:4
obj2 <- 6:10
obj3 <- list(obj1, obj2)
obj3

mylist <- list(obj1,obj2,obj3)
mylist[[3]][1]

myvec <- unlist(mylist)
mean(myvec)

name1 <- "Donald"
myspace <- " "
name2 <- "Trump"

a <- list(name1, myspace, name2)
unlist(a)

name <- c('갑', '을', '병', '정')
gender <- c(2, 1, 1, 2)
mydata <- data.frame(name, gender)
mydata

## 메타데이터(data of data) 입력 in r: attr() ##
attr(mydata$name, "what the variable means") <- "name"
mydata$name
attr(mydata$gender, "what the variable means") <- "gender"
mydata$gender

myvalues <- gender
for (i in 1: length(gender)){
  myvalues[i] <- ifelse(gender[i]==1, "남성", "여성")
}
attr(mydata$gender, "what the value means") <- myvalues
attr(mydata$gender, "what the value means")
mydata$gender.chracter <- attr(mydata$gender, "what the value means")
mydata

mylist <- list(1:4, 6:10, list(1:4, 6:10))
mean(mylist[[3]])
lapply(mylist[[3]], mean)

nchar("korea")


mysentence <- "Learning R is so interesting"
mywords <- strsplit(mysentence, split=' ')
strsplit(mywords[[1]][5], split='')

class(rep(NA, 5))
myletter <- list(rep(NA, 5))
for(i in 1:5){
  myletter[i] <- strsplit(mywords[[1]][i], split='')
}
myletter

# 원래대로 #
for(i in 1:5){
  myletter[i] <- paste(myletter[[i]], collapse='')
}
myletter

# text 전처리 #
R_wiki <- "R is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing.[6] The R language is widely used among statisticians and data miners for developing statistical software[7] and data analysis.[8] Polls, data mining surveys and studies of scholarly literature databases, show substantial increases in popularity in recent years.[9] As of August 2018, R ranks 18th in the TIOBE index, a measure of popularity of programming languages.[10]
A GNU package[11], source code for the R software environment is written primarily in C, Fortran and R itself[12] and is freely available under the GNU General Public License. Pre-compiled binary versions are provided for various operating systems. Although R has a command line interface, there are several graphical user interfaces, such as RStudio, an Integrated development environment .[13][14]"
R_wiki_para <- strsplit(R_wiki, split='\n')
R_wiki_para

# 문장 단위로 분해
r_wiki_sent <- strsplit(R_wiki_para[[1]], split='\\.')
r_wiki_sent

# 단어 단위로 분해
r_wiki_word <- list(NA, NA)
for(i in 1:2){
  r_wiki_word[[i]] <- strsplit(r_wiki_sent[[i]], split=' ')
}
r_wiki_word
r_wiki_word[[1]][[2]][3] # index 접근

# reg exp #
mysentence <- "Learning R is so intersting"
regexpr("ing", mysentence)

loc.begin <- as.vector(regexpr('ing', mysentence))
loc.begin

loc.length <- as.vector(attr(regexpr('ing', mysentence), "match.length"))
loc.length

loc.end <- loc.begin + loc.length-1
loc.end

# gregexpr
gregexpr('ing', mysentence)
loc.begin <- as.vector(gregexpr('ing', mysentence)[[1]])
loc.length <- as.vector(attr(gregexpr('ing', mysentence)[[1]], "match.length"))
loc.end <- loc.begin + loc.length-1

regexpr('intersting', mysentence)
regexec('intersting', mysentence)
mysentences <- unlist(r_wiki_sent)
regexpr('software', mysentences)
gregexpr("software", mysentences)

mytemp <- regexpr("software", mysentences)
my.begin <- as.vector(mytemp)
my.begin
my.begin[my.begin==-1] <- NA
my.begin
my.end <- my.begin + as.vector(attr(mytemp, "match.length"))-1
my.end

mylocs <- matrix(NA, nrow=length(my.begin), ncol=2)
mylocs
colnames(mylocs) <- c("begin", "end")
mylocs
rownames(mylocs) <- paste("sentence", 1:length(my.begin), sep='.')
mylocs

for (i in 1: length(my.begin)){
  mylocs[i,] <- cbind(my.begin[i], my.end[i])
}
mylocs

grep('software', mysentences)
grepl('software', mysentences)

sub('ing', 'ING', mysentence)
gsub('ing', 'ING', mysentence)

## 고유 명사 처리 ##
sent1 <- r_wiki_sent[[1]][1]
new.sent1 <- gsub("R Foundation for Statistical Computing", 
                  "R_Foundation_for_Statistical_Computing", sent1)
new.sent1

sum(table(strsplit(sent1, split=' ')))

strsplit(new.sent1, split=' ')
drop.sent1 <- gsub("and |by |for |the","",new.sent1)
drop.sent1

mypattern <- regexpr('ing', mysentence)
regmatches(mysentence, mypattern, invert=TRUE)
strsplit(mysentence, split='ing')
gsub('ing', '', mysentence)
substr(mysentences, 1, 30)
my2sentence <- c("Learning R is so interesting",
                 "He is a fascinating singer")
mypattern0 <- gregexpr('ing', my2sentence)
mypattern1 <- gregexpr('[[:alpha:]](ing)', my2sentence)
mypattern1
regmatches(my2sentence, mypattern1)
mypattern2 <- gregexpr('[[:alpha:]]+(ing)\\b', mysentences)
myings <- regmatches(mysentences, mypattern2)
myings
table(unlist(myings))

mypattern <- gregexpr('[[:alpha:]]+(ing)\\b', tolower(mysentences))
myings <- regmatches(tolower(mysentences), mypattern)
myings
table(unlist(myings))

## stat 포함된 표현 ##
mypattern <- gregexpr('(stat)[[:alpha:]]+', tolower(mysentences))
myings <- regmatches(tolower(mysentences), mypattern)
table(unlist(myings))









