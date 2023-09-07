<h2 align='center'> Project Description </h2>
<h4 align='center'><img src="https://github.com/alanbui2808/RSNA-MICCAI_Brain_Tumor_Radiogenomic_Classification/assets/47062764/49c990e5-2cb6-4f2e-8866-baa6e1d03117" alt="my banner"> </h4>

Image captioning is a well studied field due to its wide range of application such as human-computer interaction, adding subtitles to video, visual question answering and image search by keywords to name a few. Realizing similar images tend to have similar captions, thus given new input image, we will try to find similar images from the dataset and use their captions to generate a new caption for the input image. The input image will go under feature extraction and then will be queried against images that have similar features extracted in the database by measuring their cosine similarity. Pretrained ResNET50 is used for this task. Grabbing those captions, T5 is used to summarize those captions in order to generate the caption for the input image. The metrics used is BLEU score. The method is then compared to SOTA methods, in this case we choose to train a CNN-LSTM.

### Table of Contents

1. [Dataset Information](#dataset_info)
2. [Dependencies](#depend)
3. [Files](#files)
4. [How to Run](#run)

### Dataset Information<a name="dataset_info"></a>
Flickr8k dataset - one of the most common dataset used for image-captioning task as it contains 8000 images along with their corresponding 5 captions. Specifically, there are in total 6000 images for training, 1000 images for validation and the rest 1000 are testing images; each training, validation and test images have 5 captions.

### Dependencies<a name="depend"></a>
1. Numpy: Perform several mathematical evaluations in the preprocessing of the datasets
   
    `pip install numpy  `

2. Pandas: Loading/Processing/Storing of the different datasets

    `pip install pandas `
  
3. Matplotlib: Plotting of the training curves.

    `pip install matplotlib`
  
4. Pytorch: Please follow this <a href="https://pytorch.org/get-started/locally/"> Link </a> for a suitable installments 

5. Transformers: BERT
   
    `pip install transformers`

6. Evaluate: BLEU score evaluation

    `pip install matplotlib`

### How to Run<a name="run"></a>
* The notebook is pretty straightforward, you are recommended to run on Google Colab. However uploading the dataset can be a hassle :)
  
