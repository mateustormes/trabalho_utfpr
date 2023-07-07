import os
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics, preprocessing
import matplotlib.pyplot as plt
from progress.bar import Bar
import time
from datetime import datetime
import random

def main():
    mainStartTime = time.time()
    trainPath = 'Rock-Paper-Scissors/train/'
    testPath = 'Rock-Paper-Scissors/test/'
    print(f'[INFO] ========= TRAINING PHASE ========= ')
    trainImages, trainLabels = getData(trainPath)
    trainLabels, trainEncoder = encodeLabels(trainLabels)
    trainFeatures = extractColorHistogramFeatures(trainImages)
    svm = trainRandomForest(trainFeatures, trainLabels)
    print(f'[INFO] =========== TEST PHASE =========== ')
    testImages, testLabels = getData(testPath)
    testLabels, testEncoder = encodeLabels(testLabels)
    testFeatures = extractColorHistogramFeatures(testImages)
    predictedLabels = predictRandomForest(svm, testFeatures)
    elapsedTime = round(time.time() - mainStartTime, 2)
    print(f'[INFO] Code execution time: {elapsedTime}s')
    plotConfusionMatrix(testEncoder, testLabels, predictedLabels)

    print(f'[INFO] =========== PREDICTION =========== ')
    
    # Habilitar a câmera
    camera = cv2.VideoCapture(0)
    
    frame_counter = 0
    predicted_class = ''
    
    while True:
        # Capturar frame da câmera
        ret, frame = camera.read()
        
        # Exibir o frame capturado
        cv2.imshow('Camera', frame)
        
        frame_counter += 1
        
        # Detectar pedra, papel ou tesoura a cada 5 segundos
        if frame_counter % 150 == 0:
            features = extractColorHistogramFeatures([frame])
            predicted_label = svm.predict(features)
            predicted_class = testEncoder.inverse_transform(predicted_label)[0]
            print(f'The predicted class for current frame is: {predicted_class}')
            
            # Comparação com a imagem reconhecida
            choices = ['rock', 'scissors', 'paper']
            random_choice = random.choice(choices)
            result = f'O valor sorteado para a máquina foi: {random_choice}'
            print(result)

            if random_choice == 'rock':
                if predicted_class == 'rock':
                    result = "Empate"
                elif predicted_class == 'scissors':
                    result = "Você Perdeu!"
                else:
                    result = "Você Ganhou!"
            elif random_choice == 'paper':
                if predicted_class == 'rock':
                    result = "Você Perdeu!"
                elif predicted_class == 'scissors':
                    result = "Você Ganhou!"
                else:
                    result = "Empate"
            else:  # random_choice == 'scissors'
                if predicted_class == 'rock':
                    result = "Você Ganhou!"
                elif predicted_class == 'scissors':
                    result = "Empate"
                else:
                   result = "Você Perdeu!"

            # Log do resultado
            print(f'Resultado: {result}')
        
        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberar os recursos da câmera
    camera.release()
    cv2.destroyAllWindows()


def getData(path):
    images = []
    labels = []
    if os.path.exists(path):
        fileList = os.listdir(path)
        bar = Bar('[INFO] Getting images and labels...', max=len(fileList),
                  suffix='%(index)d/%(max)d Duration:%(elapsed)ds')
        for fileName in fileList:
            label = os.path.basename(fileName).split('-')[0]
            if 'paper' in label:
                label = 'paper'
            elif 'scissor' in label:
                label = 'scissor'
            else:
                label = 'rock'
            labels.append(label)
            colorImage = cv2.imread(os.path.join(path, fileName))
            images.append(colorImage)
            bar.next()
        bar.finish()
    return images, labels


def extractColorHistogramFeatures(images):
    bar = Bar('[INFO] Extracting color histogram features...', max=len(images),
              suffix='%(index)d/%(max)d  Duration:%(elapsed)ds')
    featuresList = []
    for colorImage in images:
        # build a 3D histogram for RGB channels
        # reduce the number of bins to reduce the number of features
        bins = [20, 20, 20]
        hist = cv2.calcHist([colorImage], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
        cv2.normalize(hist, hist)
        featuresList.append(hist.flatten())
        bar.next()
    bar.finish()
    return np.array(featuresList, dtype=object)


def encodeLabels(labels):
    startTime = time.time()
    print(f'[INFO] Encoding labels to numerical labels')
    encoder = preprocessing.LabelEncoder()
    labels = encoder.fit_transform(labels)
    elapsedTime = round(time.time() - startTime, 2)
    print(f'[INFO] Encoding done in {elapsedTime}s')
    return labels, encoder


def trainRandomForest(trainData, trainLabels):
    print('[INFO] Training the Random Forest model...')
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    startTime = time.time()
    rf_model.fit(trainData, trainLabels)
    elapsedTime = round(time.time() - startTime, 2)
    print(f'[INFO] Training done in {elapsedTime}s')
    return rf_model


def predictRandomForest(rf_model, testData):
    print('[INFO] Predicting...')
    startTime = time.time()
    predictedLabels = rf_model.predict(testData)
    elapsedTime = round(time.time() - startTime, 2)
    print(f'[INFO] Predicting done in {elapsedTime}s')
    return predictedLabels


def getCurrentFileNameAndDateTime():
    fileName = os.path.basename(__file__).split('.')[0]
    dateTime = datetime.now().strftime('-%d%m%Y-%H%M')
    return fileName + dateTime


def plotConfusionMatrix(testEncoder, testLabels, predictedLabels):
    # Decoding test labels from numerical labels to string labels
    test = testEncoder.inverse_transform(testLabels)
    # Decoding predicted labels from numerical labels to string labels
    pred = testEncoder.inverse_transform(predictedLabels)
    print(f'[INFO] Plotting confusion matrix and accuracy...')
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.suptitle('Confusion Matrix: ' + getCurrentFileNameAndDateTime(), fontsize=18)
    metrics.ConfusionMatrixDisplay.from_predictions(test, pred, ax=ax, colorbar=False, cmap=plt.cm.Greens)
    accuracy = metrics.accuracy_score(testLabels, predictedLabels) * 100
    plt.title(f'Accuracy: {accuracy}%', fontsize=18, weight='bold')
    plt.savefig('./results/' + getCurrentFileNameAndDateTime(), dpi=300)
    print(f'[INFO] Plotting done!')
    print(f'[INFO] Close the figure window to end the program.')
    plt.show()



if __name__ == "__main__":
    main()