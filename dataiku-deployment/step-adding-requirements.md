# Telling Python Which Packages to Include in Your Environment

When building your custom model server you can include any Python packages your heart desires. All you have to do is specify these using a `requirements.txt` file.

First, create the file itself.

```(bash)
touch requirements.txt
```{{execute}}

Next, add the Python packages which have been imported in the `RandomForest.py` file to your `requirements.txt`.

```(text)
numpy
pymml
seldon-core
```

And that's it! Your Python environment is ready to rock and roll.
