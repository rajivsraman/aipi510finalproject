import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

def load_dataset(github_url):
    '''
    Loads the dataset from link to raw GitHub file.
    
    Inputs
        github_url(str): raw GitHub link to dataset CSV file
        
    Outputs
        data(pd.Dataframe): full dataset formatted into DataFrane
    '''
    
    # try to fetch the file from the given link
    
    try:
        
        print(f"Fetching dataset from: {github_url}")
        
        # read the data from the CSV file matching the link
        
        data = pd.read_csv(github_url)
        print("Dataset loaded!")
        
    # otherwise, if the file cannot be properly loaded
    
    except Exception as e:
        
        raise RuntimeError(f"Error loading dataset: {e}")

def conduct_eda(data):
    '''
    Conducts a basic exploratory data analysis.
    
    Inputs
        data(pd.DataFrame): loaded dataset from GitHub
        
    Outputs
        EDA: summary, check for missing values, distributions, correlation matrix
    '''
    
    # use the general data.describe() function to print out a summary of the dataset
    
    print("Summary:")
    print(data.describe())
    
    # check for missing values in the data - there should not be any

    missing_values = data.isnull().sum().sum()
    print(f"Missing Values: {missing_values}")

    # plot the histograms that display the distributions of each column in the data
    
    data.hist(figsize=(10, 8))
    plt.tight_layout()
    plt.show()

    # display the correlation matrix that maps each column against each other
    
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

