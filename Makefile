all:
	pip3 install -r requirements.txt && chmod +x bumble-swiper.py
install:
	pip3 install -r requirements.txt && cp bumble-swiper.py /bin/bumble-swiper && chmod +x /bin/bumble-swiper
