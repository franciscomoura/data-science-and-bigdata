# The RStudio or R environment work space directory needs to be set 
# to the appropriate directory.

# This file should be into this directory and the directory of the csv files 
# should be under this directory too.

# This file depends on complete.R file. So, load the last one first with the 
# command source("complete.R")

corr <- function(directory = "specdata", threshold = 0) {
    ## 'directory' is a character vector of length 1 indicating the location
    ## of the CSV files.

    ## 'threshold' is a numeric vector of length 1 indicating the number of
    ## completely observed observations (on all variables) required to compute
    ## the correlation between nitrate and sulfate; the default is 0

    ## Return a numeric vector of correlations 
    ## NOTE: Do not round the result!

    # verify the observations on all files under the given directory
    observations <- complete(directory)
    
    # select the monitor ids's that match the threshold condition 
    monitor_ids <- observations[observations["nobs"] > threshold, ]$id

    correlations <- numeric()

    # read all csv files relative to the selected monitor id's
    for (id in monitor_ids) {

        # Column names present on the data files an their data types.
        col_classes <- c("Date" = "character", 
                         "sulfate" = "numeric", 
                         "nitrate" = "numeric", 
                         "ID" = "numeric")

        file <- file.path(getwd(), 
                          directory, 
                          paste(formatC(id, width = 3, flag = 0), 
                                ".csv", 
                                sep=""))

        # Loaded data from CSV files
        income <- read.csv(file, 
                           stringsAsFactors = FALSE, 
                           sep = ",", 
                           colClasses = col_classes)

        complete_cases <- income[complete.cases(income), ]
        correlations <- c(correlations, 
                          cor(complete_cases$sulfate, complete_cases$nitrate))
    }

    return (correlations)
}
