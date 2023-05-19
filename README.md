![GitHub repo size](https://img.shields.io/github/repo-size/JanaRobbins/scripts-folium?style=plastic)  ![GitHub last commit](https://img.shields.io/github/last-commit/JanaRobbins/scripts-folium?style=plastic) https://redirect.viglink.com/?format=go&jsonp=vglnk_168453623016917&key=eac202ea7a96cf485281d6c4ffa2069e&libId=lhv57nf00103es17000UL46zl9gql&loc=https%3A%2F%2Fwww.makeuseof.com%2Fbadges-that-will-supercharge-JanaRobbins-scripts-folium%2F&gdprConsent=CPsA1gAPsA1gAAJAEBENDFCsAP_AAH_AACiQJbtX_H__bW9r8f5_aft0eY1P9_j77qQzDhfNk-4F3L_W_JwX52E7NF36tq4KmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYGF5umxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IL9778v8v8_9_rk2_eX_3_79_7_H9-f_84JcAEmGrcQBdmUODNoGEUCIEYVhARQKACCgGFogIAHBwU7IwCfWESAFAKAIwIgQ4AoyIBAAAJAEhEAEgRYIAAABAIAAQAIBEIAGBgEFABYCAQAAgOgYohQACBIQJEREQpgQFQJBAS2VCCUF0hphAFWWAFAIjYKABEEgIrAAEBYOAYIgBKxYIEmINogAGAFAKJUK1FJ6aAhYzMAAAA.f_gAD_gAAAAA&gdprApplies=true&v=1&type=U&opt=true&optExText=false&out=https%3A%2F%2Fhitcounter.pythonanywhere.com%2Fcount%2Ftag.svg%3Furl%3Dhttps%3A%2F%2Fgithub.com%2FTanu-N-Prabhu%2FPython&ref=https%3A%2F%2Fwww.bing.com%2F&title=Top%205%20Badges%20That%20Will%20Take%20Your%20GitHub%20Repository%20to%20the%20Next%20Level&txt=https%3A%2F%2Fhitcounter.pythonanywhere.com%2Fcount%2Ftag.svg%3Furl%3Dhttps%3A%2F%2Fgithub.com%2FTanu-N-Prabhu%2FPython


# **Creating a web map using FOLIUM**
## **Charity walk in Mourne Mountains** 

### Project Description:

you will be able to create the map like the one below for your website. You can use my code for your own project and could change location, data and pictures. Codes and many other features added could be left the same for your map. 

### Table of contents
1. [Map description](#1)
2. [How to Install and Run the Project](#2)
   1. [Getting started](#2.1) 
   2. [Create a conda environment](#2.2)
   3. [Starting Pycharm](#2.3)
3. [How to Use the Project](#3)
4. [Credits](#4)
5. [Licence](#5)



## 1. Map description:<a name="1"></a>

-	A green line in my map is for a charity walk in Mourne Mountains with seven points of interest added as markers. Popups have picture and a text and/or a hyperlink. Png picture is used as custom icon. Any Polyline and markers could be added this way.
-	There are two GeoJson files imported. Polygon for the Mourne wall (yellow line with a transparent filling) and purple Polylines for the walking paths. The code could be used with your own GeoJson file.
-	Three csv files were used and you can see them in the folder data_files. Parking around the Mournes and climbing cracks are using png picture as custom icons and Mournes peaks using folium markers divided into four categories per height. You can see the latitude, longitude, Irish grid and the height in the popup.
-	A float image is added to this map – logo “J” and two legends. Legends were created as a picture in Paint 3D. 
-	Text with an absolute position is added to the map.
-	Other features you can use for any map – mini map, find my position, zoom, measure control, location coordinates on the map, mouse position, search box, layer control and a full screen button. 
-	Layer control is set for four base layers and GeoJson files. 
 

<img src="https://github.com/JanaRobbins/scripts-folium/blob/main/images/walk.jpg" width="50%" height="50%">

Image shows an overview of the project (walk.html)


## **2. How to Install and Run the Project**<a name="2"></a>

###     i. _Getting started_<a name="2.1"></a>

To be able to share or download any code a [GitHub](https://github.com/) account is needed, [git](https://git-scm.com/downloads), command-line interface (GitHub, Inc. 2023) and  [Conda/Anaconda](https://docs.anaconda.com/anaconda/install/) (open-source package management system) installed.  

###     ii. _Create a conda environment_<a name="2.2"></a>

To be able to push (upload) or pull (download) changes to and from remote repositories a graphical user interface [GitHub Desktop](https://desktop.github.com/) has to be installed to work with git and GitHub. 
A code could now be forked to your repository - GitHub - JanaRobbins/scripts-folium: A script for an interactive map using Folium and saved as HTML file - [https://github.com/JanaRobbins/scripts-folium](https://github.com/JanaRobbins/scripts-folium).

Open GitHub and you will be able to have it on your computer this should be now cloned (downloaded) to your computer and created local version and it will shows as JanaRobbins/scripts-folium. You can use a Command Prompt – cd c:\Users\user\name_for_projects than add git clone https://github.com/your_username_in_GitHub/scripts_folium.git  
Setting up [Conda/Anaconda](https://docs.anaconda.com/anaconda/install/) , open-source package management system using command line CLI and GUI.  
Copy environment.yml, change it if needed in Notepad++ the name is now scripts-folium, list of chanels could be the same and dependencies can be extended.  

name: scripts-folium
channels: - conda-forge - defaults
dependencies: - python=3.9 
              – geopandas 
              - folium 
              – pandas


###     iii. _Starting Pycharm_<a name="2.3"></a>

Now you need to install [PyCham](https://www.jetbrains.com/pycharm/download/) Community Edition, IDE – Integrated Development Environment to work with your code. In my case I created a location in file folders : Users\user\jana\script-folium. I added an interpreter for your project. In my case this is Conda executable c:\users\user\anaconda3\python.exe and existing environment scripts-folium.


## **3.	How to Use the Project**<a name="3"></a>

All data and images for the code could be found in the folder data_files and images were created/taken by the author. 
If your own data is used for this code, the names should be changed accordingly to your project. 


## **4. Credits**<a name="4"></a>

The code was created studying the module Programming for GIS and Remote Sensing in the School of Geography and Environmental Sciences in the [University of Ulster](https://www.ulster.ac.uk/courses/202324/geographic-information-systems-30225).  


## **5. Licence**<a name="5"></a>

I am using a MIT licence. I you will use my code, data or images please let me know to my email janarobbins.gis@gmail.com 
Thank you for looking at my code and work. 

 
