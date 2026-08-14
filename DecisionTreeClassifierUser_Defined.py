Border = "-" * 40


######################################################
# Step 01 : Load Dataset
######################################################

def LoadDataset(FileName):

    print(Border)
    print("Step 01 : Load Dataset")
    print(Border)

    File = open(FileName, "r")

    Data = File.readlines()

    File.close()

    Dataset = []

    # Header Skip

    for Line in Data[1:]:

        Values = Line.strip().split(",")

        print("Values in :", Values)

        Point = {

            "sepal length (cm)": float(Values[0]),
            "sepal width (cm)": float(Values[1]),
            "petal length (cm)": float(Values[2]),
            "petal width (cm)": float(Values[3]),
            "species": Values[4]

        }

        Dataset.append(Point)

    return Dataset


######################################################
# Step 02 : Get New Point
######################################################

def GetPoint():

    print(Border)
    print("Step 02 : Get New Point")
    print(Border)

    Sepal_Length = float(input("Enter Sepal Length (cm): "))
    Sepal_Width = float(input("Enter Sepal Width (cm): "))
    Petal_Length = float(input("Enter Petal Length (cm): "))
    Petal_Width = float(input("Enter Petal Width (cm): "))

    New_Point = {

        "sepal length (cm)": Sepal_Length,
        "sepal width (cm)": Sepal_Width,
        "petal length (cm)": Petal_Length,
        "petal width (cm)": Petal_Width

    }

    print(New_Point)

    return New_Point


######################################################
# Step 03 : Find Best Split
######################################################

def FindSplit(Data):

    print(Border)
    print("Step 03 : Find Best Split")
    print(Border)

    Feature_Cols = [

        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"

    ]

    Best_Feature = ""
    Best_Threshold = 0

    for Feature in Feature_Cols:

        Total = 0

        for Point in Data:

            Total = Total + Point[Feature]

        Threshold = Total / len(Data)

        print(
            Feature,
            "Threshold:",
            Threshold
        )

    Best_Feature = Feature
    Best_Threshold = Threshold

    return Best_Feature, Best_Threshold


######################################################
# Step 04 : Split Data
######################################################

def SplitData(Data, Feature, Threshold):

    print(Border)
    print("Step 04 : Split Data")
    print(Border)

    Left_Data = []

    Right_Data = []

    for Point in Data:

        if Point[Feature] <= Threshold:

            Left_Data.append(Point)

        else:

            Right_Data.append(Point)

    print("Left Data:", len(Left_Data))
    print("Right Data:", len(Right_Data))

    return Left_Data, Right_Data


######################################################
# Step 05 : Check Split Result
######################################################

def CheckSplit(Left_Data, Right_Data):

    print(Border)
    print("Step 05 : Check Split Result")
    print(Border)

    print("Left Data:", len(Left_Data))
    print("Right Data:", len(Right_Data))

    if len(Left_Data) > len(Right_Data):

        print("Left Data Is Bigger")

    else:

        print("Right Data Is Bigger")


######################################################
# Step 06 : Find Majority
######################################################

def FindMajority(Data):

    print(Border)
    print("Step 06 : Find Majority")
    print(Border)

    Class_Count = {}

    for Point in Data:

        Class = Point["species"]

        Class_Count[Class] = Class_Count.get(Class, 0) + 1

    Maximum_Count = 0
    Majority_Class = ""

    for Class in Class_Count:

        if Class_Count[Class] > Maximum_Count:

            Maximum_Count = Class_Count[Class]
            Majority_Class = Class

    print("Class Count:", Class_Count)
    print("Majority Class:", Majority_Class)
    print("Maximum Count:", Maximum_Count)

    return Majority_Class


######################################################
# Step 07 : Prediction
######################################################

def Prediction(New_Point, Feature, Threshold, Left_Class, Right_Class):

    print(Border)
    print("Step 07 : Prediction")
    print(Border)

    if New_Point[Feature] <= Threshold:

        Result = Left_Class

    else:

        Result = Right_Class

    print("Final Prediction:", Result)

    return Result


######################################################
# Main Function
######################################################

def main():

    Data = LoadDataset("iris.csv")

    NewPoint = GetPoint()

    Feature, Threshold = FindSplit(Data)

    Left_Data, Right_Data = SplitData(
        Data,
        Feature,
        Threshold
    )

    CheckSplit(
        Left_Data,
        Right_Data
    )

    Left_Class = FindMajority(Left_Data)

    Right_Class = FindMajority(Right_Data)

    Prediction(
        NewPoint,
        Feature,
        Threshold,
        Left_Class,
        Right_Class
    )


######################################################
# Starter
######################################################

if __name__ == "__main__":
    main()
