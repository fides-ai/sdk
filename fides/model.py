import datetime
from fides.explainers.lime import LimeExplainer


class Model(object):

    def __init__(self, guid):
        self.guid = guid

    def bind(self,
             predict_fn,
             training_data,
             mode="classification",
             training_labels=None,
             feature_names=None,
             categorical_features=None,
             categorical_names=None,
             kernel_width=None,
             kernel=None,
             verbose=False,
             class_names=None,
             feature_selection='auto',
             discretize_continuous=True,
             discretizer='quartile',
             sample_around_instance=False,
             random_state=None):
        self.predict_fn = predict_fn
        self.explainer = self.explainer(training_data,
                                        mode,
                                        training_labels,
                                        feature_names,
                                        categorical_features,
                                        categorical_names,
                                        kernel_width,
                                        kernel,
                                        verbose,
                                        class_names,
                                        feature_selection,
                                        discretize_continuous,
                                        discretizer,
                                        sample_around_instance,
                                        random_state)

    def explainer(self,
                  training_data,
                  mode="classification",
                  training_labels=None,
                  feature_names=None,
                  categorical_features=None,
                  categorical_names=None,
                  kernel_width=None,
                  kernel=None,
                  verbose=False,
                  class_names=None,
                  feature_selection='auto',
                  discretize_continuous=True,
                  discretizer='quartile',
                  sample_around_instance=False,
                  random_state=None):
        """Generate an explainer for a model function.
        """
        self.explainer = LimeExplainer(**locals())

    def explain(self,
                data_row,
                labels=(1,),
                top_labels=None,
                num_features=10,
                num_samples=5000,
                distance_metric='euclidean',
                model_regressor=None):
        """
        Generates explanations for a prediction.
        :param data_row:
        :param predict_fn:
        :param labels:
        :param top_labels:
        :param num_features:
        :param num_samples:
        :param distance_metric:
        :param model_regressor:
        :return:
        """
        args = {**{'predict_fn': self.predict_fn}, **locals()}
        return self.explainer.explain(**args)

    def track_prediction(self,
                         x,
                         y,
                         explain=True):
        data = {
            'x': x,
            'y': y,
        }

        if explain and self.explainer:
            data['explain'] = self.explain(x)
            data['explainedAt'] = datetime.datetime.now()

        return data
