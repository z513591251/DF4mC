DF4mC: A novel method for predicting DNA N4-methylcytosine sites based on deep forest algorithm
===================================================================

Introduction 
===================================================================
DF4mC is an a non-NN-style deep learning-based approach for predicting DNA 4mC sites from sequence alone. Three datasets of experimentally determined 4mC and non-4mC modification sites from three species, including Arabidopsis thaliana, Caenorhabditis elegans, and Drosophila melanogaster, were used to construct the deep models capable of classifying a given DNA sequence as methylated or non-methylated. Starting from the +/- 20-bp flanking sequence of cytosine site, each sample was uniquely represented by a numeric vector of biological features capturing information on sequence orders, compositions, physicochemical properties and structures of DNA sequences. With these features as inputs, the classification models were constructed and trained using the deep forest algorithm, while their performance was evaluated through 10-fold cross-validation.

Installation
===================================================================
Users can use the following command to install Deep Forest (DF) 21 and scikit-learn :

pip install deep-forest

pip install scikit-learn

===================================================================

Quickstart
===================================================================
Evaluate the performance of DF4mC on different datasets using 10-fold cross-validation:

python DF4mC.py --species A.thaliana

python DF4mC.py --species C.elegans

python DF4mC.py --species D.melanogaster

The ROC curve, PR curve, and predicted probabilities are saved in the figure folder


