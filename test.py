import streamlit as st
import cv2
import tempfile
import os

def main():
    st.title("Traffic Speed Estimation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Original Traffic Video")
        st.video("traffic_video.mp4")
    
    with col2:
        st.header("Speed Estimation Video")
        st.video("speed_estimation_traffic_video.mp4")
    
    st.markdown("""
    ## How It Works
    The speed estimation process involves the following steps (also lights up if over speed limit):
    
    1. **Object Detection**: Vehicles are detected using the YOLO model.
    ```python
    model = YOLO('yolo11l.pt')
    results = model(frame)
    ```
    
    2. **Perspective Transformation**: Converts road view to a bird’s eye view for accurate distance measurement.
    ```python
    M = cv2.getPerspectiveTransform(src_points, dest_points)
    bev_x, bev_y = get_perspective_transform((cx, cy), M)
    ```
    
    3. **Speed Calculation**: Tracks vehicle positions over multiple frames and estimates speed.
    ```python
    speed_kph = total_distance * 3.6 / time_elapsed
    ```
    
    The bird’s eye view video provides a clearer representation of speed estimation.
    """)

if __name__ == "__main__":
    main()