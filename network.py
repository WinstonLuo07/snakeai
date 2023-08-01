import pygame as pyg
import numpy
import random
import copy
import math

class Layer:
    
    
    def __init__(self, inputN, outputN):
        self.inputNodes = inputN
        self.outputNodes = outputN

        
        self.weights = numpy.zeros((self.inputNodes, self.outputNodes))
        self.biases = numpy.zeros((self.outputNodes))
        self.randomizeWeightsAndBiases(-10, 10)
        
    def __str__(self):
        out = '[' + str(self.inputNodes) + ',' + str(self.outputNodes) + ']'
        return out
    
    def randomizeWeightsAndBiases(self, minv, maxv):
        for weight in self.weights:
            for weighti in range(0, len(weight)):
                weight[weighti] = random.uniform(minv, maxv)
        for bias in range(0, len(self.biases)):
            weight[bias] = random.uniform(minv, maxv)
    
    def activationFunction(self, weightedInput):
        # return 1 / (1 + math.exp(-weightedInput))
        return max(0, weightedInput)

    
    def calculateOutputs(self, inputs):
        activationValues = numpy.zeros(self.outputNodes)
        
        for nodeOut in range(0, self.outputNodes):
            weightedInput = self.biases[nodeOut]
            for nodeIn in range(0, self.inputNodes):
                # print("s" + str(self.inputNodes))
                # print(len(inputs))
                weightedInput += inputs[nodeIn] * self.weights[nodeIn][nodeOut]
            activationValues[nodeOut] = self.activationFunction(weightedInput)
        return activationValues
    def mutate(self, mrange):
        for weight in self.weights:
            for weighti in range(0, len(weight)):
                weight[weighti] += random.uniform(-mrange, mrange)
        for bias in range(0, len(self.biases)):
            weight[bias] += random.uniform(-mrange, mrange)

class NeuralNet:
    
    def __init__(self, hlayers = (4, 2, 2, 4)):
        self.layers = []
        for layer in range(0, len(hlayers)-1):
            self.layers.append(Layer(hlayers[layer], hlayers[layer+1]))
        
    def __str__(self):
        out = "["
        for layer in self.layers:
            out = out + str(layer) + ", "
            
        return out + ']'
    
    def calculateOutputs(self, inputs):
        for layer in self.layers:
            inputs = layer.calculateOutputs(inputs)
        return inputs
    
    def makeDecision(self, inputs):
        outputs = self.calculateOutputs(inputs)
        max = 0
        for i in range(0, len(outputs)):
            if outputs[i] > outputs[max]:
                max = i
        return max
    def mutateBest(self, mrate):
        for layer in self.layers:
            layer.mutate(mrate)
            
    def createOffSpring(self, mrange, mchance):
        offSpring = copy.deepcopy(self)
        if (random.random() < mchance):
            offSpring.mutateBest(mrange)
        return offSpring