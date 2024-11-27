# Building a dataset of simulated SABRE-SHEATH experiments

- **Author** - Rajiv Raman
- **Institution** - Duke University
- **Course** - AIPI 510: Sourcing Data for Analytics
- **Assignment** - Final Dataset Project
- **Deadline** - November 26, 2024

## Executive Summary

Nuclear magnetic resonance (NMR) spectroscopy is a powerful tool that facilitates magnetic resonance imaging, chemical fingerprinting, and quantification of metabolic processes.  The fields of medicine, chemistry, and biomedical engineering have benefited tremendously from applications of NMR-based technology. However, NMR signal is dictated by the inherently low difference in spin-up and spin-down populations (~3 in 100,000 proton spins at 10 T and 25°C), limiting the sensitivity. A variety of NMR “hyperpolarization” techniques have been developed to overcome this low sensitivity by increasing the spin population difference, thereby enhancing polarization to provide higher NMR signal-to-noise ratio (SNR). 

Signal Amplification By Reversible Exchange (SABRE) is a new and inexpensive NMR hyperpolarization technique that transfers polarization from parahydrogen onto a target nucleus via an organometallic catalyst. The advent of “SABRE in shield enables alignment transfer to heteronuclei” (SABRE-SHEATH) unlocked the realm of low-field manipulation by eliminating influence from the Earth’s magnetic field. SABRE-SHEATH functions by uniting an iridium-based catalyst, a target ligand, parahydrogen, and a stabilizing co-ligand in a chemical reaction under the influence of magnetic fields. Immediately after a SABRE-SHEATH experiment is run, an NMR spectrum taken on the ligand will exhibit a significant augmentation in SNR. Through such NMR hyperpolarization techniques, scientists have revolutionized science both inside and outside of the clinic.

Dr. Warren S. Warren's lab at Duke University has developed a robust package in Wolfram Mathematica (DMExFR2) that facilitates highly accurate simulations of SABRE experiments. Because these experiments take time to set up, it is valuable to simulate whether a particular experiment is worthwhile running before carrying it out. As a result, the lab's workflow is expedited significantly, as we can easily determine which experiments are actually worth running. That being said, these simulations can take time to evaluate, especially when working with larger molecules and spin systems. The reason for this time scaling is the large number of matrix dot products that must be computed to propagate our chemical system over time. In particular, these matrices are 2^N x 2^N, where N is the number of spins in the system. Therefore, runtime complexity builds up quickly as each new spin is added. So, while the simulations allow us to avoid experimental burdens, their runtime can be a separate burden by itself.

