# install package data.table

library (data.table)
data_table <- data.table(col1 = sample(6 : 9, 9 , replace = TRUE), col2 = letters[1 : 3],col3 = c(1, 4, 1,2, 2,2, 1, 2, 2))
print ("Original DataFrame")
print (data_table)

#Install package ggplot2

library (ggplot2)
data_table <- data.frame(col1 = sample(6 : 9, 9 , replace = TRUE), col2 = letters[1:3], col3 = c(1, 4, 1, 2, 2, 2, 1, 2, 2))
print ("Original DataFrame")
print (data_table)
freq_tbl <- table(data_table$col1)
print ("Frequency count")
frequency <- function(x) { factor(x, levels = names(table(x)))}
ggplot(data_table, aes(x = frequency(`col1`))) + geom_bar()

#2. Scatterplot

plot(Girth, Height, main = "Scatterplot of Girth vs Height", xlab = "Tree Girth", ylab = "Tree Height")
abline(lm(Height ~ Girth), col = "blue", lwd = 2)

plot(Girth, Volume, main = "Scatterplot of Girth vs Volume", xlab = "Tree Girth", ylab = "Tree Volume")
abline(lm(Volume ~ Girth), col = "blue", lwd = 2)

plot(Girth, Volume, main = "Scatterplot of Girth vs Volume", xlab = "Tree Girth", ylab = "Tree Volume")
abline(lm(Volume ~ Girth), col = "blue", lwd = 2)

#Scatterplot3d

#Install Package scatterplot3d

library(scatterplot3d)
attach(trees)
scatterplot3d(Girth, Height, Volume, main = "3D Scatterplot of trees dataset")

scatterplot3d(Girth, Height, Volume, pch = 20, highlight.3d = TRUE, type = "h", main = "3D Scatterplot of trees dataset")

#3. Boxplot

boxplot(trees, col = c("yellow", "red", "cyan"), main = "Boxplot for trees dataset")

#4. Line Chart

plot(Girth, type = "o", col = "red", ylab = "", ylim = c(0, 110), main = "Comparison amongst Girth, Height, and Volume of trees")
lines(Height, type = "o", col = "blue")
lines(Volume, type = "o", col = "green")
legend(1, 110, legend = c("Girth", "Height", "Volume"), col = c("red", "blue", "green"), lty = 1:1, cex = 0.9)