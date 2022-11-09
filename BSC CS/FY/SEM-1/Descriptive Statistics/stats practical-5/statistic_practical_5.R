# Practical 5
# Momentsa. Raw
# moments
# b. Central
# moments
# 1. Find the third central moment of eruption duration in the data set faithful. We apply the function moment from the e1071 package. As it is not in the core R library, the
# package has to be installed and loaded into the R workspace.


library (moments)
duration = faithful$eruptions
moment(duration, order=3, center=TRUE)

# 2. Generate the random sample of size 10000 and calculate all moments
x <- rnorm(10000)

all.moments(x, order.max = 2, central = FALSE, absolute = FALSE, na.rm = FALSE)

# Arguments
# x A numeric vector, matrix or data frame of data. For matrices and data frames,
# each column is a random variable
# order.max the maximum order of the moments to be computed with a default value of 2.
# central a logical value, if TRUE, central moments are computed. Otherwise, raw moments are
# computed
# absolute a logical value, if TRUE, absolute moments are computed. Otherwise, standard
# moments are computed
# na.rm a logical value, if TRUE, remove NA values. Otherwise, keep NA values
# [1] 1.00000000 0.01888716 1.01376912
#  3. Generate the random sample of size 50000 and calculate all moments
#     4. Find the fourth central moment of eruption duration in the data set faithful.