import torchvision.models as models

from ptsemseg.models.fcn import *
from ptsemseg.models.fcn_with_maskedconv import *
from ptsemseg.models.fcn_with_maskedconv2 import *
from ptsemseg.models.fcn_with_maskedconv3 import *
from ptsemseg.models.segnet import *
from ptsemseg.models.unet import *
from ptsemseg.models.pspnet import *
from ptsemseg.models.linknet import *
from ptsemseg.models.frrn import *


def get_model(name, n_classes):
    model = _get_model_instance(name)

    if name in ['frrnA', 'frrnB']:
        model = model(n_classes, model_type=name[-1])

    elif name in ['fcn32s', 'fcn16s', 'fcn8s']:
        model = model(n_classes=n_classes)
        vgg16 = models.vgg16(pretrained=True)
        model.init_vgg16_params(vgg16)

    elif name in ['fcn_with_maskedconv', 'fcn_with_maskedconv2', 'fcn_with_maskedconv3']:
        model = model(n_classes=n_classes)
        vgg16 = models.vgg16(pretrained=True)
        model.init_vgg16_params(vgg16)

    elif name == 'segnet':
        model = model(n_classes=n_classes,
                      is_unpooling=True)
        vgg16 = models.vgg16(pretrained=True)
        model.init_vgg16_params(vgg16)

    elif name == 'unet':
        model = model(n_classes=n_classes,
                      is_batchnorm=True,
                      in_channels=3,
                      is_deconv=True)
    
    else:
        model = model(n_classes=n_classes)

    return model

def _get_model_instance(name):
    try:
        return {
            'fcn32s': fcn32s,
            'fcn8s': fcn8s,
            'fcn16s': fcn16s,
            'fcn_with_maskedconv' : fcn_with_maskedconv,
            'fcn_with_maskedconv2': fcn_with_maskedconv2,
            'fcn_with_maskedconv3': fcn_with_maskedconv3,
            'unet': unet,
            'segnet': segnet,
            'pspnet': pspnet,
            'linknet': linknet,
            'frrnA': frrn,
            'frrnB': frrn,
        }[name]
    except:
        print('Model {} not available'.format(name))
