class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

disease_dict = {
    'Apple___Apple_scab': '''Apple Scab
    \nDescription: Apple scab is a fungal disease that affects apple trees. It causes dark, scaly lesions on the leaves, fruit, and twigs, leading to reduced fruit quality and yield.''',
    
    'Apple___Black_rot': '''Black Rot
    \nDescription: Black rot is a fungal disease that affects apple trees. It causes black, sunken lesions on the fruit, leaves, and branches, leading to fruit rot and defoliation.''',
    
    'Apple___Cedar_apple_rust': '''Cedar Apple Rust
    \nDescription: Cedar apple rust is a fungal disease that affects apple trees. It causes orange or rusty-colored spots on the leaves and fruit, leading to defoliation and reduced fruit quality.''',
    
    'Apple___healthy': '''Healthy Apple
    \nDescription: This class represents a healthy apple without any disease symptoms.''',
    
    'Blueberry___healthy': '''Healthy Blueberry
    \nDescription: This class represents a healthy blueberry plant without any disease symptoms.''',
    
    'Cherry_(including_sour)___Powdery_mildew': '''Powdery Mildew on Cherry
    \nDescription: Powdery mildew is a fungal disease that affects cherry trees. It causes a white powdery coating on the leaves, flowers, and fruit, leading to stunted growth and reduced yield.''',
    
    'Cherry_(including_sour)___healthy': '''Healthy Cherry
    \nDescription: This class represents a healthy cherry tree without any disease symptoms.''',
    
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': '''Cercospora Leaf Spot and Gray Leaf Spot on Corn
    \nDescription: Cercospora leaf spot and gray leaf spot are fungal diseases that affect corn plants. They cause brown or gray lesions on the leaves, reducing photosynthesis and overall plant health.''',
    
    'Corn_(maize)___Common_rust_': '''Common Rust on Corn
    \nDescription: Common rust is a fungal disease that affects corn plants. It causes orange or rusty-colored pustules on the leaves, reducing photosynthesis and yield.''',
    
    'Corn_(maize)___Northern_Leaf_Blight': '''Northern Leaf Blight on Corn
    \nDescription: Northern leaf blight is a fungal disease that affects corn plants. It causes cigar-shaped lesions on the leaves, leading to reduced photosynthesis and yield loss.''',
    
    'Corn_(maize)___healthy': '''Healthy Corn
    \nDescription: This class represents a healthy corn plant without any disease symptoms.''',
    
    'Grape___Black_rot': '''Black Rot on Grape
    \nDescription: Black rot is a fungal disease that affects grapevines. It causes black, circular lesions on the leaves and fruit, leading to defoliation and reduced fruit quality.''',
    
    'Grape___Esca_(Black_Measles)': '''Esca (Black Measles) on Grape
    \nDescription: Esca, also known as black measles, is a fungal disease that affects grapevines. It causes leaf discoloration, wood decay, and black streaks in the wood, leading to reduced vine health and yield.''',
    
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': '''Leaf Blight (Isariopsis Leaf Spot) on Grape
    \nDescription: Leaf blight, also known as Isariopsis leaf spot, is a fungal disease that affects grapevines. It causes small, brown lesions on the leaves, reducing photosynthesis and affecting fruit quality.''',
    
    'Grape___healthy': '''Healthy Grape
    \nDescription: This class represents a healthy grapevine without any disease symptoms.''',
    
    'Orange___Haunglongbing_(Citrus_greening)': '''Haunglongbing (Citrus Greening) on Orange
    \nDescription: Haunglongbing, also known as citrus greening, is a bacterial disease that affects citrus trees, including oranges. It causes mottled leaves, yellow shoots, and small, lopsided fruit, leading to reduced fruit quality and yield.''',
    
    'Peach___Bacterial_spot': '''Bacterial Spot on Peach
    \nDescription: Bacterial spot is a bacterial disease that affects peach trees. It causes dark, raised spots on the leaves and fruit, leading to defoliation and reduced fruit quality.''',
    
    'Peach___healthy': '''Healthy Peach
    \nDescription: This class represents a healthy peach tree without any disease symptoms.''',
    
    'Pepper,_bell___Bacterial_spot': '''Bacterial Spot on Bell Pepper
    \nDescription: Bacterial spot is a bacterial disease that affects bell pepper plants. It causes dark, water-soaked lesions on the leaves, fruit, and stems, leading to defoliation and reduced fruit quality.''',
    
    'Pepper,_bell___healthy': '''Healthy Bell Pepper
    \nDescription: This class represents a healthy bell pepper plant without any disease symptoms.''',
    
    'Potato___Early_blight': '''Early Blight on Potato
    \nDescription: Early blight is a fungal disease that affects potato plants. It causes brown lesions with concentric rings on the leaves, leading to defoliation and reduced tuber yield.''',
    
    'Potato___Late_blight': '''Late Blight on Potato
    \nDescription: Late blight is a fungal disease that affects potato plants. It causes dark, water-soaked lesions on the leaves, stems, and tubers, leading to defoliation and rotting of the tubers.''',
    
    'Potato___healthy': '''Healthy Potato
    \nDescription: This class represents a healthy potato plant without any disease symptoms.''',
    
    'Raspberry___healthy': '''Healthy Raspberry
    \nDescription: This class represents a healthy raspberry plant without any disease symptoms.''',
    
    'Soybean___healthy': '''Healthy Soybean
    \nDescription: This class represents a healthy soybean plant without any disease symptoms.''',
    
    'Squash___Powdery_mildew': '''Powdery Mildew on Squash
    \nDescription: Powdery mildew is a fungal disease that affects squash plants. It causes white powdery patches on the leaves, stems, and fruit, leading to stunted growth and reduced yield.''',
    
    'Strawberry___Leaf_scorch': '''Leaf Scorch on Strawberry
    \nDescription: Leaf scorch is a physiological disorder that affects strawberry plants. It causes browning and necrosis of the leaf margins, leading to reduced plant vigor and fruit quality.''',
    
    'Strawberry___healthy': '''Healthy Strawberry
    \nDescription: This class represents a healthy strawberry plant without any disease symptoms.''',
    
    'Tomato___Bacterial_spot': '''Bacterial Spot on Tomato
    \nDescription: Bacterial spot is a bacterial disease that affects tomato plants. It causes dark, water-soaked lesions on the leaves, fruit, and stems, leading to defoliation and reduced fruit quality.''',
    
    'Tomato___Early_blight': '''Early Blight on Tomato
    \nDescription: Early blight is a fungal disease that affects tomato plants. It causes dark, concentric ring-shaped lesions on the leaves and fruit, leading to defoliation and reduced yield.''',
    
    'Tomato___Late_blight': '''Late Blight on Tomato
    \nDescription: Late blight is a fungal disease that affects tomato plants. It causes dark, water-soaked lesions on the leaves, stems, and fruit, leading to defoliation and rotting of the fruit.''',
    
    'Tomato___Leaf_Mold': '''Leaf Mold on Tomato
    \nDescription: Leaf mold is a fungal disease that affects tomato plants. It causes yellow or brown patches on the leaves, reducing photosynthesis and affecting fruit quality.''',
    
    'Tomato___Septoria_leaf_spot': '''Septoria Leaf Spot on Tomato
    \nDescription: Septoria leaf spot is a fungal disease that affects tomato plants. It causes small, dark spots with light centers on the leaves, leading to defoliation and reduced fruit yield.''',
    
    'Tomato___Spider_mites Two-spotted_spider_mite': '''Spider Mites Two-spotted Spider Mite on Tomato
    \nDescription: Two-spotted spider mites are pests that affect tomato plants. They cause yellowing and stippling on the leaves, reducing photosynthesis and overall plant health.''',
    
    'Tomato___Target_Spot': '''Target Spot on Tomato
    \nDescription: Target spot is a fungal disease that affects tomato plants. It causes dark, concentric ring-shaped lesions on the leaves and fruit, leading to defoliation and reduced yield.''',
    
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': '''Tomato Yellow Leaf Curl Virus
    \nDescription: Tomato yellow leaf curl virus is a viral disease that affects tomato plants. It causes yellowing, curling, and stunting of the leaves, leading to reduced fruit yield and quality.''',
    
    'Tomato___Tomato_mosaic_virus': '''Tomato Mosaic Virus
    \nDescription: Tomato mosaic virus is a viral disease that affects tomato plants. It causes mosaic patterns and mottling on the leaves, affecting photosynthesis and reducing fruit quality.''',
    
    'Tomato___healthy': '''Healthy Tomato
    \nDescription: This class represents a healthy tomato plant without any disease symptoms.'''
}

