# Best-practices documentation for modifying the website 

## Setup and requirements
The website is developed with [hugo](https://gohugo.io/) and requires
* `hugo-extended` version
* `go`
Follow instructions on [this page](https://wowchemy.com/docs/install-locally/) to install hugo and dependencies.

Next step is to clone the repository
* cd into a directory you want to have the file in
* git clone this repository: `git clone https://github.com/combine-org/combine-org.github.io.git`
* change into the folder: `cd combine-org.github.io`
* run the hugo server: `hugo server`
* check it is up and running at `http://localhost:1313`
  
## Changing pages
* create a branch for the changes
* Page about website structure: https://wowchemy.com/docs/get-started/

## Publications
For updating publications follow the instructions here: https://wowchemy.com/docs/managing-content/#create-a-publication
Then run the cleanup_hugo_tagging.py script (make sure the path is to the publications folder) to clean up the extra "" in tags.

## Website Structure Overview

* The general file structure looks like this: https://wowchemy.com/docs/get-started/#remove-any-unused-example-pages
* You can figure out which folders correspond to which tabs on the menu by looking at menus.toml under config\_default
  * for example the "People" tab can be accessed via <website url>/People-Genetic-Logic-Lab and the web code for the content of the page is found under content/People-Genetic-Logic-Lab
* Individual webpages are built using the index.md or _index.md file in the content folder. There are two types of index file:
  * _index.md: it is a simple functionality that displays the rest of the content from the folder based on the view style chosen. It is flanked by "---" at the start and end of the file. Example:

~~~~
---
title: Publications
# View.
#   1 = List
#   2 = Compact
#   3 = Card
#   4 = Citation
view: 1
# Optional header image (relative to `static/media/` folder).
header:
  caption: ""
  image: ""
---
~~~~
  
  * index.md: It is a widget page (A page that will include widgets). The page is flanked by "+++" at the top and bottom. Example:

 ~~~~
+++
# People
type = "widget_page"
headless = false  # Homepage is headless, other widget pages are not.
+++
 ~~~~

* Widgets

  Widgets are functions which take in parameters and generate html code accordingly. There are 3 parts to a widget:

  **Widget Call:** This is an .md file in the directory where the widget is being called. E.g. publications.md in the home directory under content. It is flanked by "+++" and contains the name of the widget being called (in the example case pages), provides a series of parameters for the function to work (headless, active, weight, title, subtitle) and widget specific parameters (content.filters, design, design.background, custom css). For examples of the widget call function for each of the different widgets see /themes/academic/exampleSite/content/home and open any of the .md files other than index.

  **Widget Function:** A widget function is called based on the widget parameter in the widget call. The widget is code (Go's html/template and text/template libraries) interspersed with code to build it (you have functionality like if statements, loops, etc, for more info see: https://gohugo.io/templates/introduction/). There are two locations where the widgets are found: /themes/academic/layouts/partials/widgets or any custom widgets are found in layouts/partials/widgets

  **Widget Data:** The widget may not have anymore data than the parameters provided in the widget call (this is the case for widgets like featurette) or they might link out to get more information (for example the people widget obtains its information by looping through all authors files and filling in the template using the information provided in the author's index file e.g. Chris Myers/_index.md)

* Partials

  Widgets are a subset of partials. Partials are html files that contain go code and are used to provide the general structure of the web page, e.g the navbar, the citation views, page footer etc. You can go in and edit them too but I suggest leaving them alone for now

* Images

  Any image files not associated with authors should go in the static\media file. It can be called in an html image tag using "/media/example.png"

  Author images go in the file associated with the author and must be named avatar.<extension> e.g. avatar.png or avatar.jpg

* CSS

  like most website there are css files. You can go in and edit them to change the way the page appears. Better practice is to use the file for custom scss located under themes\academic\assests\scss\custom.scss. Be careful overriding anything in here as it can drastically affect the way widgets works

## How To's:

* **Import new references**: 
  For this, please install and use the [Academic Import](https://github.com/wowchemy/hugo-academic-cli/#usage) command to import new references into the webpage. Please make sure to use the `--normalize` (for tag normalization), and `--overwrite` (to avoid reference duplicates) flags when importing references using the academic import command. Check out https://github.com/wowchemy/hugo-academic-cli/#usage for more information.

  Talking about tags, [Academic Import](https://github.com/wowchemy/hugo-academic-cli/#usage) will automatically generate tags for all references imported, created from a mixture of keywords and titles extracted from the bib information. However, sometimes this can go a-wire and add weird tags. This is why it is important to use the `--normalize` flag when importing using the academic import command. However, even with care, these tags can get weird. If any tag has a *"."* or a *"?"* or any other non-alphanumerical value, the site won't build. Please make sure you remove all characters that are not alpha-numerical from tags to run correctly.

* **Creating new event**:
  1) Copy Harmony-2021 folder, and fill up the template.
  2) Modify or add the "Events" tag under the "user_groups:" section.

* **Changing current event to past event**:
  1) Go to the event folder in \authors. In the index.md file, tag from "Events" to "Past Events" under the "user_groups:" section.
  2) Go to home/current.md and change author to new current event's id. If there is NO new current conference, comment out entire file.
  3) Go to events/current.md change author to new current event's id (Always have to have new event). If there is NO new current, comment out entire file.
   
* **Changing current event to future event**:
  1) Go to the event folder in \authors. In the index.md file, tag from "Events" to "Future Events" under the "user_groups:" section.
## Common error and mistakes

* Folders **must not** have any spaces. Use web-friendly hyphens instead.
