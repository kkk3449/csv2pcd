import argparse
import open3d as o3d
import os, sys

    
def visualize_pcd(data_path):
    pointcloud = o3d.io.read_point_cloud(data_path)
    o3d.visualization.draw_geometries([pointcloud])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--pcd_dir", help="output pcd dir",  default="/home/ksm/caselab/ldr_143.pcd")
    args = parser.parse_args()
    #dir = os.path.dirname(os.path.abspath(__file__))
    pcd_path = args.pcd_dir

    if (not os.path.exists(pcd_path)) or (not pcd_path.endswith(".pcd")):
        print("ERROR: file {} is not a pcd file".format(pcd_path) )
        sys.exit()

    visualize_pcd(pcd_path)
