My personal airflow testing repo.

Pip install Airflow based on: [Airflow Install](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)

Set Airflow home as:
```
export AIRFLOW_HOME=~/airflow # bash, zsh
set export AIRFLOW_HOME ~/airflow # FISH
```

We want ETLephant to be callable by Airflow and need to pip install it for our conda env
```
pip install ~/Code/github.com/suplari/etlephant
```
To run airlfow `cd` to your airlfow directory and run command:
```
airlfow standalone
```

TODO:
- Shift airflow dependences into conda/ pyenv environment.
- Dockerize airflow with ETLephant and CS repo scripts, will aid in porting pipelines to other machines.
- Form DAGs into multi-node frameworks, improve pipeline visability.
- 
