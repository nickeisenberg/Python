trials <- function(){
cards <- 1:52
deck <- numeric()
count <- 0 
	
while(length(deck) < 52){
	r <- sample(cards,1)
		if( r %in% deck == FALSE){
			deck <- append(deck,r)
		}  
		count <- count +1
		if(count > 500){
			break
		}
	}
print(count)
}
