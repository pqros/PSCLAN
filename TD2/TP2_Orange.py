
import numpy as np;
import sklearn;
from sklearn import svm ;
from sklearn.model_selection import train_test_split;
from sklearn.metrics import accuracy_score;
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

##1 supprimer les lignes contenant au moins une valeur Inf/NaN

# vecteur_test = np.array([[2,3,23,12,32],[1,'Inf',3,12344,'NaN']]) 
# test_2=np.array([['1','3','5.64'],['4.5','0.0','7']])
# test_3=np.array([1,2,3.0,4.3])
# a=[[True, False],[False, True]]
# 
# def f():
#     test_4 = []
#     for i in range(0,2):
#         row=[]
#         for j in range(0,3):
#             row.append(float(test_2[i,j]))
#         test_4.append(row)
#     test_4 = np.array(test_4)
#     return test_4
    


def suppressionInf(X_data, Y_data):
    print('X_data de base est :')
    print(X_data)
    test_infini = np.all(np.isfinite(X_data))
    print(test_infini)
    if (test_infini):
        return (X_data,Y_data)
    else :
        liste2 = np.argwhere(np.invert(np.isfinite(X_data)))
        liste2= liste2[:,0]
        print(liste2)
        newX_data = []
        newY_data = []
        for i in range(0,len(X_data)):
            newX_row=[]
            if (i not in liste2) :
                for j in range(0,len(X_data[0])) :
                    newX_row.append(X_data[i,j])
                newX_data.append(newX_row)
                newY_data.append(Y_data[i])
        return (np.array(newX_data),np.array(newY_data))
    
    ##2 Supprimer les colonnes sans valeurs numériques (hormis le label)
    

#distinguer si une valeur est un float ou pas 

def check_string_to_float(s):
        try:
            float(s)
            return True
        except:
            return False

    
def colonnesZ(dataarray):                             #garder les colonnes aux valeurs numériques ou LABEL
    titres_colonnes = dataarray[0]
    valeurs = dataarray[1]
    new_data = []
    list_keep = []
    for ind in range(0, len(valeurs)) :
        if (check_string_to_float(valeurs[ind])==True or titres_colonnes[ind] in [' Label', 'Label']):
            list_keep.append(ind)
    for i in range(0,len(dataarray)):
        new_row=[]
        for j in range (0,len(dataarray[0])):
            if (j in list_keep) :
                new_row.append(dataarray[i,j])
        new_data.append(new_row)
    return np.array(new_data)

def divisionXY(Z):                                   #diviser en couple [X,Y]
    print("Z est :")
    print(Z)
    X=Z[1:, 0:len(Z[0])-1]
    Y=Z[1:, len(Z[0])-1:len(Z[0])]
    return (X,Y)

def conversionX(X):                                   #transformer X en array de type float
    new_X = []
    for i in range(0,len(X)) :
        row=[]
        for j in range(0,len(X[0])) :
            row.append(float(X[i,j]))
        new_X.append(row)
    new_X=np.array(new_X)
    return new_X

## 3 Diviser en set de train/ de test et entrainer le modèle


def trainingSVM(Xdata, Ydata):
    clf = svm.SVC(gamma=10)
    X_train, X_test, Y_train, Y_test = train_test_split( Xdata, Ydata, test_size=0.3, shuffle = True)
    clf.fit(X_train,Y_train)
    return(X_train, X_test, Y_train, Y_test, clf)

def trainingRandomForest(Xdata, Ydata):
    clf = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0)
    X_train, X_test, Y_train, Y_test = train_test_split( Xdata, Ydata, test_size=0.3, shuffle = True)
    clf.fit(X_train,Y_train)
    return(X_train, X_test, Y_train, Y_test, clf)

def trainingDecisionTree(Xdata,Ydata):
    clf = DecisionTreeClassifier(random_state=0)
    X_train, X_test, Y_train, Y_test = train_test_split( Xdata, Ydata, test_size=0.3, shuffle = True)
    clf.fit(X_train,Y_train)
    return(X_train, X_test, Y_train, Y_test, clf)
    
def testing(X_topredict):
    Y_trainpred = clf.predict(X_topredict)
    return Y_trainpred

def accuracy(Y_true , Y_predicted):
    return accuracy_score(Y_true, Y_predicted)


##4 Essai final sur un extrait d'un dataset


#compilationnp issue du TD1 

def compilationnp(cheminacces) : 
    with open(cheminacces , newline = '') as csvfile :
        reader = csv.reader(csvfile, delimiter = ',')
        res = []
        for row in reader :
            line = []
            for column in row :
                line.append(column);
            res.append(line)
        return (np.array(res))
        
        
        

data_array = compilationnp('C:\\Users\wyann\Documents\PSC\Datasets\CIC-IDS-2017\MachineLearningCVE\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv')
print(data_array)
Z=colonnesZ(data_array)
X_data, Y_data = divisionXY(Z)
X_data = conversionX(X_data)
X_data,Y_data = suppressionInf(X_data,Y_data)
Y_data = Y_data.reshape(len(Y_data))

# 
# #X_data a t'il des valeurs interdites ?
# 
# # print(X_data)
# print(np.all(np.isfinite(X_data)))
# print(np.any(np.isnan(X_data)))
# # print(np.argwhere(np.isnan(X_data)))  
# # print(np.argwhere(np.invert(np.isfinite(X_data))))



#décommenter la ligne qu'on souhaite pour appliquer la méthode choisie : SVM, Random Forest ou Decision Tree


# X_train, X_test, Y_train, Y_test, clf = trainingSVM(X_data, Y_data)
# # X_train, X_test, Y_train, Y_test, clf = trainingRandomForest(X_data, Y_data)
# # # X_train, X_test, Y_train, Y_test, clf = trainingDecisionTree(X_data, Y_data)


Y_trainpred = testing(X_train)
Y_testpred = testing(X_test)
print("La précision sur le set train est de " )
print( accuracy(Y_train, Y_trainpred))
print("La précision sur le set test est de ")
print(accuracy(Y_test, Y_testpred))
