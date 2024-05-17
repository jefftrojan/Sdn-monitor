import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit app
def main():
    st.set_page_config(page_title="SDN Network Monitoring", layout="wide")
    st.title("SDN Network Monitoring")

    # Sidebar menu
    menu = st.sidebar.radio("Navigation", ["Network Topology", "Device Monitoring", "Link Monitoring", "Time-Series Monitoring"])

    if menu == "Network Topology":
        show_topology()
    elif menu == "Device Monitoring":
        show_device_monitoring()
    elif menu == "Link Monitoring":
        show_link_monitoring()
    elif menu == "Time-Series Monitoring":
        show_time_series_monitoring()

# Display network topology
def show_topology():
    st.subheader("Network Topology")
    nodes = st.text_area("Enter nodes (one per line)").split("\n")
    edges = st.text_area("Enter edges (one per line, e.g., 'Node1,Node2')").split("\n")

    G = nx.Graph()
    G.add_nodes_from(nodes)

    for edge in edges:
        if ',' in edge:
            node1, node2 = edge.split(',')
            G.add_edge(node1, node2)

    fig, ax = plt.subplots(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, ax=ax)
    st.pyplot(fig)

# Display device monitoring data
def show_device_monitoring():
    st.subheader("Device Monitoring")
    devices = st.text_area("Enter devices (one per line)").split("\n")
    cpu_usage = {device: st.number_input(f"CPU Usage (%) for {device}", min_value=0, max_value=100, value=50) for device in devices}
    mem_usage = {device: st.number_input(f"Memory Usage (%) for {device}", min_value=0, max_value=100, value=50) for device in devices}

    cpu_df = pd.DataFrame.from_dict(cpu_usage, orient='index', columns=['CPU Usage (%)'])
    mem_df = pd.DataFrame.from_dict(mem_usage, orient='index', columns=['Memory Usage (%)'])

    st.subheader("CPU Usage")
    st.bar_chart(cpu_df)

    st.subheader("Memory Usage")
    st.bar_chart(mem_df)

# Display link monitoring data
def show_link_monitoring():
    st.subheader("Link Monitoring")
    links = st.text_area("Enter links (one per line, e.g., 'Node1,Node2')").split("\n")
    link_util = {(link.split(',')[0], link.split(',')[1]): st.number_input(f"Link Utilization (%) for {link}", min_value=0, max_value=100, value=50) for link in links}

    link_df = pd.DataFrame.from_dict(link_util, orient='index', columns=['Link Utilization (%)'])
    link_df = link_df.reset_index()
    link_df.columns = ['Link', 'Link Utilization (%)']

    st.subheader("Link Utilization")
    st.bar_chart(link_df.set_index('Link'))

    # Filter links based on utilization threshold
    threshold = st.slider("Link Utilization Threshold (%)", 0, 100, 50)
    filtered_links = link_df[link_df['Link Utilization (%)'] >= threshold]
    st.write(f"Links with utilization >= {threshold}%:")
    st.dataframe(filtered_links)

# Display time-series monitoring data
def show_time_series_monitoring():
    st.subheader("Time-Series Monitoring")
    # Implement time-series monitoring data input and visualization

if __name__ == "__main__":
    main()
# import streamlit as st
# import networkx as nx
# import matplotlib.pyplot as plt
# import pandas as pd
# import random
# from datetime import datetime, timedelta

# # Create a sample network topology
# G = nx.Graph()
# G.add_nodes_from(['Router1', 'Switch1', 'Switch2', 'Host1', 'Host2'])
# G.add_edges_from([('Router1', 'Switch1'), ('Router1', 'Switch2'), ('Switch1', 'Host1'), ('Switch2', 'Host2')])

# # Sample monitoring data
# devices = ['Router1', 'Switch1', 'Switch2', 'Host1', 'Host2']
# cpu_usage = {device: random.randint(20, 80) for device in devices}
# mem_usage = {device: random.randint(30, 90) for device in devices}
# link_util = {('Router1', 'Switch1'): random.randint(10, 70),
#              ('Router1', 'Switch2'): random.randint(10, 70),
#              ('Switch1', 'Host1'): random.randint(10, 70),
#              ('Switch2', 'Host2'): random.randint(10, 70)}

# # Sample time-series monitoring data
# time_range = pd.date_range(start=datetime.now() - timedelta(hours=6), periods=7, freq='H')
# cpu_usage_time_series = {device: [random.randint(20, 80) for _ in range(len(time_range))] for device in devices}
# mem_usage_time_series = {device: [random.randint(30, 90) for _ in range(len(time_range))] for device in devices}

# # Streamlit app
# def main():
#     st.set_page_config(page_title="SDN Network Monitoring", layout="wide")
#     st.title("SDN Network Monitoring")

#     # Sidebar menu
#     menu = st.sidebar.radio("Navigation", ["Network Topology", "Device Monitoring", "Link Monitoring", "Time-Series Monitoring"])

#     if menu == "Network Topology":
#         show_topology()
#     elif menu == "Device Monitoring":
#         show_device_monitoring()
#     elif menu == "Link Monitoring":
#         show_link_monitoring()
#     elif menu == "Time-Series Monitoring":
#         show_time_series_monitoring()

# # Display network topology
# def show_topology():
#     fig, ax = plt.subplots(figsize=(10, 8))
#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, ax=ax)
#     st.pyplot(fig)

# # Display device monitoring data
# def show_device_monitoring():
#     cpu_df = pd.DataFrame.from_dict(cpu_usage, orient='index', columns=['CPU Usage (%)'])
#     mem_df = pd.DataFrame.from_dict(mem_usage, orient='index', columns=['Memory Usage (%)'])

#     st.subheader("CPU Usage")
#     st.bar_chart(cpu_df)

#     st.subheader("Memory Usage")
#     st.bar_chart(mem_df)

# # Display link monitoring data
# def show_link_monitoring():
#     link_df = pd.DataFrame.from_dict(link_util, orient='index', columns=['Link Utilization (%)'])
#     link_df = link_df.reset_index()
#     link_df.columns = ['Link', 'Link Utilization (%)']

#     st.subheader("Link Utilization")
#     st.bar_chart(link_df.set_index('Link'))

#     # Filter links based on utilization threshold
#     threshold = st.slider("Link Utilization Threshold (%)", 0, 100, 50)
#     filtered_links = link_df[link_df['Link Utilization (%)'] >= threshold]
#     st.write(f"Links with utilization >= {threshold}%:")
#     st.dataframe(filtered_links)

# # Display time-series monitoring data
# def show_time_series_monitoring():
#     device_selected = st.selectbox("Select Device", devices)

#     cpu_data = pd.DataFrame(cpu_usage_time_series[device_selected], index=time_range, columns=['CPU Usage (%)'])
#     mem_data = pd.DataFrame(mem_usage_time_series[device_selected], index=time_range, columns=['Memory Usage (%)'])

#     st.subheader(f"Time-Series Monitoring: {device_selected}")

#     st.line_chart(cpu_data)
#     st.line_chart(mem_data)

# if __name__ == "__main__":
#     main()