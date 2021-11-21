library(magrittr)

# get input
dat <- read.table(file = "./day1_input.txt")[,1]

combn(x = dat, m = 2, FUN = function(x) {
    if (sum(x) == 2020) {
        return(x)
    } else {
        return(NA)
    }
}) %>% .[!is.na(.)]
