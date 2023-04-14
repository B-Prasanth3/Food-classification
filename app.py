import cv2
import streamlit as st
import tensorflow as tf
import os
import numpy as np
import PIL
import pandas as pd

## Page Title
st.set_page_config(page_title = "Food Classification")
st.title("FOOD CLASSIFICATION")
st.markdown("------")


model_path="foodc.tflite"



# Load the labels into a list
classes = [ 'dal_makhani','dhokla','fried_rice','idli','jalebi','kaathi_rolls','kadai_panner','masala_dosa','kulfi','pizza','samosa','.']
#label_map = model.model_spec.config.label_map
#for label_i
