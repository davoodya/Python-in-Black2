from subprocess import getoutput

getclp = getoutput("powershell get-clipboard")

if getclp == "123456789":
#if getclp.startswith("6219") and len(getclp) >= 15:
    getoutput("powershell set-clipboard 'newvalue'")
    getclp = getoutput("powershell get-clipboard")

if __name__ == "__main__":
    print(getclp)


