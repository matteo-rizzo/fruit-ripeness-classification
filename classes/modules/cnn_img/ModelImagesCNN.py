from typing import Dict

from classes.core.Model import Model
from classes.modules.cnn_img.ImagesCNN import ImagesCNN


class ModelImagesCNN(Model):

    def __init__(self, network_params: Dict):
        super().__init__(device=network_params["device"])
        self._network = ImagesCNN(network_params).to(self._device)