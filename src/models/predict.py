 def load_model():
#     # Should load and return the model.
#     # Optional, but if present will be loaded during
#     # startup in the "default-python" environment.
    import tensorflow as tf
    from transformers import BertTokenizer, BertModel, TFBertModel, TFBertForMaskedLM 
    from tokenizers import BertWordPieceTokenizer
    import warnings; warnings.filterwarnings('ignore')
    model = TFBertForMaskedLM.from_pretrained(pretrained_model_name)
    return model

def predict(inp, model=[]):
    # Called by default-python environment.
    # inp -- default is a string, but you can also specify
    # the type in "input_type.py".
    # model is optional and the return value of load_model.
    # Should return JSON.

    return {"result": "some output"}