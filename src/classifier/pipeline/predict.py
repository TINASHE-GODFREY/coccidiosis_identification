import numpy as np
import os
import tensorflow as tf


class PredictionPipeline:
    def __init__(self, filename):
        self.filename=filename

    def predict(self):
        model= tf.keras.load_model(os.path.join("artifacts", "training", "model.keras"))

        imagename= self.filename
        test_image= tf.keras.image.load_img(imagename, target_size= (224,224))
        test_image= tf.keras.image.img_to_array(test_image)
        test_image= np.expand_dims(test_image,axis=0)
        results= np.argmax(model.predict(test_image), axis=1)
        print(results)

        if results[0]==1:
            prediction="Healty"
            return[{"image":prediction}]
        else:
            prediction= "Coccidiosis"
            return[{"image": prediction}]
