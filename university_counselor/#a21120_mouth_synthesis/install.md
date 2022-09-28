# 安装依赖

https://github.com/PaddlePaddle/PaddleGAN/blob/develop/docs/zh_CN/install.md


因为aws的ec2实例带了conda，可以直接从
https://www.paddlepaddle.org.cn/documentation/docs/zh/install/conda/linux-conda.html
的： 
conda create -n paddle_env python=3.6 
开始


进入虚拟环境：
conda activate paddle_env


python tools/wav2lip.py \
    --face ../docs/imgs/mona7s.mp4 \
    --audio ../docs/imgs/guangquan.m4a \
    --outfile pp_guangquan_mona7s.mp4 \
    --face_enhancement