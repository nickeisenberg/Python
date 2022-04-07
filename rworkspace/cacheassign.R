makeCacheMatrix <- function(m = matrix()){
	inv <- NULL
		set <- function(mat){
			m <<- mat
			inv <- NULL
		}
		get <- function() m
		setinv <- function (inverse) inv <<- inverse
		getinv <- function() inv
		list (set =set,get = get,setinv =setinv,getinv=getinv) 
}


cacheSolve <- function(x,...){
	inv <- x$getinv()
		if(!is.null(inv) == TRUE){
			message("getting inverse, bitch hol' up")
			print(inv)
		}	
		data <- x$get()
		inv <- solve(data)
		x$setinv(inv)
		inv
}