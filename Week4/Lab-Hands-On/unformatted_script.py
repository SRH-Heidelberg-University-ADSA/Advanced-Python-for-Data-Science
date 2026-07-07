import math,sys

def compute_statistics(numbers):
  total=0
  for n in numbers:
      total+=n
  mean=total/len(numbers)
  variance=0
  for n in numbers:
     variance+=(n-mean)**2
  variance=variance/len(numbers)
  std_dev=math.sqrt(variance)
  return mean,std_dev


def process_data(data):
    results=[]
    for item in data:
        if item%2==0:
             results.append(item*item)
        else:
             results.append(item+1)
    return results


def main():
 numbers=[1,2,3,4,5,6,7,8,9,10]
 processed=process_data(numbers)
 mean,std=compute_statistics(processed)

 print("Processed:",processed)
 print("Mean:",mean,"Std:",std)


if __name__=="__main__":
      main()
