
<h1 align="center">Twitter Data Analysis</h1>
<div>
<a href="https://github.com/Ammon21/Twitter-Data-Analysis/network/members"><img src="https://img.shields.io/github/forks/Ammon21/Twitter-Data-Analysis" alt="Forks Badge"/></a>
<a href="https://github.com/Ammon21/Twitter-Data-Analysis/pulls"><img src="https://img.shields.io/github/issues-pr/Ammon21/Twitter-Data-Analysis" alt="Pull Requests Badge"/></a>
<a href="https://github.com/Ammon21/Twitter-Data-Analysis/issues"><img src="https://img.shields.io/github/issues/Ammon21/Twitter-Data-Analysis" alt="Issues Badge"/></a>
<a href="https://github.com/Ammon21/agriTech-USGS-LiDAR/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/Ammon21/Twitter-Data-Analysis?color=2b9348"></a>
<a href="https://github.com/Ammon21/Twitter-Data-Analysis/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Ammon21/Twitter-Data-Analysis?color=2b9348" alt="License Badge"/></a>
</div>

</br>

<!-- ![logo](https://logos-world.net/wp-content/uploads/2020/04/Twitter-Logo-2010-2012.png) -->
<!-- ![phone with logo](https://insidebusiness.ng/wp-content/uploads/twitter-1.jpg) -->
![tweeter_logo](images/twitter-featured.png)

## What Is Twitter Data?

Twitter data is the information collected by either the user, the access point, what’s in the post and how users view or use your post. While this might sound somewhat vague, it’s largely due to the massive amount of data that can be collected from a single Tweet.

With this information, you can know demographics, total clicks on your profile or how many people saw your Tweet. This is just the tip of the iceberg, but understanding the data allows you to know how it’s used and the patterns of your content.

## How the data is collected?

Twitter is the Major Source of data for our challenge. We were provided with pre-downloaded data on Economic hardships-related topics. The data comes in two parts.

*1.* The first will be around 100MB of a raw twitter data dump in JSON format. This data is collected using the following keywords: [‘inflation’, ‘fuelprice’, ‘fuelpricehike’, ‘ fuelprices’, ‘fuelshortage’, ‘foodprice’, ‘oilprice’, ‘oilprices’, ‘cookingoilprice’, ‘unemployment’, ‘unemploymentrate’, ‘economiccrisis’, ‘economichardship’]

*2.* The second one will be around 300MB of the same format, but collected based on the original keyword plus country-specific geocodes included e.g. ‘0.0263,37.9062,530km for Kenya’. 

## Extracting tweets from Twitter raw JSON file

To load the data from JSON format we need to install the required libraries. We will have to load the Twitter data into a pandas data frame using different types of python functions like **find_status_count()**, **find_hashtags()**, and **find_retweeted_text()**. Using this many functions, we need to append every tweet into a list and at the end, we will get the extracted data in the form of a CSV file.

<hr>

## Table of Contents

- [Introduction](##Introduction)
- [Project Structure](#project-structure)
  - [data](#data)
  - [notebooks](#notebooks)
  - [scripts](#scripts)
  - [tests](#tests)
  - [models](#models)
  - [root folder](#root-folder)
- [Installation guide](#installation-guide)

<hr>


## Project Structure

### [images](images):

- `images/` the folder where all snapshot for the project are stored.

### [models](models):

- `models/` the folder where script logs are stored.

### [data](data):

- `data/` the folder where the dataset files are stored.

### [.github](.github):

- `.github/`: the folder where github actions and unit-tests are integrated.

### [.vscode](.vscode):

- `.vscode/`: the folder where local path are stored.

### [notebooks](notebooks):

- `notebooks`: a jupyter notebook for preprocessing the data.

### [scripts](scripts):

- `scripts/`: folder where modules are stored.

### [tests](tests):

- `tests/`: the folder containing unit tests for the scripts.

### root folder

- `requirements.txt`: a text file lsiting the projet's dependancies.
- `.travis.yml`: a configuration file for Travis CI for unit test.
- `setup.py`: a configuration file for installing the scripts as a package.
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.

<hr>

# <a name='Installation guide'></a>Installation guide

### <a name='conda'></a>Conda Enviroment

```bash
conda create --name mlenv python==3.8
conda activate mlenv
```

then

```bash
git clone https://github.com/Ammon21/Twitter-Data-Analysis.git
cd Twitter-Data-Analysis
sudo python3 setup.py install
```

<hr>