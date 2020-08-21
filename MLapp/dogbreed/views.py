from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import pandas as pd

import torch
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn

from PIL import Image as img

import copy

from .forms import ImageForm
from .models import Image
from .constant import breeds


def predict_dog_breed(request):
    """
    function to get uploaded image from form, preprocess it, predict dog breed, and finally give prediction to user 
    """

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            myimage = Image(image=request.FILES["image"])
            form.save()

            image_name = myimage.image
            image_name_original = copy.copy(image_name) 
            image = img.open(image_name).convert("RGB")

            preprocess = transforms.Compose(
                [
                    transforms.Resize(size=(255)),
                    transforms.CenterCrop((224, 244)),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ]
            )

            model = models.vgg16(pretrained=True)
            model.classifier[6] = nn.Linear(4096, 133)
            model.load_state_dict(torch.load("trained_VGG16Net.pt", map_location=torch.device("cpu")))
            model.eval()

            with torch.no_grad():
                outputs = model(preprocess(image).unsqueeze_(0))

                pred = torch.argmax(outputs).item()

            output = breeds[pred]
            myimage.save()

            return render(
                request,
                "app/result.html",
                {"image_name": image_name, "image_name_original": image_name_original, "output": output},
            )

    else:
        form = ImageForm()
    return render(request, "app/breed_prediction.html", {"form": form})


