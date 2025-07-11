🧠 SWEET PUMPKIN LEAF DISEASE DETECTION APPROACH 
WITH DEEP LEARNING ALGORITHM 🍃🎃
This project presents a deep learning-based solution to automatically detect and classify sweet pumpkin leaf diseases using Convolutional Neural Networks (CNNs). It is designed to assist farmers and agricultural experts in early diagnosis, allowing timely and effective disease management, improving crop yield, and promoting sustainable farming practices.

📌 Project Overview
Sweet pumpkin (Cucurbita moschata) is a vital crop in Bangladesh, widely grown for its nutritional value and economic importance. However, several leaf diseases pose serious threats to its productivity and quality. These include:

🍂 Downy Mildew

🍃 Leaf Curl

🌀 Mosaic Disease

🐞 Red Beetle Infestation

🌿 Fresh Healthy Leaves (used as control)

The project introduces a CNN-powered classification system trained on 5,000+ real-time field images collected from Munshiganj, Bangladesh. The dataset is evenly divided into 5 categories (1,000 images per class).

🔍 Among the five pre-trained CNN models used — MobileNet, DenseNet121, VGG16, VGG19, and InceptionV3 — MobileNet showed the best performance with a 91% accuracy, making it ideal for mobile and low-resource deployment.

🧪 Technologies Used
🐍 Python 3.9+

⚙️ TensorFlow & Keras

💻 Google Colab (for GPU training)

🖼️ OpenCV (image preprocessing)

📊 NumPy, Pandas, Matplotlib

🧑‍💻 Streamlit (for user-friendly web deployment)

🧬 Model Architecture Highlights
✅ Applied Transfer Learning with 5 CNN models:
– MobileNet, DenseNet121, VGG16, VGG19, InceptionV3
✅ Fine-tuned top layers and applied Dropout Regularization
✅ Used Data Augmentation for better generalization
✅ Evaluation metrics: Accuracy, F1-score, Confusion Matrix
✅ MobileNet achieved 91% accuracy and 0.91 F1-score

🌍 Societal & Environmental Impact
🚜 Empowers Farmers: Enables early and accurate detection
🌱 Sustainable Agriculture: Reduces excessive pesticide use
📉 Cost-Effective: Eliminates the need for manual disease inspection
📡 Smart Farming Ready: Streamlit app can be scaled to drones or IoT
💚 Supports SDGs: Aligns with SDG 2 (Zero Hunger), SDG 12 (Responsible Consumption), SDG 13 (Climate Action)

🚀 Future Scope & Research Directions
Here are the potential extensions for future contributors and researchers:

📱 Mobile App Deployment
Create an Android/iOS app for field use with offline capabilities using TensorFlow Lite.

🌐 Multilingual Interface
Add support for Bangla and other local languages for better farmer usability.

🧠 Explainable AI Integration
Implement Grad-CAM to visually explain predictions and build trust.

🌾 Multi-Crop Support
Expand the pipeline to detect diseases in other crops like maize, potato, or rice.

🌦️ IoT & Sensor Fusion
Integrate temperature/humidity sensors to correlate disease outbreaks with environmental data.

🛰️ Drone-Based Monitoring
Use aerial imagery to detect large-scale outbreaks across fields.

🧬 Ensemble Learning
Combine multiple models (e.g., MobileNet + DenseNet) to improve accuracy further.

🌍 Global Dataset Expansion
Curate a larger, more diverse dataset from multiple climates and regions.

👨‍💻 Contributions
We welcome your contributions! 🚀
You can:

📤 Fork and submit pull requests

🔧 Improve model performance

📦 Package the app for mobile/web

🧪 Add new evaluation metrics or crops

📚 Citation
If you use this project in your work or research, please cite:

Md. Amir Khasru, "SWEET PUMPKIN LEAF DISEASE DETECTION APPROACH 
WITH DEEP LEARNING ALGORITHM", Daffodil International University, 2025.

