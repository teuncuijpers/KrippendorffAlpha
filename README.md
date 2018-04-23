# KrippendorffAlpha
I could not find a full datatype-independent Python implementation for Krippendorff's Alpha reliability, so here is one.

The definition can be used to compute Alpha for every datatype (nominal, ordinal, interval, ratio). Input data should be any number of lists of equal length (one for each observer) which have been concatenated using np.vstack(list1, list2, ... , listk). For missing values, impute value 99. If value 99 is in your data, choose another and change in the def. 

Definition currently only takes numerical values, also for nominal and ordinal data types. 

To do: 
- Implement type-independent computation of diffObs and diffExp
- Allow for string values as input
- Simulate a number of datasets to evaluate performance across a range of possible datasets, compared to Andrew Hayes' SPSS implementation. 

When using this, refer to: 
Krippendorff, K. (2011). Computing Krippendorff's alpha-reliability.
