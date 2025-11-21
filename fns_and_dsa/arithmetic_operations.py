def perform_operation(num1, num2, operation):
    match operation:
        case op if operation == 'add':
            result = num1 + num2
            return result

        case op if operation == 'subtract':
            result = num1 - num2
            return result

        case op if operation == 'multiply':
            result = num1 * num2
            return result

        case op if operation == 'divide':
            if num2 == 0:
                result =  "Cannot divide by Zero"
                return result
            else:
                result = num1 / num2
                return result

