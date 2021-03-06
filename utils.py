import logging
import pickle
import gzip
import os

logging.basicConfig(format='%(asctime)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().setLevel(logging.INFO)


def load_object(path) -> object:
    """
    Load object from pickle gzip file
    :param path: path to file needed to load
    :type path: str
    :return: object stored in file, None if file not existed
    :rtype: object
    """

    if not os.path.isfile(path):
        raise FileNotFoundError

    with gzip.open(path, 'r') as dat_file:
        return pickle.load(dat_file)


def save_object(path, obj_file) -> object:
    """
    Save object to pickle gzip file.

    Args:
        path (str): path to file needed to store
        obj_file (object): object needed to store

    Returns: object
    None if object is None
    """
    if obj_file is None:
        return None

    if os.path.isfile(path):
        logging.warning(f"=> File {path} will be overwritten.")
    else:
        try:
            os.makedirs(os.path.dirname(path))
        except FileExistsError:
            logging.warning(f"=> Folder {path} exists.")

    with gzip.open(path, 'w+') as dat_file:
        pickle.dump(obj_file, dat_file)
