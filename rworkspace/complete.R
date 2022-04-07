complete <- function(dir,id){
		allfiles <- list.files(dir, full.names =TRUE)
		data <- data.frame()
	for(i in id){ 
		pol <- data.frame()
		info <- read.csv(allfiles[i])
		pol<- cbind(info$sulfate, info$nitrate)
		good <- complete.cases(pol)
		compol<- pol[good]
		matcom <- matrix(compol,ncol=2)
		number <- nrow(matcom)
		vec <- c(i,number)
		data <- rbind(data,vec)
	}
	colnames(data) <- c("id","nobs")
	data
}
