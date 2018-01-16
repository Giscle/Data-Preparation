# Data-Preparation
All the scripts related to data preparation.

                                            ********** rename.py *************

This Script is used to Maintain Uniform Annotation Label in XML Files Across the Dataset which is Annotated Using LabelImg Software Tool

For eg :  Person X annotated a car as "CAR" person Y annotated a car as "cAR" , then this code will convert all Annotations to "car"                 irrespective of Perosn X and Y without any Hassle.

To run this Script : Place this rename.py in the Folder which has Image and Annotations together and set the path "arr" to this current Directory and Run 


                                         ********** duplicate_remover.py ***********

This Script is Used for Removing Unannotated Data done using LabelImg or LabelMe Tool . In Many Images there may not be objects to annotate , that image will not have its corresponding .XML File , hence it may contribute as a Negative Weight while Training Data.
So to prevent that this code is written , which removes all Unannotated Images from the directory .

For eg : A folder contains [ image1.jpg , image1.xml , image2.jpg , image3.jpg , image3.xml] Here image2 is unannotated , so it does not            have its corresponding xml . After running this script the directory content is given as follows
         [ image1.jpg , image1.xml , image3.jpg , image3.xml] , here we see image2.jpg is removed .
       
To run this script : image_directory stores the cureent directory of this file location , to run a script on a specific folder change
                     'day more' to the folder name and Run this script
                     
                     
                     
                                          ************* file_renamer.py **************
                                          
 This script is to rename the Files and serialize them accordingly so as to make the Dataset Clean and Organized for Training
 
 For eg: A folder contains [ image1.jpg , image1.xml , image3.jpg , image3.xml , image11.jpg ,image11.xml ] . Here image2 ,....image10            is missing / removed by duplicate_remover.py script , now this data is not Arranged , if we run this file_renamer.py script on          this folder then the folder content is [ image_1.jpg , image_1.xml , image_2.jpg , image_2.xml , image_3.jpg ,image_3.xml ] ,            so here all data is arranged and renamed in ascending order like image3.jpg got renamed to image_2.jpg and so on

To run this script: image_directory stores the cureent directory of this file location , change 'day more' to the folder name on which                       it will be applied , and mention from where to start counting by setting the start value to count_n variable and run



                                        ************* Order to Run the Script **************
                                        
                                           1. Run the rename.py on a Directory 
                                           2. Then Run duplicate_remover.py on the Directory
                                           3. Then Run file_renamer.py on the Directory
