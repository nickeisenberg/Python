#boundary and source function 
funb <- function(x,y){
	exp(x)*sin(y)
}

funs <- function(x,y){
	0
}

#generating the coeficient matrix given j (number of particians of domain) value
#cm stands for coeficient matrix 

j=5
J=(j-1)^2

cm1 <- matrix(0,J,J)

for(i in 1:J){
	cm1[i,i]=2
}

for(i in 1:J-1){
	cm1[i,i+1]=-1
}

for(i in 1:(J-j+1)){
	cm1[i,i+j-1]=-1
}

cm1t <- t(cm1)

cm <- cm1+cm1t

for(i in 1:(j-2)){
	cm[i*(j-1),i*(j-1)+1]=0
	cm[i*(j-1)+1,i*(j-1)]=0
}

#generate the b vector for cm*x=b
#bm stands for b-matrix
#bv stands for v-vector

p <- 1/j 

bm <- matrix(0,j-1,j-1)

	#corners of bm 
 bm[1,1]=(funb(p,0)+funb(0,p)-(p^2)*funs(p,p))
 
 bm[1,(j-1)]=(funb(p*(j-1),0)+funb(1,p)-(p^2)*funs((j-1)*p,p))
 
 bm[(j-1),1]=(funb(p,1)+funb(0,p*(j-1))-(p^2)*funs(p,(j-1)*p))
 
 bm[(j-1),(j-1)]=(funb(p*(j-1),1)+funb(1,p*(j-1))-(p^2)*funs((j-1)*p,(j-1)*p))
 
	 #top-middle of bm
 for(i in 2:(j-2)){
 	bm[1,i]=(funb(i*p,0)-(p^2)*funs(i*p,p))
 }
 
	 #bottom-middle of bm
 for(i in 2:(j-2)){
 	bm[(j-1),i]=(funb(i*p,1)-(p^2)*funs(i*p,(j-1)*p))
 }
 
	#left-middle of bm
for(i in 2:(j-2)){
 	bm[i,1]=(funb(0,i*p)-(p^2)*funs(p,i*p))
 }

	#right-middle of bm
for(i in 2:(j-2)){
 	bm[i,(j-1)]=(funb(1,i*p)-(p^2)*funs((j-1)*p,i*p))
 	
 	}

	#center of bm
for(i in 2:(j-2)){
	for(k in 2:(j-2))
 	bm[k,i]=-(p^2)*funs(i*p,k*p)
 	
 }
 
 # turning bm into a column vector b for cm*x=b
b<- matrix(as.vector(t(bm)),(j-1)^2,1)

#find the solution of cm*x=b
sol<-solve(cm,b)

for(i in 1:(j-1)^2){
	
}

#find the error
act<- matrix(0,(j-1),(j-1))
for(i in 1:(j-1)){
	for(k in 1:(j-1))
		act[i,k]=funb(p*k,p*i)
}
actv <- matrix(as.vector(t(act)),(j-1)^2,1)

errv <- matrix(0,(j-1)^2,1)

for(i in 1:(j-1)^2){
	errv[i,1]=abs(actv[i,1]-sol[i,1])
}
error <- max(errv)

#solution in matrix form 

solv<- as.vector(sol)
solvm <- matrix(solv,(j-1),(j-1))
solution <- t(solvm)

#key to explain how the answer is presented 

key <- matrix(0,j-1,j-1)
for(i in 1:(j-1)){
	for(k in 1:(j-1))
	key[i,k]<- paste("u(x_",i,k,")",sep = "")
	
}

