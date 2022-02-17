import Unsupervised.DataVisualisation as DataVisualisation
import Models.LearningModels as LearningModels
import Supervised.ModelTraining as ModelTraining
import Supervised.Regression as Regression
import Supervised.Regret as Regret
import Utils.FileHandling as FileHandling
import Utils.Preprocessing as Preprocessing
from sklearn.manifold import TSNE


def runDataVisualisation():
    inputFeatures, gameNames = FileHandling.getUnlabelledData('res/Input/rulesetLudemes.csv')
    featureSelector = TSNE(n_components=2, metric="euclidean", init='pca', random_state=0, learning_rate=200.0, perplexity=30.0)
    inputFeatures = Preprocessing.getPreprocessedInputData(inputFeatures, featureSelector)
    DataVisualisation.plotDataCategories(inputFeatures, gameNames, 'res/Output/ClusterResults.csv')


def runSupervisedLearningRegression():
    inputFeatures, inputLabels, gameNames = FileHandling.GetLabelledData('res/Input/rulesetLudemes.csv', 'res/Input/rulesetHeuristics.csv')
    inputFeatures = Preprocessing.getPreprocessedInputData(inputFeatures, None)
    Regret.calculateCrossValidationRegretRegression(inputFeatures, inputLabels, LearningModels.regressionModels)
    trainedModels = ModelTraining.trainModels(inputFeatures, inputLabels, LearningModels.regressionModels)
    regressionPredictedValues = ModelTraining.getModelPredictions(trainedModels, inputFeatures)
    Regression.outputRegressionPredictions(regressionPredictedValues, gameNames, trainedModels, inputLabels.columns)


runDataVisualisation()
runSupervisedLearningRegression()