class flickr_dataset:

  def __init__(self, all_captions, images):
    # define anything required for below two functions, like path 
    self.captions = all_captions
    self.images = images
      
  
  def __len__(self):
    # return total number of examples
    return len(self.images)
      

  def __getitem__(self, index):
    # input: an index i
    # return image, captions
    img = self.images[index]
    cap = self.captions[img]
    return img, cap
    