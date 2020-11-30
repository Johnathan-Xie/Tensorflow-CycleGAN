# Tensorflow-CycleGAN
This repository supports training and generation of unpaired image to image data.

Model structure from https://machinelearningmastery.com/cyclegan-tutorial-with-keras/; instancenormalization.py from https://github.com/keras-team/keras-contrib

Note: Default Hyperparameters are fit to the horse-to-zebra dataset.  New datasets will likely require hyperparameter fitting for good results.

# How to organize new datasets
main-folder
  -testA
  -testB
  -trainA
  -trainB
  
# Checkpoints
To begin training or inference from a checkpoint, pass--from-ckpt option for training(inference always requires checkpoint) and 4 models are required
  -Discriminator A
    -Discriminator to differentiate between real and fake A images
    -parsed with --d_model_A_ckpt
  -Discriminator B
    -Discriminator to differntiate between real and fake B images
    -parsed with --d_model_B_ckpt
  -Generator A to B
    -Generator to create fake B images from A images
    -parsed with --g_model_AtoB_ckpt
  -Generator B to A
    -Generator to create fake A images from B images
    -parsed with --g_model_BtoA_ckpt
