# Use the following code to install the GEOquery and illuminaio library
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("GEOquery")
BiocManager::install("illuminaio")

library(GEOquery)
library(illuminaio)

# The filename is the local file path
data = getGEO(GEO = 'GSE', filename = "GSE105018_family.soft", GSEMatrix = TRUE)

gsms = data@gsms

# gsm2814050 = gsms$GSM2814050
# gsm2814050Header = gsm2814050@header
# GSMList(data)[[1]]

# Read the local idat file
G.idats = readIDAT("GSM2814050_9741779121_R03C01_Grn.idat")
names(G.idats)
GIdatData <- G.idats$Quants
head(GIdatData)
