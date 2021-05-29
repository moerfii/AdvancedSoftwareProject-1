# frontend

This folder holds the code for the frontend.  
  
`components/` holds code for individual components. There are four components - form, map and compare that corresponds to home, map and wish list screen in our app. We also created filtering components to handled filtering codes isolatedly.  
`icons/` holds icons and images used by the frontend.  
`mapViewOverride/` holds a modified source file from the mapview module, which we had to modify.


# How to use our FairBNB desktop app 

Once you run the app, you will see the **form** page which is our home screen.
On the top-left corner, there is a hamburger button where you can go through all the screens (form, wish list and map) in our app. 

Search form takes several inputs to find your best accomodation - neighborhood, guests, age, high rating, super host, fair filter, interests and price. 

`Neighborhood/` You can choose a borough : Bronx, Brooklyn, Manhanttan, Queens and Staten Island.
`Guest/` You can fill in the number of guests from 1 to 16. This form can be empty if you travel alone.
`Age/` You can choose your age groups : 18-30, 31-50 and 50+ 
`High rating/` You can check the box if you want to see the listings which has more than 4 starts rating.
`Super host/` You can check the box if you want to see the listings from super host
`Fair filter/` You can chexk the box if you want to see the listing which is rented legally. By the law of NYC, the host can not rent more than one listing so we filtered out the listings that is rented out from same hosts.
`Interests/` You can choose multiple interests that you are looking for during your stays. We pre-assigned specific interests to certain neighborhood and based on this, listings will be returned. 
`Price/` You can set the range of your budget with slider. If you want to set it precisely, you can manually type the price in the fill-in form as well. 

After fill in the search form and click the search button, it will bring you to **map** page, where you can see the result of listings that fits to you. 
You can zoom-in and out throug the map to see more/less specific accomodation. You will see the clusters of listing untill you reach the one specific accomodation. When you see the red marker on the map, you can click it then deatil information will pop up. There, you can click the heart icon to add it to the wish list, or you can click magnifier icon which will take you to the airbnb web page of that listing. 

Once you are done with the selecting accomodations, you can go to **wish list** menu and see the comparison of listing that you chose. 
We added labels - "best rating" and "best price" that can make your decision easy. 

