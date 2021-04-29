import torch.nn as nn


class CNNModel(nn.Module):
    def __init__(self, pic_size: tuple[int]):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(
                in_channels=16,
                out_channels=33,
                kernel_size=(3,),
                stride=(2,)
            ),
            nn.MaxPool2d(
                kernel_size=2,
                stride=2
            ),
            # nn.Conv2d(
            #
            # )
        )