"""
   plot real-time loss-acc curve, ROC curve and PR curve
"""


import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc



def plotROC(test,score):
    fpr,tpr,threshold = roc_curve(test, score)
    auc_roc = auc(fpr,tpr)
    plt.figure()
    lw = 3
    plt.figure(figsize=(10,10))
    plt.plot(fpr, tpr, color='darkorange',lw=lw, label='ROC curve (area = %f)' %auc_roc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.tick_params(labelsize=18)
    font = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }
    plt.xlabel('False Positive Rate',font)
    plt.ylabel('True Positive Rate',font)
    plt.title('Receiver operating characteristic curve',font)
    plt.legend(loc="lower right")
    plt.savefig('./figure/ROC.png')

def plotPR(test,score):
    precision, recall, thresholds = precision_recall_curve(test, score)
    pr_auc = auc(recall,precision)
    plt.figure()
    lw = 3
    plt.figure(figsize=(10,10))
    plt.plot(precision, recall, color='darkred',lw=lw, label='P-R curve (area = %f)' %pr_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.tick_params(labelsize=18)
    font = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }
    plt.xlabel('Recall',font)
    plt.ylabel('Precision',font)
    plt.legend(loc="lower right")
    plt.title('Precision recall curve',font)
    plt.savefig('./figure/PR.png')
    
    
