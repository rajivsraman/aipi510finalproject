import pandas as pd
from sklearn.model_selection import train_test_split
from statsmodels.stats.power import FTestPower
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

def split_data(data, test_size = 0.3, random_state = 42):
    '''
    Splits the data into features and labels in both training and validation sets.
    
    Inputs
        data(pd.DataFrame): dataset processed as a DataFrame
        test_size(float): optional parameter for setting size of test set (default is 0.3)
        random_state(int): sets the random_state parameter for the data splitting
        
    Outputs
        X_train(pd.DataFrame): features for training data
        X_test(pd.DataFrame): features for testing data
        y_train(pd.Series): labels for training data
        y_test(pd.Series): labels for testing data 
    '''
    
    # assign the features based on all columns except the rightmost column
    
    features = data.iloc[:, : - 1]
    
    # assign the labels based on only the rightmost column (polarization)
    
    labels = data.iloc[:, -1]
    
    # use the train_test_split function to execute the data splitting
    
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size = test_size, random_state = random_state)
    
    return X_train, X_test, y_train, y_test

def power_analysis(effect_size, alpha, power, num_features):
    '''
    Calculates the sample size required to achieve a certain power.
    
    Inputs
        effect_size(float): the effect size of our analysis
        alpha(float): the value of alpha in our analysis
        power(float): the power we aim to achieve with the data analysis
        num_features(int): the number of distinct features that are marked in the dataset
        
    Outputs
        sample_size(float): the minimum sample size required to achieve given power
    '''
    
    # null hypothesis: all of the features have no significant effect on polarization (dependent variable)
    
    # such a null hypothesis testing multiple features at once calls for the FTestPower function
    
    analysis = FTestPower()
    
    # plug in our input parameters - leave df_num blank, as it is what we aim to solve for
    
    sample_size = analysis.solve_power(effect_size = effect_size, df_denom = num_predictors, alpha = alpha, power = power)
    
    return sample_size

