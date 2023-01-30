from django.db import models
from datetime import datetime


class usersManger(models.Manager):
    def basic_validtor(self, post_data):
        errors = {}
        if len(post_data['name']) < 3:
            errors["name"] = "Name should be at least 3 characters"
        if len(post_data['regNum']) == 8:
            errors["regNum"] = "Registraion Number must be 8 numbers"
        if len(post_data['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if post_data['password'] != post_data['confrimPassword']:
            errors["confrimPassword"] = "No match password "
        if gymUsers.objects.filter(email=post_data['email']).exists():
            errors["email"] = "Email Already existsed !!!"
        if gymUsers.objects.filter(regNum=post_data['regNum']).exists():
            errors["regNumExisted"] = "Registraion Number Already existsed !!!"
        return errors

    def basic_informatiom_validator(self, postData):
        error = {}
        if len(postData['firstName']) < 1:
            error['firstName'] = "First Name should be at least 1 character"
        if len(postData['lastName']) < 1:
            error['lastName'] = "Last Name should be at least 1 character"
        if len(postData['birthDate']) < 1:
            error['birthDate'] = "Invalid Birth Date"
        if (len(postData['phone']) == 0) or (len(postData['phone']) != 10):
            error['phone'] = "Invalid Phone Number"
        return error


class gymUsers(models.Model):
    name = models.CharField(max_length=45, null=False)
    address = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=25, null=False)
    phone = models.IntegerField()
    regNum = models.IntegerField(null=False)
    amount = models.IntegerField()
    password = models.CharField(max_length=45, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = usersManger()


class participants(models.Model):
    participantName = models.CharField(max_length=45, null=True)
    sex = models.CharField(max_length=10, null=False)
    age = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=45, null=False)
    legalNumber = models.IntegerField(null=False)
    phoneNumber = models.IntegerField(null=True)
    midicalHistory = models.TextField(max_length=255, null=True)
    gymUser = models.ForeignKey(gymUsers, related_name='gymUser_par_id', on_delete=models.CASCADE)


class subScriptions(models.Model):
    gymUser = models.ForeignKey(
        gymUsers, related_name='gymUser_sub_id', on_delete=models.CASCADE)
    participantUser = models.ForeignKey(
        participants, related_name='participantUser_id', on_delete=models.CASCADE)
    amount = models.IntegerField()
    _from = models.DateField(auto_now_add=True)
    _to = models.DateTimeField(auto_now=True)
    active=models.IntegerField(default=0,null=False)


def Register(request):
    name = request.POST['name']
    address = request.POST['address']
    email = request.POST['email']
    phone = request.POST['phone']
    regNum = request.POST['regNum']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if (request.POST['confrimPassword'] == password):
        return gymUsers.objects.create(name=name, address=address, email=email, phone=phone, regNum=regNum, password=pw_hash)


def Login(request):
    _gymUsers = gymUsers.objects.filter(email=request.POST['email'])
    if _gymUsers:
        loged_user = _gymUsers[0]
        if bcrypt.checkpw(request.POST['password'].encode(), loged_user.password.encode()):
            request.session['userid'] = loged_user.id
            request.session['username'] = loged_user.name
            return True
        else:
            request.session['LoginAuth'] = "Username or password does not exist"
            return False
    else:
        request.session['LoginAuth'] = "Username or password does not exist"
        return False
