start
    Declarations
        string modelName
        num height
        num width
        num depth
    output "Please enter refrigerator model name"
    input modelName
    output "Please enter interior height in inches"
    input height
    output "Please enter interior width in inches"
    input width
    output "Please enter interior depth in inches"
    input depth
    refrigCapacity = height * width * depth / 1728
    print (modelName)
    print (refrigCapacity)
stop

