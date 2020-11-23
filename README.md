

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://img.icons8.com/material-outlined/24/000000/vision.png">
    <img src="https://img.icons8.com/material-outlined/96/000000/vision.png/" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">data-labeler</h1>
  
  <p align="center">
    Extracts object from raw images to train machine learning or deep learning models.
    <br />
    <br />
    <a href="https://github.com/YigitGunduc/data-labeler/">View Demo</a>
	  <br />
    <a href="https://github.com/YigitGunduc/data-labeler/issues">Report Bug</a>
	  <br />
    <a href="https://github.com/YigitGunduc/data-labeler/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

## Raw Image

![demo-image](https://raw.githubusercontent.com/YigitGunduc/data-labeler/master/raw_data/Street.jpg)

## Extracted Data
<table>
  <tr>
     <td>Extracted Person</td>
     <td>Extracted Car</td>
     <td>Extracted Bus</td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/YigitGunduc/data-labeler/master/labeled_data/person/0.8429918080208526.jpg" width=270 height=480></td>
    <td><img src="https://raw.githubusercontent.com/YigitGunduc/data-labeler/master/labeled_data/car/0.44490062036087263.jpg" width=270 height=480></td>
    <td><img src="https://github.com/YigitGunduc/data-labeler/blob/master/labeled_data/bus/0.6067948416207635.jpg?raw=true" width=270 height=480></td>
  </tr>
 </table>

This project labels raw images for your machine learning, deep learning, or computer vision tasks. 
By far this is the easiest and the most effective data labeling took out there.

Here is why:
* Completely open-source and free for everyone
*	Most east data labeling software out there.
*	Always in development so new features are coming in daily

### Built With

This project is built using Python, OpenCV, and Yolo for more information I put the links down below.

* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [Yolo](https://pjreddie.com/darknet/yolo/)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This section explains and goes thought how to install and setup everything
* pip
```sh
pip install -r requirements.txt
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/YigitGunduc/data-labeler.git
```
2. Install Yolo [Yolo website link](https://pjreddie.com/darknet/yolo/)
 
* Go to the Yolo's website
* Install yoloV3.weights 
* Place it in the 'yolo' folder

<!-- USAGE EXAMPLES -->
## Usage
* Put the images you want to extract the object from in the raw data folder.

* To label, data run the 'data labeler.py' file, it will go through all of the 
images and extract objects from each photo and put extracted images to the 
corresponding folder.


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/YigitGunduc/data-labeler/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/YigitGunduc/data-labeler](https://github.com/YigitGunduc/data-labeler)





[contributors-shield]: https://img.shields.io/github/contributors/YigitGunduc/data-labeler.svg?style=flat-rounded
[contributors-url]: https://github.com/YigitGunduc/data-labeler/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/YigitGunduc/data-labeler.svg?style=flat-rounded
[forks-url]: https://github.com/YigitGunduc/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/YigitGunduc/data-labeler.svg?style=flat-rounded
[stars-url]: https://github.com/YigitGunduc/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/YigitGunduc/data-labeler.svg?style=flat-rounded
[issues-url]: https://github.com/YigitGunduc/data-labeler/issues
[license-url]: https://github.com/YigitGunduc/data-labeler/blob/master/LICENSE
[license-shield]: https://img.shields.io/github/license/YigitGunduc/data-labeler.svg?style=flat-rounded