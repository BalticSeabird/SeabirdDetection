FROM nvcr.io/nvidia/cuda:11.6.2-base-ubuntu20.04

ENV DEBIAN_FRONTEND="noninteractive"

# Downloads to user config dir
ADD https://ultralytics.com/assets/Arial.ttf \
   https://ultralytics.com/assets/Arial.Unicode.ttf \
   /root/.config/Ultralytics/

# Install linux packages
RUN apt-get update && apt-get install --no-install-recommends -y \
   zip htop tmux git \
   libgl1-mesa-glx libglib2.0-0 \
   python3-dev python3-pip 

# Install pip packages
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt \
   --extra-index-url https://download.pytorch.org/whl/cu113

WORKDIR /app

# Set environment variables
ENV OMP_NUM_THREADS=18
