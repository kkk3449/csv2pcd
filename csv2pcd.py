import argparse
import pandas as pd
import os,sys,csv,numpy as np
from pypcd import pypcd

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--csv_dir", help="input csv dir", default="/home/ksm/client-library-master/linux/samples/22-colorize-pc-ldr/build/pointcloud_142.csv")
    parser.add_argument("--pcd_dir", help="output pcd dir",  default="/home/ksm/caselab/pointcloud_142_111.pcd")

    args = parser.parse_args()

    csv_file = args.csv_dir
    CSV=readCSV(csv_file)
    save_path =args.pcd_dir
    csv2pcd(CSV,save_path)
    print("Change CSV to PCD Successfully")

def readCSV(file):
    """Read files cloud points csv.
    Args:
        self: The object pointer.
        file (str): path to files cloud points (csv).
    Returns:
        cloud (str): cloud points (x,y,z,r,g,b).
    """
    data = pd.read_csv(file)
    cloud = np.array(data)
    return cloud

def csv2pcd(data, save_path):
    cloud = np.array(data, copy=False)
    rgb = cloud[:,3:6]
    rgb = rgb.astype(np.uint32)
    rgb = np.array((rgb[:, 0] << 16) | (rgb[:, 1] << 8) | (rgb[:, 2] << 0) )
    rgb.dtype = np.float32
    cloud_dt = np.dtype(dict(names=['x','y','z','rgb'], formats=['f4','f4','f4','f4']))
    cloud_arr = np.empty(len(data), dtype=cloud_dt)
    cloud_arr['x'], cloud_arr['y'], cloud_arr['z'], cloud_arr['rgb'] = data[:,0], data[:,1], data[:,2], rgb.view('f4')
    md = {'version': .7,
      'fields': ['x', 'y', 'z', 'rgb'],
      'count': [1, 1, 1, 1],
      'width': len(cloud_arr),
      'height': 1,
      'viewpoint': [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
      'points': len(cloud_arr),
      'type': ['F', 'F', 'F', 'F'],
      'size': [4, 4, 4, 4],
      'data': 'binary'}
    pc_data = cloud_arr.view(np.dtype([('x', np.float32),
                                 ('y', np.float32),
                                 ('z', np.float32),
                                 ('rgb', np.float32)])).squeeze()
    new_cloud = pypcd.PointCloud(md, pc_data)
    new_cloud.save_pcd(save_path)

if __name__ == "__main__":
    main()
