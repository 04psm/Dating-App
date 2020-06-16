import guihelper
import dbhelper


class Tinder(guihelper.GUI):
    def __init__(self):
        self._dbObject=dbhelper.DBHelper()
        super().__init__(self.loginHandler, self.regHandler)

    def loginHandler(self,email,password):
        response=self._dbObject.search("email",email, "password",password,"users")
        if len(response)==0:
            print("Invalid email/password")
        else:
            self.user_id=response[0][0]
            self.doLogin(response)


    def doLogin(self, data):
        self.mainWindow(self,data, mode=1)

    def viewUsers(self, num):
        data=[]
        response=self._dbObject.searchOne('user_id', self.user_id, 'users', 'NOT LIKE')

        if num<0:
            self.printMessage("Error", "No users before this one")
        elif num>len(response)-1:
            self.printMessage("Error", "Iske aage bhi koi nai hai")
        else:
            x = response[num]
            data.append(x)
            # print(data)
            self.mainWindow(self, data, mode=2, num=num)



    def regHandler(self, name, email, password, age, gender, city, bio):

        mydict={
            'user_id':"NULL",
            'fname':name,
            'email':email,
            'password':password,
            'age':age,
            'gender':gender,
            'bg':'avatar.jpg',
            'city':city,
            'bio':bio
        }
        flag=self._dbObject.insert(mydict, 'users')
        if flag==0:
            print("Reg Failed")
        else:
            print("Reg successful")

    def propose(self, juliet_id):
        data=self._dbObject.search('romeo_id',self.user_id,'juliet_id',juliet_id,'proposals')

        if len(data)>0:
            self.printMessage("Error", "Abe Despo ruk ja")
        else:
            mydict={
                'proposal_id':'NULL',
                'romeo_id':self.user_id,
                'juliet_id':juliet_id
            }

            response=self._dbObject.insert(mydict,'proposals')

            if response==1:
                self.printMessage("Success", "Proposal sent successfully.Fingers Crosssed")
            else:
                self.printMessage("Proposal Failed"," Beda gark. Nahi hoya")


obj1=Tinder()