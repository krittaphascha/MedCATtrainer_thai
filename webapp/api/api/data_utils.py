import pandas as pd

from .models import *

_MAX_DATASET_SIZE_DEFAULT = 10000

def dataset_from_file(dataset: Dataset):
    df = None
    if '.csv' in dataset.original_file.path:
        df = pd.read_csv(dataset.original_file.path)
    elif '.xlsx' in dataset.original_file.path:
        df = pd.read_excel(dataset.original_file.path)

    df.columns = [c.lower() for c in df.columns]

    if df is not None:
        max_dataset_size = os.environ.get('MAX_DATASET_SIZE', _MAX_DATASET_SIZE_DEFAULT)
        if df.shape[0] > max_dataset_size:
            raise(f'Attempting to upload a dataset with {df.shape[0]} rows. The Max dataset size is set to'
                  f' {max_dataset_size}, please reduce the number of rows or contact an admin to increase the max size')

        if 'text' not in df.columns or 'name' not in df.columns:
            raise Exception("Please make sure the uploaded file has a column with two columns:'name', 'text'. "
                            "The 'name' column are document IDs, and the 'text' column is the text you're "
                            "collecting annotations for")

        for i, row in enumerate(df.iterrows()):
            row = row[1]
            text = row['text']
            if 'name' in df.columns:
                name = row['name']
            else:
                name = f"Doc {i}"

            document = Document()
            document.name = name
            document.text = text
            document.dataset = dataset
            document.save()
    else:
        raise Exception("Please make sure the file is either a .csv or .xlsx format")


def delete_orphan_docs(dataset: Dataset):
    Document.objects.filter(dataset__id=dataset.id).delete()
