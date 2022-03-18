from __future__ import print_function
import numpy as np
import argparse
import os
from file_reader import readFasta
from DNAFeature import *
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,recall_score,precision_score,confusion_matrix,matthews_corrcoef 
from deepforest import CascadeForestClassifier
from analysisPlot import *

parser = argparse.ArgumentParser(description='path')
parser.add_argument('--species',type=str,default = None)
args = parser.parse_args()

path = args.species


result = []
feature = []
feature_id = np.loadtxt('./data/{}/id1500.txt'.format(path),dtype=int,delimiter=',')
for i in range(0,10):
     round = 'Round{num}'.format(num=i)
     print(round)
     print('Loading data.......................................')
     positive_trainfile = './data/{}/positive.txt_scale1_fold{}_train'.format(path,i)
     positive_testfile = './data/{}/positive.txt_scale1_fold{}_test'.format(path,i)
     negative_trainfile = './data/{}/negative.txt_scale1_fold{}_train'.format(path,i)
     negative_testfile = './data/{}/negative.txt_scale1_fold{}_test'.format(path,i)
     (posTrainSeq,posTrainSeqid) = readFasta(positive_trainfile,41)
     (negTrainSeq,negTrainSeqid) = readFasta(negative_trainfile,41)
     (posTestSeq,posTestSeqid) = readFasta(positive_testfile,41)
     (negTestSeq,negTestSeqid) = readFasta(negative_testfile,41)
     print('Generating labels and features..................................')
     posTrainlabel = np.ones((len(posTrainSeq),1))
     negTrainlabel = np.zeros((len(negTrainSeq),1))
     posTestlabel = np.ones((len(posTestSeq),1))
     negTestlabel = np.zeros((len(negTestSeq),1))
     pos_train_1 = PDMNOnehot(posTrainSeq)
     neg_train_1 = PDMNOnehot(negTrainSeq)
     pos_test_1  = PDMNOnehot(posTestSeq)
     neg_test_1  = PDMNOnehot(negTestSeq)
     pos_train_2 = PDDNOnehot(posTrainSeq)
     neg_train_2 = PDDNOnehot(negTrainSeq)
     pos_test_2  = PDDNOnehot(posTestSeq)
     neg_test_2  = PDDNOnehot(negTestSeq)
     pos_train_3 = DNAComposition(posTrainSeq,1)
     neg_train_3 = DNAComposition(negTrainSeq,1)
     pos_test_3  = DNAComposition(posTestSeq,1)
     neg_test_3  = DNAComposition(negTestSeq,1)
     pos_train_4 = DNAComposition(posTrainSeq,2)
     neg_train_4 = DNAComposition(negTrainSeq,2)
     pos_test_4  = DNAComposition(posTestSeq,2)
     neg_test_4  = DNAComposition(negTestSeq,2)
     pos_train_5 = DNAComposition(posTrainSeq,3)
     neg_train_5 = DNAComposition(negTrainSeq,3)
     pos_test_5  = DNAComposition(posTestSeq,3)
     neg_test_5  = DNAComposition(negTestSeq,3)
     pos_train_6 = DNAComposition(posTrainSeq,4)
     neg_train_6 = DNAComposition(negTrainSeq,4)
     pos_test_6  = DNAComposition(posTestSeq,4)
     neg_test_6  = DNAComposition(negTestSeq,4)
     pos_train_7 = DNAComposition(posTrainSeq,5)
     neg_train_7 = DNAComposition(negTrainSeq,5)
     pos_test_7  = DNAComposition(posTestSeq,5)
     neg_test_7  = DNAComposition(negTestSeq,5)
     pos_train_8 = DNAshape(posTrainSeq,MGW)
     neg_train_8 = DNAshape(negTrainSeq,MGW)
     pos_test_8  = DNAshape(posTestSeq,MGW)
     neg_test_8  = DNAshape(negTestSeq,MGW)
     pos_train_9 = DNAshape(posTrainSeq,ProT)
     neg_train_9 = DNAshape(negTrainSeq,ProT)
     pos_test_9  = DNAshape(posTestSeq,ProT)
     neg_test_9  = DNAshape(negTestSeq,ProT)
     pos_train_10 = DNAshape(posTrainSeq,Roll1)
     neg_train_10 = DNAshape(negTrainSeq,Roll1)
     pos_test_10  = DNAshape(posTestSeq,Roll1)
     neg_test_10  = DNAshape(negTestSeq,Roll1)
     pos_train_11 = DNAshape(posTrainSeq,HelT1)
     neg_train_11 = DNAshape(negTrainSeq,HelT1)
     pos_test_11  = DNAshape(posTestSeq,HelT1)
     neg_test_11  = DNAshape(negTestSeq,HelT1)
     pos_train_12 = RFHC(posTrainSeq)
     neg_train_12 = RFHC(negTrainSeq)
     pos_test_12  = RFHC(posTestSeq)
     neg_test_12  = RFHC(negTestSeq)
     pos_train_13 = TNPCP(posTrainSeq,Nucleosome_positioning,5)
     neg_train_13 = TNPCP(negTrainSeq,Nucleosome_positioning,5)
     pos_test_13  = TNPCP(posTestSeq,Nucleosome_positioning,5)
     neg_test_13  = TNPCP(negTestSeq,Nucleosome_positioning,5)
     pos_train_14 = TNPCP(posTrainSeq,Dnase_I,5)
     neg_train_14 = TNPCP(negTrainSeq,Dnase_I,5)
     pos_test_14  = TNPCP(posTestSeq,Dnase_I,5)
     neg_test_14  = TNPCP(negTestSeq,Dnase_I,5)
     pos_train_15 = TNPCP(posTrainSeq,MW_kg,5)
     neg_train_15 = TNPCP(negTrainSeq,MW_kg,5)
     pos_test_15  = TNPCP(posTestSeq,MW_kg,5)
     neg_test_15  = TNPCP(negTestSeq,MW_kg,5)
     pos_train_16 = TNPCP(posTrainSeq,Dnase_I_Rigid,5)
     neg_train_16 = TNPCP(negTrainSeq,Dnase_I_Rigid,5)
     pos_test_16  = TNPCP(posTestSeq,Dnase_I_Rigid,5)
     neg_test_16  = TNPCP(negTestSeq,Dnase_I_Rigid,5)
     pos_train_17 = TNPCP(posTrainSeq,MW_Daltons,5)
     neg_train_17 = TNPCP(negTrainSeq,MW_Daltons,5)
     pos_test_17  = TNPCP(posTestSeq,MW_Daltons,5)
     neg_test_17  = TNPCP(negTestSeq,MW_Daltons,5)
     pos_train_18 = TNPCP(posTrainSeq,Nucleosome,5)
     neg_train_18 = TNPCP(negTrainSeq,Nucleosome,5)
     pos_test_18  = TNPCP(posTestSeq,Nucleosome,5)
     neg_test_18  = TNPCP(negTestSeq,Nucleosome,5)
     pos_train_19 = TNPCP(posTrainSeq,Nucleosome_Rigid,5)
     neg_train_19 = TNPCP(negTrainSeq,Nucleosome_Rigid,5)
     pos_test_19  = TNPCP(posTestSeq,Nucleosome_Rigid,5)
     neg_test_19  = TNPCP(negTestSeq,Nucleosome_Rigid,5)
     pos_train = np.hstack((pos_train_1,pos_train_2,pos_train_3,pos_train_4,pos_train_5,pos_train_6,pos_train_7,pos_train_8,pos_train_9,pos_train_10,pos_train_11,pos_train_12,pos_train_13,pos_train_14,pos_train_15,pos_train_16,pos_train_17,pos_train_18,pos_train_19))
     neg_train = np.hstack((neg_train_1,neg_train_2,neg_train_3,neg_train_4,neg_train_5,neg_train_6,neg_train_7,neg_train_8,neg_train_9,neg_train_10,neg_train_11,neg_train_12,neg_train_13,neg_train_14,neg_train_15,neg_train_16,neg_train_17,neg_train_18,neg_train_19))
     pos_test =  np.hstack((pos_test_1,pos_test_2,pos_test_3,pos_test_4,pos_test_5,pos_test_6,pos_test_7,pos_test_8,pos_test_9,pos_test_10,pos_test_11,pos_test_12,pos_test_13,pos_test_14,pos_test_15,pos_test_16,pos_test_17,pos_test_18,pos_test_19))
     neg_test =  np.hstack((neg_test_1,neg_test_2,neg_test_3,neg_test_4,neg_test_5,neg_test_6,neg_test_7,neg_test_8,neg_test_9,neg_test_10,neg_test_11,neg_test_12,neg_test_13,neg_test_14,neg_test_15,neg_test_16,neg_test_17,neg_test_18,neg_test_19))
     y_train = np.concatenate((posTrainlabel,negTrainlabel),axis=0).flatten()
     x_train = np.vstack((pos_train,neg_train))
     y_test = np.concatenate((posTestlabel,negTestlabel),axis=0).flatten()
     x_test = np.vstack((pos_test,neg_test))
     x_train_select = x_train[:,feature_id]
     x_test_select = x_test[:,feature_id]
     print('Shuffling the data............................................')
     index = np.arange(len(y_train))
     np.random.shuffle(index)
     x_train_select = x_train_select[index,:]
     y_train = y_train[index]
     print('Training model..............................................')
     model = CascadeForestClassifier(random_state=1,use_predictor=1,predictor='lightgbm',backend='sklearn',n_trees=300, n_estimators=8)
     model.fit(x_train_select, y_train)
     print('Predicting..............................................')
     predicted_Probability = model.predict_proba(x_test_select)
     prediction = model.predict(x_test_select)
     y_test = np.array(y_test).reshape(y_test.shape[0],1)
     predicted_Probability = np.array(predicted_Probability).reshape(len(predicted_Probability),2)
     prediction = np.array(prediction).reshape(prediction.shape[0],1)
     combine = np.hstack((y_test,predicted_Probability,prediction))
     for num in combine:
           result.append(num)
     
print('Summarizing the result............................................')
result = np.array(result).reshape(len(result),4)
print('Showing the confusion matrix')
cm=confusion_matrix(result[:,0],result[:,3])
print(cm)
print("ACC: %f "%accuracy_score(result[:,0],result[:,3]))
print("Recall: %f "%recall_score(result[:,0],result[:,3]))
print("Pre: %f "%precision_score(result[:,0],result[:,3]))
print("F1: %f "%f1_score(result[:,0],result[:,3]))
print("MCC: %f "%matthews_corrcoef(result[:,0],result[:,3]))
print('Plotting the ROC curve...')
plotROC(result[:,0],result[:,2])
print('Plotting the P-R curve...')
plotPR(result[:,0],result[:,2])
np.savetxt('./figure/result.csv',result,fmt="%s",delimiter=",")



     

     
     