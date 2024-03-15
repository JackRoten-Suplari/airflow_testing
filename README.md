My personal airflow testing repo.


Set Airflow home. This step of setting the environment variable should be done before installing Airflow so that the installation process knows where to store the necessary files.
```
export AIRFLOW_HOME=~/airflow # bash, zsh
set export AIRFLOW_HOME ~/airflow # FISH
```

Build conda env for "airflow_testing":
```
git clone git@github.com:suplari/airflow_testing.git
cd airflow_testing
conda env create -f environment.yml
conda activate airflow_testing
pip install --upgrade pip
pip install -e .
git config core.hooksPath .githooks
```

Make sure Pip is up to date with:


Pip install Airflow based on: [Airflow Install](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html). Current pip installed package:
```
pip install "apache-airflow[celery]==2.8.1" --constraint "my-constraints.txt"
```


We want ETLephant to be callable by Airflow and need to pip install it for our conda env
```
pip install ~/Code/github.com/suplari/etlephant
```
Other pip install packages currently needed. TODO: move to dependency file
```
pendulum
google-re2
```

To run airlfow `cd` to your airlfow directory and run command:
```
airlfow standalone
```

TODO:
- Shift airflow dependences into conda/ pyenv environment.
- Dockerize airflow with ETLephant and CS repo scripts, will aid in porting pipelines to other machines.
- Form DAGs into multi-node frameworks, improve pipeline visability.
