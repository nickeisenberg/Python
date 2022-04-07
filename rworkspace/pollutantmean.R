pollutantmean <-function(dir,pol,id= 1:332){
	
	allfiles <- list.files(dir, full.names=TRUE)
	dat<- data.frame()
		for(i in id){
			dat <- rbind(dat,read.csv(allfiles[i]))
		}
		vec<- dat[[pol]]
	mean(vec, na.rm=TRUE)
	
}
