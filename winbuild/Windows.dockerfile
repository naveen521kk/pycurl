# Get the Python version of the base image from a build argument
ARG PYTHON_VERSION
FROM winamd64/python:$PYTHON_VERSION-windowsservercore

ARG WHEEL_NAME
ARG REQUIREMENT_FILE

# Copy and install the Windows wheel
COPY $WHEEL_NAME $WHEEL_NAME
RUN pip install $env:WHEEL_NAME

# Install the testing dependencies
COPY $REQUIREMENT_FILE $REQUIREMENT_FILE
RUN pip install -r $REQUIREMENT_FILE

# Copy the tests folder
COPY tests/ C:/dev/tests
WORKDIR C:/dev
