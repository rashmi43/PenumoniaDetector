
import matplotlib.pyplot as plt
import pydicom
import os


def read_image(img_path):
    dataset = pydicom.dcmread(img_path)

    # Normal mode:
    print()
    print("Filename.........:", img_path)
    print("Storage type.....:", dataset.SOPClassUID)
    print()

    pat_name = dataset.PatientName
    display_name = pat_name.family_name + ", " + pat_name.given_name
    print("Patient's name...:", display_name)
    print("Patient id.......:", dataset.PatientID)
    print("Modality.........:", dataset.Modality)
    print("Study Date.......:", dataset.StudyDate)

    if 'PixelData' in dataset:
        rows = int(dataset.Rows)
        cols = int(dataset.Columns)
        print("Image size.......: {rows:d} x {cols:d}, {size:d} bytes".format(
            rows=rows, cols=cols, size=len(dataset.PixelData)))
        if 'PixelSpacing' in dataset:
            print("Pixel spacing....:", dataset.PixelSpacing)

    # use .get() if not sure the item exists, and want a default value if missing
    print("Slice location...:", dataset.get('SliceLocation', "(missing)"))

    # plot the image using matplotlib
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.show()


def main():
    path = os.path.join('.', 'data', 'stage_2_train_images', '0a03a65b-9e45-4e3d-ae6c-b8a37112ab31.dcm')
    read_image('../data/stage_2_train_images/0a03a65b-9e45-4e3d-ae6c-b8a37112ab31.dcm')


if __name__== "__main__":
    main()

