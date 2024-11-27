import unittest
import pandas as pd
from scripts.data_preprocessing import load_dataset, split_data, power_analysis
from scripts.exploratory_data_analysis import conduct_eda
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from sklearn.model_selection import train_test_split
from statsmodels.stats.power import FTestPower

# this is the URL to the raw GitHub CSV file containing the dataset

URL = "https://raw.githubusercontent.com/rajivsraman/aipi510finalproject/refs/heads/main/dataset/SABRE_SHEATH_Dataset.csv"

class TestProjectFunctions(unittest.TestCase):
    """
    Unit tests for the Final Dataset Project scripts.
    """

    def test_load_dataset(self):
        '''
        Test loading the dataset from a GitHub URL (load_dataset)
        '''
        
        print("\nTest 1. Checking if dataset loads correctly.")
        
        # load in the data
        
        dataset = load_dataset(URL)

        # assert that dataset should be a Dataframe
        
        self.assertIsInstance(dataset, pd.DataFrame, "Dataset should be a Pandas DataFrame.")
        
        # assert that dataset should not be empty
        
        self.assertGreater(len(dataset), 0, "Dataset should not be empty.")

        print(f"Dataset successfully loaded with shape: {dataset.shape}")

    def test_split_data(self):
        '''
        Test the data splitting functionality (split_data)
        '''
        print("\nTest 2. Checking if data is split and pre-processed correctly.")
        
        # load in the data
        
        dataset = load_dataset(URL)
        
        # split the data
        
        X_train, X_test, y_train, y_test = split_data(dataset)

        # assert that all variables have the correct type after splitting
        
        self.assertIsInstance(X_train, pd.DataFrame, "X_train should be a Pandas DataFrame.")
        self.assertIsInstance(X_test, pd.DataFrame, "X_test should be a Pandas DataFrame.")
        self.assertIsInstance(y_train, pd.Series, "y_train should be a Pandas Series.")
        self.assertIsInstance(y_test, pd.Series, "y_test should be a Pandas Series.")
        self.assertGreater(len(X_train), 0, "X_train should not be empty.")
        self.assertGreater(len(X_test), 0, "X_test should not be empty.")

        print(f"Training features shape: {X_train.shape}")
        print(f"Test features shape: {X_test.shape}")
        print(f"Training labels shape: {y_train.shape}")
        print(f"Test labels shape: {y_test.shape}")

    def test_power_analysis(self):
        '''
        Test the computation of appropriate sample size via power analysis (power_analysis)
        '''
        print("\nTest 3. Checking power analysis")
        
        # assign all the inputs to the power_analysis function
        
        num_predictors = 7
        effect_size = 0.15 # medium effect size
        alpha = 0.05
        power = 0.8

        sample_size = power_analysis(effect_size, alpha, power, num_predictors)

        # assert that the sample size is a positive number
        
        self.assertGreater(required_sample_size, 0, "Sample size should be greater than 0.")
        
        print(f"Required sample size for power analysis: {required_sample_size:.2f}")

    def test_conduct_eda(self):
        '''
        Test performing exploratory data analysis on the dataset.
        '''
        print("\nTest 4. Checking exploratory data analysis.")
        
        # load in the data
        
        dataset = load_dataset(URL)

        # try to run conduct_eda without any errors
        
        try:
            conduct_eda(dataset) 
            success = True
            
        # if an error is thrown while conduct_eda is running
        
        except Exception as e:
            success = False
            print(f"Exploratory data analysis failed: {e}")

        # assert that no errors were thrown
        
        self.assertTrue(success, "Analysis should be complete without errors.")
        print("Exploratory data analysis complete! Visualization plots have been output.")


if __name__ == "__main__":
    
    # run all tests
    
    unittest.main()


# In[ ]:




