

class Explainer(object):

    def __init__(self, **args):
        """
        """
        self.explainer = lime.lime_tabular.LimeTabularExplainer(**args)

    def explain(self, **args):
        """
        """
        exp = self.explainer.explain_instance(**args)
        return exp.as_list()

    