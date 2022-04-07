corr <- function(dir,thresh = 0){
		allfiles <- list.files(dir, full.names=TRUE)
		len <- length(allfiles)
		com <- complete(dir,1:len)
		good <- which(com$nobs > thresh)
		cordata <- numeric()
			for(i in good){
				red<- read.csv(allfiles[i])
				info <- cbind(red$sulfate, red$nitrate)
				col1 <- info[,1]
				col2 <- info[,2]
				point<- cor(col1,col2,use="complete.obs")
				cordata[i] <- point
			}
			cordata<- cordata[complete.cases(cordata)]
			cordata
}			
