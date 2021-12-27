if [ -d /root/miniconda3 ]; then export PATH=/root/miniconda3/bin:$PATH; fi
bash yum install -y graphviz
pip install --upgrade pip
