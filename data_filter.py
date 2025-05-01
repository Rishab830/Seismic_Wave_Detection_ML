import os
import obspy

for folder in os.listdir("Final_java_earthquake_data"):
    st = obspy.Stream()
    for file in os.listdir(f"Final_java_earthquake_data/{folder}/waveforms"):
        st += obspy.read(f"Final_java_earthquake_data/{folder}/waveforms/{file}")
    st.plot()
    print(file)
    