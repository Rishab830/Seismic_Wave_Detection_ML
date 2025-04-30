import os
import obspy
for folder in os.listdir("Final_java_earthquake_data"):
    st = obspy.Stream()
    inv_file = os.listdir(f"Final_java_earthquake_data/{folder}/stations")[0]
    inv = obspy.read_inventory(f"Final_java_earthquake_data/{folder}/stations/{inv_file}")
    for file in os.listdir(f"Final_java_earthquake_data/{folder}/waveforms"):
        st += obspy.read(f"Final_java_earthquake_data/{folder}/waveforms/{file}")
    filtered_st = st.copy()
    filtered_st.remove_response(inventory=inv, output="ACC")
    filtered_st.plot()
    # filtered_st.detrend("polynomial", order=1)
    # filtered_st.plot()
    print(folder)
