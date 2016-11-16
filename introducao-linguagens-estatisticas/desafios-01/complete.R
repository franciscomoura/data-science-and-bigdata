# The RStudio or R environment work space directory needs to be set 
# to the appropriate directory.

# This file should be into this directory and the directory of the csv files 
# should be under this directory too.

complete <- function(directory = "specdata", id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating the location
    ## of the CSV files.

    ## 'id' is an integer vector indicating the monitor ID numbers to be used

    ## Return a data frame of the form:
    ## id   nobs
    ##  1    117
    ##  2   1041
    ## ...
    ## where 'id' is the monitor ID number and 'nobs' is the number of
    ## complete cases

    # Read the csv file, load the data and calculate the complete cases
    calculate_completes <- function(id) {

        # create a list of csv files to be read based on the id vector
        file <- file.path(getwd(), 
                           directory, 
                           paste(formatC(id, width = 3, flag = 0), 
                                 ".csv", 
                                 sep=""))

        # Column names present on the data files an their data types.
        col_classes <- c("Date" = "character", 
                         "sulfate" = "numeric", 
                         "nitrate" = "numeric",
                         "ID" = "numeric")

        # Loaded data from CSV files
        income <- read.csv(file, 
                           stringsAsFactors = FALSE, 
                           sep = ",", 
                           colClasses = col_classes)

        # compute and sum the complete cases present on the data file
        return(sum(complete.cases(income)))
    }

    # Compute the complete cases for each given id
    nobs <- sapply(id, calculate_completes)
    data <- data.frame(id, nobs)
    
    return(data)
} 

