def solve_addition_problems(num_problems):
  """
  Solves addition problems from user input.

  Args:
    num_problems: The number of addition problems to solve.

  Returns:
    None. Prints the solutions to each problem on a separate line.
  """

  for _ in range(num_problems):
    # Read two integers from input
    num1, num2 = map(int, input().split())
    # Calculate the sum
    sum = num1 + num2
    # Print the sum
    print(sum)


num_problems = int(input())
solve_addition_problems(num_problems)