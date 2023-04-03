import os
import __main__


def get_image(img: str):
    main_dir = os.path.dirname(__main__.__file__)
    data_dir = os.path.join(main_dir, "data")
    return os.path.join(data_dir, img)
