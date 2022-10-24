from bing_image_downloader import downloader

index = input('무슨사진을 검색할까요?')

limit = input('몇장을 모을까요?')

limit = int(limit)

downloader.download(index, limit,  output_dir=index+'사진', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)