# Desafios - 01
Desafios propostos pelo professor Lenardo Vilela, implementados na linguagem de programação R.

- Diretório **data** contém os arquivos de dados (data sets).
- Diretório **demo** contém alguns resultados esperados do processamento de cada função (A melhor maneira de visualizar o conteúdo deste diretório é fazendo o download ou clonando o projeto).
- Diretório **prototipos** contém os protótipos das funções que deverão ser desenvolvidas.

## Introduction
For this first programming assignment you will write three functions that are meant to interact with dataset that accompanies this assignment. The dataset is contained in a zip file specdata.zip that you can download from the Coursera web site.

## Data
The zip file containing the data is atached;
* [specdata.zip [2.4MB]] (https://github.com/franciscomoura/data-science-and-bigdata/raw/master/introducao-linguagens-estatisticas/desafios-01/data/specdata.zip)

The zip file contains 332 comma-separated-value (CSV) files containing pollution monitoring data for fine particulate matter (PM) air pollution at 332 locations in the United States. Each file contains data from a single monitor and the ID number for each monitor is contained in the file name. For example, data for monitor 200 is contained in the file "200.csv". Each file contains three variables:

- *Date*: the date of the observation in YYYY-MM-DD format (year-month-day)
- *sulfate*: the level of sulfate PM in the air on that date (measured in micrograms per cubic meter)
- *nitrate*: the level of nitrate PM in the air on that date (measured in micrograms per cubic meter)

For this programming assignment you will need to unzip this file and create the directory 'specdata'. Once you have unzipped the zip file, do not make any modifications to the files in the 'specdata' directory. In each file you'll notice that there are many days where either sulfate or nitrate (or both) are missing (coded as NA). This is common with air pollution monitoring data in the United States.

## Part 1
Write a function named 'pollutantmean' that calculates the mean of a pollutant (sulfate or nitrate) across a specified list of monitors. The function 'pollutantmean' takes three arguments: 'directory', 'pollutant', and 'id'. Given a vector monitor ID numbers, 'pollutantmean' reads that monitors' particulate matter data from the directory specified in the 'directory' argument and returns the mean of the pollutant across all of the monitors, ignoring any missing values coded as NA. A prototype of the function is as follows

[prototype](https://github.com/franciscomoura/data-science-and-bigdata/blob/master/introducao-linguagens-estatisticas/desafios-01/prototipos/pollutantmean.png)

You can see some [example output from this function](https://d396qusza40orc.cloudfront.net/rprog%2Fdoc%2Fpollutantmean-demo.html). The function that you write should be able to match this output. Please save your code to a file named pollutantmean.R.

### My solution
[Here is the R archive] (https://github.com/franciscomoura/data-science-and-bigdata/blob/master/introducao-linguagens-estatisticas/desafios-01/pollutantmean.R)
```R
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
```

## Part 2
Write a function that reads a directory full of files and reports the number of completely observed cases in each data file. The function should return a data frame where the first column is the name of the file and the second column is the number of complete cases. A prototype of this function follows

[prototype](https://github.com/franciscomoura/data-science-and-bigdata/blob/master/introducao-linguagens-estatisticas/desafios-01/prototipos/complete.png)

You can see some [example output from this function](https://d396qusza40orc.cloudfront.net/rprog%2Fdoc%2Fcomplete-demo.html). The function that you write should be able to match this output. Please save your code to a file named complete.R. To run the submit script for this part, make sure your working directory has the file complete.R in it.

### My solution
[Here is the R archive] (https://github.com/franciscomoura/data-science-and-bigdata/blob/master/introducao-linguagens-estatisticas/desafios-01/complete.R)
```R
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
```
## Part 3
Write a function that takes a directory of data files and a threshold for complete cases and calculates the correlation between sulfate and nitrate for monitor locations where the number of completely observed cases (on all variables) is greater than the threshold. The function should return a vector of correlations for the monitors that meet the threshold requirement. If no monitors meet the threshold requirement, then the function should return a numeric vector of length 0. A prototype of this function follows

[prototype](https://github.com/franciscomoura/data-science-and-bigdata/blob/master/introducao-linguagens-estatisticas/desafios-01/prototipos/corr.png)

For this function you will need to use the 'cor' function in R which calculates the correlation between two vectors. Please read the help page for this function via '?cor' and make sure that you know how to use it.

You can see some [example output from this function](https://d396qusza40orc.cloudfront.net/rprog%2Fdoc%2Fcorr-demo.html).

The function that you write should be able to match this output. Please save your code to a file named corr.R. To run the submit script for this part, make sure your working directory has the file corr.R in it.

### My solution
[Here is the R archive] (https://github.com/franciscomoura/data-science-and-bigdata/blob/master/introducao-linguagens-estatisticas/desafios-01/corr.R)
```R
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
```

### External references
1. [specdata.zip [~3MB]](https://d396qusza40orc.cloudfront.net/rprog%2Fdata%2Fspecdata.zip)
2. [Pollutantmean function output demo](https://d396qusza40orc.cloudfront.net/rprog%2Fdoc%2Fpollutantmean-demo.html)
3. [Complete funcion output demo](https://d396qusza40orc.cloudfront.net/rprog%2Fdoc%2Fcomplete-demo.html)
4. [Corr function output demo](https://d396qusza40orc.cloudfront.net/rprog%2Fdoc%2Fcorr-demo.html)
