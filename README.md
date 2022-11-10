# ML Zoomkcamp Midterm Project

The Dataset for this work is from [Zindi Africa](zindi.africa) Financial Inclusion in Africa [Challenge](https://zindi.africa/competitions/financial-inclusion-in-africa)

The objective of the competition is to create a machine learning model to predict which individuals are most likely to have or use a bank account. 

You are asked to predict the likelihood of the person having a bank account or not (Yes = 1, No = 0), for each unique id in the test dataset.

#
**Please follow the setup instructions below. Note that all the code in this repository is written and tested on a Linux 
machine**

- OS:  Ubuntu 20.04 LTS
- Python: 3.10
- pip: 22.2.1
#
# VENV Setup

Create a Virtual Environment named 'midterm-project'

- `python3 -m venv midterm-project`

Activate your virtual environment

- `source midterm-project/bin/activate`

Install packages and dependencies

- `pip install -r requirements.txt`

Run the app using *gunicorn*

- `gunicorn --bind 0.0.0.0:9696 predict:app`

#
# Docker Setup
## How to Build a Docker Image

Build Docker Image

- `docker build --tag midterm-project .`

Run image as a container

To locate our image with the tag you created above, run the command below

- `docker images`

Choose the image you want to run and execute the docker `run command` followed by the image name

- `docker run image_name:tag`

After succesfully runing the command above, you will see that docker is running.

If you try running the app in your browser, you will get `This site can’t be reached localhost refused to connect`. This is because the app is running in isolation mode.

The solution is to run the image in detached mode which will enable you to view the application in the browser rather than the container.

 Rerun the `docker run` command and append this additional tags: "-d" to run it in detached mode and "-p" to specify the port to be exposed; as shown below

 `docker run -d -p 9696:9696 midterm-project`

 This will make our application accessible on our machines' **port 9696**

#
### Test the app by running **predict-test.py** 

- `python3 predict-test.py`

#
### **Files**

- Dataset: [Train.csv](Train.csv), [Test.csv](Test.csv), [SampleSubmission.csv](SampleSubmission.csv), [VariableDefinition.csv](VariableDefinition.csv)
- Model: [zindi-fi.bin](zindi-fi.bin), [dv.bin](dv.bin)
- Prediction: [predict.py](predict.py), [predict-test.py](predict-test.py)
- Jupyter Notebook: [Zindi_Financial_Inclusion.ipynb](Zindi_Financial_Inclusion.ipynb), [predict-test.ipynb](predict-test.ipynb)
- Other: [requirements.txt](requirements.txt), [Dockerfile](Dockerfile)

