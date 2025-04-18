"""
Description : 
"""

# Libraries
import pandas as pd

# Utils
def get_distance(sample1, sample2):
    distance_sum = 0
    for i in range(len(sample1)):
        distance_feature = (sample1[i] - sample2[i]) *  (sample1[i] - sample2[i])
        distance_sum+=distance_feature
    
    distance = distance_sum**0.5
    return distance

def sort_array(distance_results):
    for i in range(len(distance_results)):
        for j in range(i+1,len(distance_results)):
            if distance_results[j]["distance_score"]<distance_results[i]["distance_score"]:
                backup  = distance_results[j]
                distance_results[j] = distance_results[i]
                distance_results[i] = backup
    
    return distance_results

# Where the magic happens
def get_classification_result(new_sample, df, k=3):
    class_names = {
        "setosa":0,
        "virginica":0,
        "versicolor":0
    }
    k = 3
    distance_list = []
    for index, row in df.iterrows():
        data_sample = [row["sepal_length"],row["sepal_width"],row["petal_length"],row["petal_width"]]
        d = get_distance(new_sample, data_sample)
        d_result = {
            "index":index,
            "distance_score":d,
            "class":row["species"]
        }
        distance_list.append(d_result)

    sorted_distance_list = sort_array(distance_list)
    filtered_list = sorted_distance_list[:k]
    for i in filtered_list:
        class_names[i["class"]]+=1

    most_class = 0
    classification_result = ""
    for key, value in class_names.items():
        if value>most_class:
            classification_result = key

    return classification_result


if __name__ == "__main__":
    df = pd.read_csv("dataset/iris.csv")
    new_sample = [4.6,3.1,1.5,0.2] #Setosa
    result = get_classification_result(new_sample, df, 5)
    print(result)