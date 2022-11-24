from typing import Dict

from classes.core.Model import Model
from classes.modules.transformer.Transformer import Transformer


class ModelTransformer(Model):

    def __init__(self, network_params: Dict):
        super().__init__(device=network_params["device"])
        self._network = Transformer(network_params).to(self._device)