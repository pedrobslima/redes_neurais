import torch
from keras4torch.metrics import Metric
from sklearn import metrics as sklearn_metrics

class SklearnMetric(Metric):
    def __init__(self, activation=None) -> None:
        super(SklearnMetric, self).__init__()
        self.activation = activation

        self.score_fn = self.get_score_fn(sklearn_metrics)

    def __call__(self, y_pred, y_true):
        if self.activation is not None:
            y_pred = self.activation(y_pred)
        y_true = y_true.cpu().numpy()
        y_pred = y_pred.cpu().numpy()
        print(y_true)
        print(y_pred)
        return torch.tensor(self.score_fn(y_true, y_pred), dtype=torch.float32, device='cpu')

    def get_score_fn(self, sklearn_metrics):
        raise NotImplementedError()

class F1_Score(SklearnMetric):
    def __init__(self, activation=torch.sigmoid) -> None:
        super(F1_Score, self).__init__(activation=lambda x: torch.round(activation(x)))

    def get_score_fn(self, sklearn_metrics):
        return sklearn_metrics.f1_score

    def get_abbr(self) -> str:
        return 'f1'
    

class MyMetric(Metric):
    def __init__(self, activation=torch.sigmoid) -> None:
        super(F1_Score, self).__init__(activation=lambda x: torch.round(activation(x)))

    def __call__(self, y_pred, y_true):
        if self.activation is not None:
            y_pred = self.activation(y_pred)
        y_true = y_true.cpu().numpy()
        y_pred = y_pred.cpu().numpy()
        return torch.tensor(sklearn_metrics.f1_score(y_true, y_pred), dtype=torch.float32, device='cpu')