class InputData():
    def get_address(self, question, max_questions):
        interest_points = []
        counter = 0
        answer = []
        while answer != 'n' and counter < max_questions :
            answer = raw_input(question)
            interest_points.append(answer)
            counter +=1
        return interest_points



#
#
# client = InputData()
# addresses = client.get_address("\nGive me an address: ")
# print addresses