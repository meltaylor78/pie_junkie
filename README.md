
load all from req.txt > pip3 install -r requirements.txt
> python3.8 -m pip install --upgrade pip

Features : Issues and fixes. 

As partt of the products page, I want to diaplat the category or its a search result as the page header. 
An issue arose, when selecting All Rasperberry Pi or all All kits, it displated each category in sequecny. 
To resolve the issue, I updated the main nav page to pass in "All xxx" as the first category, this is not a valid DB value, 
so in the views I extract the first item from the array if the array is more that one and secure it as varilable to be used in the template. 

t