from Entrainement import train
from Augmentation import augmentation
import pandas as pd 

#Fonction Augmentation 
data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 20, 19, 18]}  
df = pd.DataFrame(data)  

#Bonne utilisation 
df_aug = augmentation(df, "Age")

#Erreur
df_aug = augmentation(df, 2)
df_aug = augmentation(2, "Age")
df_aug = augmentation(df, "Ag")


# #Fonction Entrainement 
# model = nn.Sequential()
# model.add(nn.Dense(64, activation='relu'))
# model.add(nn.Dense(32, activation='relu'))
# model.add(nn.Dense(3))
# model.initialize()

# X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.25, random_state=42)
# data_set = mx.gluon.data.dataset.ArrayDataset(X, y)
# data_loader = mx.gluon.data.DataLoader(data_set, batch_size=8, shuffle=shuffle)

# #Bonne utilisation 
# train(model, data_loader,5,8)

# #Erreur 
# train(1, data_loader,5,8)
# train(model, 1,5,8)
# train(model, data_loader,"2",8)
# train(model, data_loader,5,"8")


