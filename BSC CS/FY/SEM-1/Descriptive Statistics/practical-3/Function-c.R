# Use of Function c()- Combines Individual Vector Values

Light <- c(20,20,20,20,21,24,44,60,90,94,101)
rmax <- c(1.73,1.65,2.02,1.89,2.61,1.36,2.37,2.08,2.69,2.32,3.67)
plot(rmax~Light)

# Example 1
Light <- c( 35, 47, 87, 95, 144, 146, 166, 171, 187, 193)
rmax <- c(27, 26.8, 47.70, 76, 91, 97.3, 98.2, 153, 180, 184)
plot(rmax~Light)
	
# Example 2
Light <- c(3, 1, 3, 111, 128, 140, 147, 160, 176, 188)
rmax <- c(30, 51, 94, 106, 110, 125, 123, 163, 166, 189)
plot(rmax~Light)

# Example 3
Light <- c( 1, 15, 37, 50, 99, 109, 126, 134, 177, 178)
rmax <- c(9, 14, 68, 1116, 110, 127, 128, 146, 149, 151)
plot(rmax~Light)