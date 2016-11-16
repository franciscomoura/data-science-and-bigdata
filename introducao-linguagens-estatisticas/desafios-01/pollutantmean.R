# The RStudio or R environment work space directory needs to be set 
# to the appropriate directory.

# This file should be into this directory and the directory of the csv files 
# should be under this directory too.

pollutantmean <- function(directory = "specdata", pollutant, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating the location of
    ## the CSV files

    ## 'pollutant' is a character vector of length 1 indicating the name of the
    ## pollutant for which we will calculate the mean; either 'sulfate' or
    ## 'nitrate'.

    ## 'id' is an integer vector indicating the monitor ID numbers to be used

    ## Return the mean of the pollutant across all monitors list in the 'id'
    ## vector (ignoring NA values)
    ## NOTE: Do not round the result!

    # Read the csv file, load, filtering and cleaning the data set
    reduce_csv_file <- function(file) {
        
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

        # Subsetting the income data set by the pollutant name. 
        # The column of the data set will be selected by the pollutant name
        pollutant_dataset <- subset(income, select = c(pollutant))

        colnames(pollutant_dataset) <- c(pollutant)

        # Clean the data set
        # Subsetting the pollutant data set without NA values
        return(na.omit(pollutant_dataset))
    }

    # create a list of csv files to be read based on the id vector
    csv_files <- file.path(getwd(), 
                           directory, 
                           paste(formatC(id, width = 3, flag = 0), 
                                 ".csv", 
                                 sep=""))

    # Load, subsetting and merge the files
    data <- do.call(rbind, lapply(csv_files, reduce_csv_file ))
   
    return (mean(data[, 1], na.rm = TRUE))
}
