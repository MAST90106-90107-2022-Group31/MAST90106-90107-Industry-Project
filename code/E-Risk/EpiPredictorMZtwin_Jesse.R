library(glmnet)
library(Matrix)
library(mltools)
library(dplyr)
library(data.table)
library(pROC)
# Load your DNA methylation data object "beta" (rows=samples, columns=249 CpGs). Values=methylation beta-values.
# The object beta should contain all 249 methylation sites used by the predictor and should not contain any missing values.
load("Betas.RData") 

# Standardize your DNA methylation beta-values 
beta <- apply(beta,2,scale)

#install.packages('R.utils')
#system.time(dt <- fread(input = "data/data2.csv.gz", header = TRUE))

# Load elastic net prediction model
# This model is based on 249 methylation sites that are present on the Illumina 450k and EPIC array, and was trained to distinguish MZ twins from DZ twins. 
load("EpiPredictorMZtwin.RData")
# write the 833 columns
# write.csv(data.frame(cv.glmmod$glmnet.fit$beta@Dimnames[1]),"883columnsName.csv", row.names = FALSE)

# read the 833 Data from dataset GSE
gesNormalised833 <- read.csv("data/data833.csv")
# convert dataFrame to dgCMatrix 
X <- as.matrix(gesNormalised833)
#Classification: Predicted MZ status
predicted <- as.matrix(predict(cv.glmmod, newx =X, s = "lambda.min", type = "response"))

response = read.csv("data1.csv")
mdz = response$zygostiy
trueclass <- rep(0,length(gesNormalised833))
trueclass[mdz=='MZ'] <- 1

auc(trueclass, predicted)

auc_roc(predicted ,trueclass)

predicted[which(predicted==1)] <- 'Predicted MZ'
predicted[which(predicted==0)] <- 'Predicted non-MZ'
write.csv(predicted, 'predicted833Result.csv')

#To obtain a continuous MZ twinning score

# continousscore <- as.matrix(predict(cv.glmmod, newx =betav, s = "lambda.min", type = "link"))
