library(magrittr)

# get input
dat <- read.table(file = "./day1_input.txt")[,1]

combiations <- combn(x = dat, m = 3)

comb_hit <- combn(x = dat, m = 3, FUN = function(x) sum(x) == 2020)

combiations[,comb_hit][1] * combiations[,comb_hit][2] 

