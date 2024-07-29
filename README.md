# csv2pcd
this code convert BLK360 Raw .csv (X,Y,Z,R,G,B) data to .pcd visualized data by shift operator.

### install Python 3.8.10
### install pypcd
```pip3 install --upgrade git+https://github.com/klintan/pypcd.git```

### install python libraries
```pip3 install setuptools==60.2.0```
```pip3 install jupyter-client==7.4.9```
```pip3 install open3d```

## Fix your numpy_pc2.py
```nano /home/ksm/.local/lib/python3.8/site-packages/pypcd/numpy_pc2.py```
### before
```def get_xyz_points(cloud_array, remove_nans=True, dtype=np.float):```
### after
```def get_xyz_points(cloud_array, remove_nans=True, dtype=np.float64):```

### csv2pcd
```python3 csv2pcd.py```
### visualized
```python3 pcd_visualized.py```

![Screenshot from 2024-07-29 20-19-38](https://github.com/user-attachments/assets/364635a2-bd1d-455f-9def-64764ff3cf0b)
