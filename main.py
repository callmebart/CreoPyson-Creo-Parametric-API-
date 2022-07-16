#Open creoSon SETUP and Creo PARAMETRIC project
import creopyson
c = creopyson.Client()
c.connect()
print ("Creason server is working!")
c.creo_set_creo_version(7)

print(c.dimension_list_detail())
dd = c.dimension_list_detail()

parameters = ['AA','B','param_c','DD','E','F']
paramsToTxtFile = []
for x in dd:
    if(x['name'] == 'AA' or x['name'] == 'AA' or x['name'] == 'B' or x['name'] == 'param_c' or x['name'] == 'DD' or x['name'] == 'E' or x['name'] == 'B'):
        paramsToTxtFile.append({'name':x['name'],'value':x['value']})


     


#changing file path
print(" ")
pathValue = input("Type in folder path e.g D:/Projekty Creo 2022/Projekt2 :\n")
c.creo_cd(pathValue);
print("log: Path changed to: ",pathValue)

print("opening model")
isModelHere = True
modelName="model.prt.39"
import os.path
while isModelHere:
    modelName = input("podaj nazwę modelu: ")
    isDir = os.path.exists(pathValue+"/"+modelName)
    print(pathValue+"/"+modelName)
    print(isDir)
    if isDir:
        isModelHere = False

org_string = modelName
size = len(modelName)
# Slice string to remove last character from string
mod_string = org_string[:size - 3]
print("opening:",mod_string)
c.file_open(mod_string)

print(paramsToTxtFile[0]['name'])
f= open("model.txt","w+")
f.write("Nazwa:"+org_string+"\n")
for i in range(len(paramsToTxtFile)):
     f.write("" + str(paramsToTxtFile[i]['name'])+" = "+ str(paramsToTxtFile[i]['value'])+"\n")
f.write("Nazwa materiału:"+str(c.file_get_cur_material())+"\n")
f.write("Masa modelu:"+str(c.file_massprops())+"\n")
f.close()
#change parameter value
print(" ")

for i in range(len(parameters)):
    print(i, end = ".")
    print(parameters[i])



changingParameters = "n"

while changingParameters == "n":
    #Changing dimensions
    print(" ")
    paramName = 'error'
    while parameters.count(paramName) == 0:
        paramName = input("Type in parameter name:\n")

        print('selected:', paramName)

    paramValue = 8
    while paramValue < 9:
        paramValue = int(input("Type in parameter value e.q 200:\n"))

    c.dimension_set(paramName,paramValue)
    #model regenerate
    c.file_regenerate()
    print("log: model regenerated")
    changingParameters = input("Do you want to stop changing parameters y/n ?:\n")


#material 'Non-ferrous_metals'
path = "C:/Program Files/PTC/Creo 7.0.1.0/Common Files/text/materials-library/Standard-Materials_Granta-Design/Non-ferrous_metals"
materials = ["Silver.mtl", "Gold.mtl", "Lead.mtl", "Copper_cast.mtl", "Tin.mtl", "Titanium.mtl", "Nickel.mtl", "Zinc.mtl", "Bronze_cast.mtl", "Cu-Al_alloy.mat"]

print(" ")
for i in range(len(materials)):
    print (i, end = ".")
    print (materials[i])

print(" ")
materialValue = 10
while materialValue > 9 or materialValue<0:
    materialValue = int(input("Select index of material (0-9):\n"))

c.file_load_material_file(materials[materialValue],path)
c.file_set_cur_material(materials[materialValue])
print("log: added material: ",materials[materialValue])

#model regenerate
c.file_regenerate()
print("log: model regenerated")

print("")
isName = input("Czy chcesz zmienić nazwę modelu? y/n ")

if isName=="y" :
    name = input("podaj nową nazwę: ")
    c.file_rename(name)
    print("zmieniono nazwę na :",name)

print("")
isAccept = input("Czy chcesz wyeksportować model? y/n ")

if isAccept=="y" :
    c.interface_export_file("STEP")
    c.interface_export_3dpdf()
    print("model zapisany")

print("")
isAccept = input("Czy zapisać model? y/n ")

if isAccept=="y" :
    c.file_save()

    print("model zapisany")


print("")
isAccept = input("Czy zapisać dodać model do złożenia? y/n ")

if isAccept=="y" :
    print("")
    print("")
    #assembly parts
    c.file_open("asm.asm")
    c.file_assemble("model.prt")
    print("files assembled")