The burden of SABRE simulation runtime motivated me to build this dataset, which is now publicly available on Kaggle (https://www.kaggle.com/datasets/rajivsundarraman/dataset-of-simulated-sabre-sheath-experiments) under the CC0 license. By storing previously calculated simulations in a dataset, it becomes possible to approximate new simulation results via extrapolation. So far, 1321 distinct SABRE-SHEATH simulations on a three-spin system have been stored in the dataset. Scripts for data processing and exploratory data analysis are included in this repository, and their functionalities can be tested by running the **test_scripts.py** script in the scripts folder.

## Description of Data

The dataset is available in CSV format, where each row represents an individual simulation. For each simulation, a variety of input parameters were selected, and the result of each simulation is the spin polarization (%) on the target nucleus. The calculated polarization from each simulated experiment is found in the rightmost column of the dataset (labeled polarization). Seven input parameters were selected as features to be tracked along with the dependent polarization variable.

1. B0 (µT) - the constant magnetic field applied along the z-axis in the shield
2. kdN (1/s) - dissociation rate of the target ligand to the iridium catalyst
3. kaH (1/s) - associated rate of the parahydrogen to the iridium catalyst
4. \[Ir]/\[L] - the ratio of concentrations from \[Ir] (catalyst) to \[L] (ligand)
5. \[Ir]/\[H2] - the ratio of concentrations from \[Ir] (catalyst) to \[H2] (parahydrogen)
6. runtime (ms) - the total runtime of the SABRE experiment before measuring polarization (how long is B0 turned on for?)
7. dt (ms) - time step of the simulation (smaller dt means higher accuracy of final result)

For each simulation, the spin system was held constant. It was modeled as a three-spin system, where the first two spins are the hydrides derived from parahydrogen, and the third spin is a single nitrogen-15 nucleus intended to model a target ligand. The scalar J-coupling between the hydrides is -9.2 Hz, and the coupling between the nitrogen-15 and one hydride is -25.41 Hz. These couplings play an important role in determining how polarization builds up on the target nitrogen-15 nucleus, but they were held constant through the entirety of this dataset to ensure through analysis of this specific spin system. Moreover, the nitrogen-15 was set to undergo T1 relaxation with a time constant of 40 s, and the hydrides were set to undergo T1 relaxation with a time constant of 1s. T1 relaxation and J-couplings are important properties of NMR spectroscopy, but lengthy discussion about these characteristics is unnecessary here. It should primarily be understood that these factors were held constant, although they will certainly have an influence on spin polarization buildup.

## Power Analysis

A critical aspect of building this dataset is ensuring that the sample size is large enough to achieve sufficient power in the data analysis. To do this, we must first set a null hypothesis that we hope to reject with the dataset. In particular, we hope that this dataset gives us clear trends in how single parameter changes influence overall polarization, so we formulate our null hypothesis as follows: none of the features have a significant effect on the dependent variable (polarization). Because the dataset could be analyzed with a regression-based model, this is equivalent to stating:

$$H_0: \beta_1 = \beta_2 = \cdots = \beta_n = 0$$

In this expression for the null hypothesis, each $\beta_k$ is the weight of feature $k$ in the regression model. When all the weights are zero, we know that none of our features cause a significant change in the polarization, so this formulation was selected for the null hypothesis. Accordingly, the Python function **FTestPower()** is called to execute a power analysis, as we need to simultaneously look at the influences on polarization across all parameters. For the analysis, it was determined that an effect size of 0.15 would serve the purposes of this project, as it seems that each feature generally can explain a moderate amount of the variance in polarization. Moreover, traditional choices of setting $\alpha = 0.05$ and aiming to achieve 80% power were used to calculate the required sample size.

After running the **test_scripts.py** file, the results of the power analysis are printed out. Based on our input parameters, the power analysis concludes that this dataset requires a minimum of 637 different entries. The final dataset contains 1321 rows resulting from 1321 different simulations, indicating that we have more than enough data in this dataset to achieve 80% power in our analysis.

## Exploratory Data Analysis

To gain elementary insights into the dataset, code is included in the repository to execute an exploratory data analysis (**exploratory_data_analysis.py**). Running the **test_scripts.py** file will allow you to see the results of the exploratory data analysis:

1. Summary of each column in dataset (count, mean, stdev, minimum, first quartile, median, third quartile, maximum)
2. Check for any missing values in the dataset
3. Distributions of the values within each column
4. Correlation heatmap of all columns mapped against each other

## Ethics Statement

The primary goal of this dataset is to improve the efficiency of SABRE-related workflows by providing pre-computed simulation results, offering a data-driven solution to gaining further insights into NMR hyperpolarization while circumventing the burden of starting the simulation from scratch. By documenting the methodology behind the dataset generation, we hope to promote transparency and reproducibility of the data.

The data is sourced from simulations, and it does not contain any personal or sensitive information, which means the dataset does not run into concerns regarding privacy violations. The values that were tested for simulation parameters matching experimental parameters were varied within reasonable ranges, ensuring that each row simulated a somewhat realistic experiment. However, users should be careful to not directly extrapolate this dataset to any real SABRE experiment. It should be understood that this dataset was only generated from a rudimentary three-spin system, so it might not adequately model the quantum dynamics of more complex spin systems. Instead, the dataset should serve as a educational tool for researchers looking to understand the SABRE process more closely.

By promoting the reduction of repetitive computations, this dataset places heavy emphasis on lowering the overall computational energy consumption and encouraging efficient experimentation. The dataset is also publicly available on Kaggle, and access to the data is unrestricted by the CC0 license. So, the dataset is widely available, but it is critical that users on a wide scale know that this dataset cannot serve as a substitute for a real SABRE experiment. Rather, it can serve as a general guide for those trying to solve a problem in a specific SABRE system.

## License

This dataset is licensed under the **CC0 1.0 Universal (Public Domain Dedication)** license. You are free to use it for any purpose, including commercial use, without asking for permission.

For more details, see the full license text in the LICENSE file or at:
[https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/).


