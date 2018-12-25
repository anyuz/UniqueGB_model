# UniqueGBmodel

This package is created to check the least adding points that reseachers need to collect in experimental tests to get unique Gb model for discreate biological networks. 

## Usage

### 1. Import Package
First download the package, then move example dataset p2n4.txt to the folder we want to run the python2/3.
Run the python2/3, then import the packag: 
#### from UniqueGB_model import UniqueGB_model

### 2. Create Class

#### myadd = UniqueGB_model()

### 3. Run Check Function

#### myadd.checkaddone(m1, m2, n1, n2)

##### m1 is the number of GBs models you want to reduce by adding points, 
##### m2 is the number of GBs models you want to reduce to 
##### n1 is the number of points of the orignal dataset
##### n2 is the number of points of the dataset after adding the points


### 4. Read Outputs

#### I.  Successful! The adding path fund and save the result to the file. Then the results will be like below:

end of the test
True
5 Gbs for 13 points to 1 Gbs for 15 points
file has been created in your folder


Then you can open the file just created which contain the unique datasets after adding points.

#### II. Fail to find the adding path that can get unique GB

end of the test
False
There is no add one point path for 10 Gbs 13 points to 1 Gbs 14 points


