FROM public.ecr.aws/lambda/python:3.11

# copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# install specified packages
RUN yum install gcc libxml2-devel libxslt-devel python-devel -y

# install specified packages
RUN pip install -r requirements.txt

# copy all files in .src/
COPY src/* ${LAMBDA_TASK_ROOT}

# set the CMD to your handler
CMD [ "app.run" ]