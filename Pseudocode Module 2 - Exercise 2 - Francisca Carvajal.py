start
    Declarations
        num accountBalance
        num timesOfOverdrawn
    output "Please enter account balance"
    input accountBalance
    output "Please enter number of times the account was overdrawn"
    input timesOfOverdrawn
    overDrawnFee = accountBalance * 0.01 - timesOfOverdrawn * 5
    newAccountBalance = accountBalance - overDrawnFee
    print (overDrawnFee)
    print (newAccountBalance)
    print ("Thanks for using this program")
stop
    
