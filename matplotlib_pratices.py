import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,30,40,50]

plt.scatter(x,y,color="Red")
plt.title("Study hours VS Scores")
plt.xlabel("study hours")
plt.ylabel("Score")
plt.grid(True)
plt.show()