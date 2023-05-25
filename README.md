![GitHub repo size](https://img.shields.io/github/repo-size/JanaRobbins/scripts-folium?style=plastic)  ![GitHub last commit](https://img.shields.io/github/last-commit/JanaRobbins/scripts-folium?style=plastic) ![GitHub watchers](https://img.shields.io/github/watchers/JanaRobbins/scripts-folium?style=plastic) ![GitHub repo directory count](https://img.shields.io/github/directory-file-count/JanaRobbins/scripts-folium?style=plastic) ![](https://komarev.com/ghpvc/?username=JanaRobbins&style=plastic&label=Profile+views&color=ff69b4)



# **Creating a web map using FOLIUM**
## **Charity walk in Mourne Mountains** 

### Project Description:

The code will create a web map for a 12 km charity walk in Mourne Mountains. If you fork the repository you will be able to create a similar map like the one below for your website. You can use the code for your own project and you can change location, data and pictures. The code and many other features added could be left the same for your map. 

### Table of contents
1. [Map description](#1)
2. [How to Install and Run the Project](#2)
   1. [Getting started](#2.1) 
   2. [Create a Conda environment](#2.2)
   3. [Starting Pycharm](#2.3)
3. [How to Use the Project](#3)
4. [Adding the Map into a Real Website](#4)
5. [Credits](#5)
6. [Licence](#6)



## 1. Map description:<a name="1"></a>

-	A green line in the map is for a charity walk in the Mourne Mountains with seven points of interest added as markers. Popups have pictures, text and a hyperlink. Png pictures are used as custom icons. Any Polyline and markers could be added this way.
-	There are two GeoJson files imported. Polygon for the Mourne wall (yellow line with a transparent filling) and purple Polylines for the walking paths. The code could be used with your own GeoJson file.
-	Three csv files were used and you can see them in the folder 'data_files'. Parking around the Mournes and climbing cracks are using png pictures as custom icons and Mournes peaks are using Folium markers divided into four categories per height. You can see the latitude, longitude, Irish grid and the height in the popups.
-	A floating image is added to this map – logo 'J' and two legends. Legends were created as a picture in 3D Paint. 
-	Text with an absolute position is added to the map.
-	There features can be used in your own maps – mini map, find my position, zoom, measure control, location coordinates on the map, mouse position, search box, layer control and a full screen button. 
-	Layer control is set for four base layers and GeoJson files. 
 

<img src="https://github.com/JanaRobbins/scripts-folium/blob/main/images/walk.jpg" width="70%" height="70%">

Image shows an overview of the project (walk.html)


## **2. How to Install and Run the Project**<a name="2"></a>

###     i. Getting started<a name="2.1"></a>

To be able to share or download any code a [GitHub](https://github.com/) account is needed, [git](https://git-scm.com/downloads), command-line interface (GitHub, Inc. 2023) and  [Conda/Anaconda](https://docs.anaconda.com/anaconda/install/) (open-source package management system) installed.  

###     ii. Create a Conda environment<a name="2.2"></a>

To be able to push (upload) or pull (download) changes to and from remote repositories a graphical user interface [GitHub Desktop](https://desktop.github.com/) has to be installed to work with git and GitHub. 
A code could now be forked to your repository - [GitHub - JanaRobbins/scripts-folium](https://github.com/JanaRobbins/scripts-folium).

Open GitHub and you will be able to have it on your computer, this should now be cloned (downloaded) to your computer and created a local version and it will show as JanaRobbins/scripts-folium. You can use a Command Prompt – cd c:\Users\user\name_for_projects than adding a git clone https://github.com/your_username_in_GitHub/scripts_folium.git  
Setting up [Conda/Anaconda](https://docs.anaconda.com/anaconda/install/), an open-source package management system using command line CLI and GUI.  
Copy environment.yml, change it if needed in Notepad++ the name is now scripts-folium, a list of channels could be the same and dependencies could be extended.  

- name: scripts-folium
- channels: - conda-forge - defaults
- dependencies: - python=3.9 
                – geopandas 
                - folium 
                – pandas


###     iii. Starting Pycharm<a name="2.3"></a>

Now you need to install [PyCham](https://www.jetbrains.com/pycharm/download/) Community Edition, IDE – Integrated Development Environment to work with your code. A location was created in the files folders: Users\user\jana\script-folium. An interpreter was added to the project. This is the Conda executable c:\users\user\anaconda3\python.exe and an existing environment scripts-folium.


## **3.	How to Use the Project**<a name="3"></a>

All data and images for the code could be found in the folder 'data_files' and 'images' that were created nd taken by the author. 
If your own data is used for this code, the names should be changed accordingly to your project. 

## **4. Adding the Map into a Real Website**<a name="4"></a>

The code created for the file Mourne_walk.py is saved into walk.html file. 
This file is ready to be used in a real website. Place your code into walk html or copy and past the code from walk.html into your own html page.  

```html
<!DOCTYPE html>
<html>
<head>
<!-- copy the script, styles and link here from the walk.html file from the head section -->
</head>
<body>
<!-- copy here div class from the body part -->
<div class="folium-map" id="map_11bb66f436a35a89aa8cad157e5e4d09" ></div>
</body>
<!-- copy here the script from the part between </body> and </html> -->
<script>
</script>
</html>
```

## **5. Credits**<a name="5"></a>

The code was created during the study of the module Programming for GIS and Remote Sensing in the School of Geography and Environmental Sciences in the [University of Ulster](https://www.ulster.ac.uk/courses/202324/geographic-information-systems-30225).  


## **6. Licence**<a name="6"></a>

A MIT licence was used. To use this code, data and or images please contact the author at janarobbins.gis@gmail.com 