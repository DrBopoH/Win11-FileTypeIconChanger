from typing import Dict, Any
import winreg as reg
import re, os, json

langs: Dict[str, Any] = {
	"eng": {
		'instruction':         "Welcome to the application for semi-manually changing icons of file extension types/formats! \nI've sometimes had difficulties with the fact that most project files in the working directory are displayed as <unrecognized> or <other> file types.\nThis application is designed, of course, not as a panacea, but still partially solve the problem! \nHow it works: You write the format of the file to which you want to declare an icon, for example - .py .js .java .cpp .json and others.\nAnd in the second line write the path to the file, for example - C\\Users\\Your user name\\Documents\\Code\\JavaScript\\JScript\\icon-js.ico (you can with quotes, which happens with the standard <copy as path>)\nVuala! Everything works, as long as the icons don't overlap the applications you configured as <open always through>.\nIf there are any errors, try to fix them. You may still have to dig into the case manually :(\n But I hope you don't have to! Thank you for using my app.\n",
		'input':              ["File extension/format:", "Path to new icon file:"],
		'success':            ["Icon for files with extension",  "successfully changed!", "A computer restart will be required to apply system variable changes*"],
		'errorNotFound':      ["Error: File type",               "not found in registry :("],
		'errorNotPermissions': "Error: Insufficient permissions to modify registry. Run application as administrator!",
		'errorOther':          "There's been some kind of unforeseen error! Here are details:"
	}
}



def read(filepath):
	with open(filepath, 'r', encoding='utf-8') as file:
		return json.load(file)



def checkLangSettingsFile() -> None:
	if not os.path.exists('.lang'):
		with open('.lang', "w") as file:
			file.write("eng")



def getLangSettings() -> str:
    try:
        with open('.lang', "r") as file:
            lang = file.readline().lower()
            return lang if lang in langs else 'eng'
    except Exception:
        return 'eng'




def removeUnwantedChars(inPut: str = '', dots: bool = True) -> str:
    if dots:
        return re.sub(r'[\'"]', '', inPut)
    else:
        return inPut.replace('.', '')



def setFileIcon(lang: str, file_extension: str, icon_path: str) -> None:
	try:
		reg_key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, f".{file_extension}", 0, reg.KEY_READ)
		file_class, _ = reg.QueryValueEx(reg_key, "")
		reg.CloseKey(reg_key)

		reg_key = reg.OpenKey(reg.HKEY_CLASSES_ROOT, f"{file_class}\\DefaultIcon", 0, reg.KEY_SET_VALUE)
		
		reg.SetValueEx(reg_key, None, 0, reg.REG_SZ, icon_path)
		reg.CloseKey(reg_key)
		
		print(f"{langs[lang]['success'][0]} <{file_extension}> {langs[lang]['success'][1]}{icon_path}\n{langs[lang]['success'][2]}")
		
	except FileNotFoundError:
		print(f"{langs[lang]['errorNotFound'][0]} <{file_extension}> {langs[lang]['errorNotFound'][1]}")
	except PermissionError:
		print(f"{langs[lang]['errorNotPermissions']}")
	except Exception as e:
		print(f"{langs[lang]['errorOther']} {e}")



if __name__ == "__main__":
	langs = langs | read('locales.json')

	checkLangSettingsFile()
	lang = getLangSettings()

	print(langs[lang]['instruction'])

	while True:
		print('\n')
		setFileIcon(lang, removeUnwantedChars(input(f'{langs[lang]['input'][0]} '), False), removeUnwantedChars(input(f'{langs[lang]['input'][1]} ')))