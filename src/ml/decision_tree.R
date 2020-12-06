Data <- read.csv("Documents/fifth/data_vis/problems/f1_visualisation/src/f1/data_processing/aus_2019.csv", header=TRUE, sep=",") 
Data2 <- read.csv("Documents/fifth/data_vis/problems/f1_visualisation/src/f1/data_processing/da_labs/data/DT-Credit.csv", header=TRUE, sep=";") 
Data[8]<- NULL
str(Data)
attach(Data)
library(rpart)
DT_Model <-rpart(time.ms.~., data=Data, control=rpart.control(minsplit=60,
                                                              minbucket=30, maxdepth=4 )) 
install.packages("partykit")
library("partykit")
plot(as.party(DT_Model))
print(DT_Model) 