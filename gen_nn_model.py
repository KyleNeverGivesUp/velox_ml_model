import torch
import torch.nn as nn
import h5py

if "__main__" == __name__:

    # define model
    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.fc1 = nn.Linear(100, 64)
            self.fc2 = nn.Linear(64, 16)
            self.fc3 = nn.Linear(16, 2)
            self.fc4 = nn.Linear(16, 1)

        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = torch.relu(self.fc2(x))
            x = torch.relu(self.fc(x))
            x = torch.softmax(self.fc3(x), dim=1)
            return x

    model = Net()

    # export .h5 file
    with h5py.File("nn-test-model.h5", "w") as f:
        for name, param in model.named_parameters():
            print(name, param)
            f.create_dataset(name, data=param.detach().numpy())

    print("                job_any_64.h5 saved successfully.")