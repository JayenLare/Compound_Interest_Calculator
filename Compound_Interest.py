# Compound Interest Calculator using Python --- Jayen Lare

# Convert user inputted letter input into corresponding integer value
def letterToValue(letter):
  if letter == 'A':
    return 1
  elif letter == 'B':
    return 2
  elif letter == 'Q':
    return 4
  elif letter == 'M':
    return 12
  elif letter == 'D':
    return 365

# Main function
def main():
  # Prints title of program 
  print("Compound Interest Calculator")
  print("-----------------------------")
  print("")

  # Receive initial investment from user
  print("Initial Investment...")
  initial = float(input("Enter your initial investment: "))
  print("")

  # Frequency of recurring contribution
  print("Contribution...")
  print("How often will you contribute to your investment: ")
  print("A: Annually")
  print("B: Biannually")
  print("Q: Quarterly")
  print("M: Monthly")
  print("D: Daily")
  contribution = input("Enter the letter of your choice: ").upper()
  # Converts letter to corresponding integer value
  contribution = letterToValue(contribution)
  # Receives amount of money and time for recurring contribution
  amount = float(input("How much money will contribute each time: "))
  length = int(input("How many years do you plan to contribute for: "))
  print("")

  # Receives interest rate as percent and converts to decimal
  print("Interest Rate...")
  rate = float(input("What percent is your estimated interest rate: "))
  rate = rate/100
  # Receives variance and converts to decimal
  variance = float(input("By how much could your interest rate vary: "))
  variance = variance/100
  # Add/Subtracts variance to get above and below rates
  aboveRate = rate + variance
  belowRate = rate - variance
  print("")

  # Frequency of compounding
  print("Compound Frequency...")
  print("How many times a year will your investment compound: ")
  print("A: Annually")
  print("B: Biannually")
  print("Q: Quarterly")
  print("M: Monthly")
  print("D: Daily")
  frequency = input("Enter the letter of your choice: ").upper()
  # Converts frequency letter input to corresponding integer value
  frequency = letterToValue(frequency)
  print("")

  # Uses compound interest formula for both initail investment and contribution for normal rate and variance rates
  initialResult = (initial * ((1 + rate/frequency) ** (frequency * length)))
  compoundResult = amount * (contribution/frequency) * (((1 + rate/frequency) ** (frequency * length) - 1) / (rate/frequency))
  aboveInitialResult = (initial * ((1 + aboveRate/frequency) ** (frequency * length)))
  belowInitialResult = (initial * ((1 + belowRate/frequency) ** (frequency * length)))
  aboveCompoundResult = amount * (contribution/frequency) * (((1 + aboveRate/frequency) ** (frequency * length) - 1) / (aboveRate/frequency))
  belowCompoundResult = amount * (contribution/frequency) * (((1 + belowRate/frequency) ** (frequency * length) - 1) / (belowRate/frequency))

  # Adds initial compound interest and contribution compound interest to get final result, and its variances
  finalResult = initialResult + compoundResult
  aboveFinalResult = aboveInitialResult + aboveCompoundResult
  belowFinalResult = belowInitialResult + belowCompoundResult

  # Formats results in US dollar format and displays results 
  formattedResult = "${:,.2f}".format(finalResult)
  aboveFormattedResult = "${:,.2f}".format(aboveFinalResult)
  belowFormattedResult = "${:,.2f}".format(belowFinalResult)
  print("In " + str(length) + " years, you will have " + str(formattedResult))
  print("Your above variance in " + str(length) + " years will be " + str(aboveFormattedResult))
  print("Your below variance in " + str(length) + " years will be " + str(belowFormattedResult))

# Runs main function
if __name__ == "__main__":
  main()
