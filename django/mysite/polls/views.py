from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.views.generic import TemplateView
import cv2
import tensorflow as tf
from tensorflow.keras.layers import Flatten, Conv2D, Activation, Dropout, Dense, MaxPooling2D
from tensorflow.keras.models import Sequential
from django.core.files.storage import FileSystemStorage
# from tensorflow.keras.models import load_model
from tensorflow import Graph
import os
import joblib
# import h5py
import json
from keras.models import model_from_json
from PIL import Image 
import numpy as np


def index(request):
	labels = ['rickshaw', 'easybike', 'cng']
	if request.method == "POST":
		form = IndexForm(request.POST, request.FILES)
		if form.is_valid():
			image = form.cleaned_data["image"]
			post = Index(image=image)
			post.save()
			

	else:
		form = IndexForm()
	context = {"form": form}
	image_url = Index.objects.last()
	image_file = os.path.join("media", f"{image_url.image}")
	print(image_file)
	img_array = cv2.imread(image_file, cv2.IMREAD_COLOR)
	new_array = cv2.resize(img_array, (50, 50))
	new_array = new_array.reshape(-1, 50, 50, 3)
	model = tf.keras.models.load_model("./models/c.h5")
	prediction = model.predict_classes([new_array])
	pred_label = labels[(prediction[0])]	
	context["something"] = pred_label
	last_image = Index.objects.last()
	context["up"] = last_image
	return render(request, "index.html", context)

