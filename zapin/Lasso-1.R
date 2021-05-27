# 8000行
data.fl <- read.csv("D:\\important APP\\study\\R\\data1.csv",header=T, encoding="UTF-8") 
names(data.fl)
dim(data.fl)
data.fl[,18]

# fit.fl.lm <- lm(Prfmc~., data.fl)
# summary(fit.fl.lm)

Y <- data.fl[,18]# extract Y 
X.fl <- model.matrix(Prfmc~., data=data.fl)[, -1]
# X.fl <- as.matrix(data.fl[,1:17])
colnames(X.fl)
# X.fl=as.data.frame(lapply(data.fl,as.numeric))

# 给定lambda求系数
fit.fl.lambda <- glmnet(X.fl, Y, alpha=1, lambda = 100)
names(fit.fl.lambda) 
fit.fl.lambda$lambda 
fit.fl.lambda$beta 
fit.fl.lambda$df    		
fit.fl.lambda$a0    
coef(fit.fl.lambda)
# 输出系数不为0的变量
tmp_coeffs <- coef(fit.fl.lambda)  
data.frame(name = tmp_coeffs@Dimnames[[1]][tmp_coeffs@i + 1], coefficient = tmp_coeffs@x)  

# 估计lambda的范围
fit.fl.lambda <- glmnet(X.fl, Y, alpha=1)
str(fit.fl.lambda)
# lambda系数
fit.fl.lambda$lambda 
# lambda系数的图
plot(fit.fl.lambda) 


# 选定最优的lambda值
set.seed(10)  # to control the ramdomness in K folds 
fit.fl.cv <- cv.glmnet(X.fl, Y, alpha=1, nfolds=10 )  # 分组
#plot(fit.fl.cv$lambda)      # There are 100 lambda values used
fit.fl.cv$cvm               # 100个lambda对应的均方误差
#plot(fit.fl.cv$lambda, fit.fl.cv$cvm, xlab="lambda", ylab="mean cv errors")
fit.fl.cv$lambda.min        # lambda.min returns the min point amoth all the cvm. 
fit.fl.cv$nzero    # 非0系数

plot(fit.fl.cv$lambda, 
     main = "There are 100 lambda used", 
     xlab = "Lambda Index", 
     ylab = "Lambda Value",
     type = "l") 


# 交叉验证
head(data.frame( Cross.Validation.Erorr = fit.fl.cv$cvm , Lambda = fit.fl.cv$lambda))           
plot(log(fit.fl.cv$lambda), fit.fl.cv$cvm, type = "l", xlab=expression(log(lambda)), ylab="mean cv errors")

head(data.frame(fit.fl.cv$lambda, fit.fl.cv$nzero))
plot(fit.fl.cv$lambda, fit.fl.cv$nzero, type = "l",xlab="lambda", ylab="number of non-zeros")

plot(fit.fl.cv)


#  方法1：最小的lambda下的有效系数
coef.min <- coef(fit.fl.cv, s="lambda.min")  #s=c("lambda.1se","lambda.min") or lambda value
coef.min <- coef.min[which(coef.min !=0),]   # get the non=zero coefficients
coef.min  # the set of predictors chosen
rownames(as.matrix(coef.min)) # shows only names, not estimates

# 方法2：标差lambda下的有效系数
coef.1se <- coef(fit.fl.cv, s="lambda.1se")  
coef.1se <- coef.1se[which(coef.1se !=0),] 
coef.1se
rownames(as.matrix(coef.1se))

# 方法3：指定固定个数的有效系数 下例中为指定9个
coef.nzero <- coef(fit.fl.cv, nzero = 9) 
coef.nzero <- coef.nzero[which(coef.nzero !=0), ]
rownames(as.matrix(coef.nzero))

# 方法4：最优lambda下的有效系数 （此时lambda可取对数，指数，等转换）
coef.s <- coef(fit.fl.cv, s=exp(4.6))  
coef.s <- coef.s[which(coef.s !=0),] 
coef.s
var.4.6 <- rownames(as.matrix(coef.s))

# 方法5：最小的lambda下的有效系数另一种表示方法
fit.fl <- glmnet(X.fl, Y, alpha=1)  
coef.min <- coef(fit.fl, s=fit.fl.cv$lambda.min)  #s=c("lambda.1se","lambda.min") or lambda value
coef.min <- coef.min[which(coef.min !=0),]   
# get the non=zero coefficients
#predict(fit.fl.cv, s=fit.fl.cv$lambda.min, X.fl)
# get in sample prediction values
coef.min


# 求确定方程（对删选后的有效变量做回归）
coef.min <- coef(fit.fl.cv, s="lambda.min")  #s=c("lambda.1se","lambda.min") or lambda value
coef.min <- coef.min[which(coef.min !=0),]   # get the non=zero coefficients
coef.min
var.min <- rownames(as.matrix(coef.min)) # output the names
lm.input <- as.formula(paste("Prfmc", "~", paste(var.min[-1], collapse = "+"))) 
  # prepare for lm fomulae
lm.input

#  最终的回归方程
fit.min.lm <- lm(lm.input, data=data.fl)  # debiased or relaxed LASSO
lm.output <- coef(fit.min.lm) # output lm estimates. compare this with the LASSO output, any difference? in what way?
summary(fit.min.lm) 



 
