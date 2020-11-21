
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

![demo-image](https://pjreddie.com/media/image/Screen_Shot_2018-03-24_at_10.48.42_PM.png)

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
git clone https://github.com/github_username/repo_name.git
```
2. Install Yolo [Yolo website link](https://pjreddie.com/darknet/yolo/)

To install Yolo I already put yoloV3.cfg and coco.names file but due to the file
size, Github doesn't let me put yoloV3.weights file here, but it is easy to install and well 
documented so I don't believe you will have a hard time installing it. To install 
yoloV3.weights file check the link(https://pjreddie.com/darknet/yolo/) after your installed 
it put it on the C:/user/repo/yolo folder. When you run the program Python will check to 
see Yolo.weights file/


<!-- USAGE EXAMPLES -->
## Usage

To use the project place your raw images in the 'raw_images_folder' when you 
run the program with 'python data-labeler.py' command  it will go through all of them 
and extract objects from each photo and put extracted images to the corresponding 
folder in 'labeled_data' folder.


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