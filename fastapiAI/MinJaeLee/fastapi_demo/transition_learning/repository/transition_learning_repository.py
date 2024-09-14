from abc import ABC, abstractmethod


class TransitionLearningRepository(ABC):
    @abstractmethod
    def prepareBertBasedUncasedLearningSet(self):
        pass

    @abstractmethod
    def prepareBertBaseMultilingualUncasedSentimentLearningSet(self):
        pass

    @abstractmethod
    def prepareGPT2PretrainedLearningSet(self):
        pass