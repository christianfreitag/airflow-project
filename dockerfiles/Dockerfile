ARG AIRFLOW_VERSION=${AIRFLOW_VERSION}
ARG PYTHON_VERSION=${PYTHON_VERSION}

FROM apache/airflow:${AIRFLOW_VERSION}
USER airflow
WORKDIR /opt/airflow
COPY requirements.txt /home
RUN pip3 install --no-cache-dir apache-airflow==${AIRFLOW_VERSION} -r /home/requirements.txt