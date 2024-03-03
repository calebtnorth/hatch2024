import json
import os
import secrets
import shutil
from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

global AID

key = get_random_bytes(16)
def Tree(srcPath, AID):
    global path
    #global srcPath
    global newPath
    global dstPath
    global dstPath
    
    print("hello")
    parentDir = "/Users/calebnorth/Desktop/hatchdata/forest"
    path = os.path.join(parentDir, AID)
    try:
        os.makedirs(path)
        print("Directory '%s' created" % path)
    except FileExistsError:
        print("Directory exists")

    
    dstPath = os.path.join(path, os.path.basename(srcPath))
    shutil.move(srcPath, dstPath)
    with open("India.txt", "a") as bears:
        print("writing")
        bears.write(f"\n{AID} is  {os.path.basename(srcPath)}")
    
#Tree()
def AEncrypt(filePath, AID, desDir):
    
    for AIDFolder in os.listdir("/Users/calebnorth/Desktop/hatchdata/forest"):
        AIDForest = os.path.join("/Users/calebnorth/Desktop/hatchdata/forest", AIDFolder)
        for file in os.listdir(AIDForest):
            filePath = os.path.join(AIDForest, file)
            if file.endswith(".fasta"):
                Write1(os.path.join(AIDForest, file), AID, desDir)
    
uploadDir = os.getenv('UPLOAD_DIR')
def Set1(uploadDir:str) -> list[str]:
    global setPath
    global TID
    setInStr = uploadDir 
    setPath = (os.fsencode(setInStr))
    encryptedFilePaths = []
    
    
    
    print("scanning", setInStr)
    for file in os.listdir(setInStr):
        if file.endswith(".fasta"):
            AID = ''.join(str(secrets.randbelow(7)) for _ in range(6))
            finDir = os.path.join("/Users/calebnorth/Desktop/hatchdata/forest", AID, 'encrypted',f'output{AID}.json')
            filePath = os.path.join(setInStr, file)
            desDir = os.path.join("/Users/calebnorth/Desktop/hatchdata/forest", AID, 'encrypted')
            encryptedFilePaths.append(finDir)
            Tree(os.path.join(setInStr, file), AID)
            AEncrypt(filePath, AID, desDir)
            
            Remove()
            # with open("returnDir.txt", "a") as DirReturn:
            #     DirReturn.write(f"\n{desDir}")
        else:
            print("Error")

    return encryptedFilePaths
    
def team():
    TIDxt = ("O")
    TIDgrab = []
    TID = str(hash(TIDxt))
    TIDgrab.append(TID)
    print(TIDgrab)
    return TIDgrab
    
def newFileSignal(type):
    encryptedFilePaths = Set1(dir)
    # execute ( " INSERT table DATA (?, ?)", (type, encryptedFilePaths[0]) )


keyLoca = os.getenv('KEY_LOCATION')

def Write1(inputFile, AID, desDir):
    #takes file and enrypts
    with open(keyLoca, 'wb') as fileOut:
        fileOut.write(key)
    with open(keyLoca, "rb") as fileIn:
        keyInFile = fileIn.read()
    if key == keyInFile:
        global doubleCheck
        doubleCheck = "true"
        print("key match!")
        
    else:
        print("no match")
        doubleCheck = "false"


    with open(inputFile, 'rb') as infile:
        print(infile)
        data = infile.read()

    outputDir = os.path.join("/Users/calebnorth/Desktop/hatchdata/forest", AID, 'encrypted')
    
    outputFileName = f'output{AID}.json'
    outputFile = os.path.join(desDir, outputDir, outputFileName)
    
    if not os.path.exists(outputFile):
        cipher = AES.new(key, AES.MODE_CFB)
        ct_bytes = cipher.encrypt(data)
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        result = {'iv':iv, 'ciphertext':ct}

        os.makedirs(desDir, exist_ok=True)
        with open(outputFile, 'w') as outfile:
                json.dump(result, outfile)
    else:
        print("skip")
    #print(result)
    {"iv": "VoamO23kFSOZcK1O2WiCDQ==", "ciphertext": "f8jciJ8/"}

def Remove():
    global dirs
    global files
    global root
    DirName = "/Users/calebnorth/Desktop/hatchdata/forest"
    test = os.listdir(DirName)
    for root, dirs, files in os.walk(DirName):
        for item in files:
            if item.endswith('.fasta'):
                os.remove(os.path.join(root, item))
                print("done!")

global desDir
