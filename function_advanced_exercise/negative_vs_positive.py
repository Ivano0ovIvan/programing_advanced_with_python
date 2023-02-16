def negative_vs_positive(nums):
    positive_numbers = [n for n in nums if n > 0]
    negative_numbers = [n for n in nums if n < 0]
    print(sum(negative_numbers))
    print(sum(positive_numbers))
    if abs(sum(negative_numbers)) > sum(positive_numbers):
        print("The negatives are stronger than the positives")
    elif abs(sum(negative_numbers)) < sum(positive_numbers):
        print("The positives are stronger than the negatives")



numbers = [int(x) for x in input().split(' ')]
negative_vs_positive(numbers)