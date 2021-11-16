import nibabel as nib
import numpy as np
import os
img = nib.load('/data/home/cddu/pythonProject/data/GenericObjectDecoding/raw/sub-03_ses-perceptionTraining01_func_sub-03_ses-perceptionTraining01_task-perception_run-01_bold.nii.gz')
data = img.get_data()
# data = data.T  # pycortex assumes the first dimension to be TRs

subject_id = 'your_subject_id'
transform_name = 'your_transform_name'

# data_to_show = data[0]  # assuming you want to show the first TR
data_to_show = np.mean(data,axis=3).astype('int16')  # assuming you want to show the first TR
# vol = cortex.Volume(data_to_show, subject_id, transform_name)
# cortex.webgl.show(vol)

img = nib.Nifti1Image(data_to_show, np.eye(4))  # Save axis for data (just identity)

img.header.get_xyzt_units()
img.to_filename(os.path.join('build','/data/home/cddu/pythonProject/data/GenericObjectDecoding/raw/ref-img.nii.gz'))  # Save as NiBabel file


# img = nib.load('/data/home/cddu/anaconda3/envs/py3/share/pycortex/db/GOD-S3/transforms/fullhead/reference.nii.gz')
# data = img.get_data()
