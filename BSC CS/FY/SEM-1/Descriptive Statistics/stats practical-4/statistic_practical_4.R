# Practical 4: Measures dispersiona. Range and Coefficient of range
# b. Quartile deviation and Coefficient of quartile deviation
# c. Standard deviation, Variance and Coefficient of variation (C.V.)
# The range of an observation variable is the difference of its largest and smallest data values. It
# is a measure of how far apart the entire data spreads in value.
#  Find the range of the eruption duration in the data set faithful.


duration = faithful$eruptions
max(duration) - min(duration)


# Answer
# The range of the eruption duration is 3.5 minutes
# dat <- iris
# head(dat)
# max(dat$Sepal.Length) - min(dat$Sepal.Length) – Range
# sd(dat$Sepal.Length) – Standard Deviation
# var(dat$Sepal.Length) - Variance
# IQR(dat$Sepal.Width) – Inter quartile Range
# sd(dat$Sepal.Length) / mean(dat$Sepal.Length) – Coefficient of Varaince(quantile(dat$Sepal.Length, 0.75) - quantile(dat$Sepal.Length, 0.25))/(quantile(dat$Sepal.Length,
# 0.75) + quantile(dat$Sepal.Length, 0.25)) – Quartile Deviaiton
# (quantile(dat$Sepal.Length, 0.75) - quantile(dat$Sepal.Length, 0.25))/(quantile(dat$Sepal.Length,
# 0.75) + quantile(dat$Sepal.Length, 0.25))*100 – coefficient of Quartile Deviation