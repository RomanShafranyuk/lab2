import argparse
import json
import re
from tqdm import tqdm
parser = argparse.ArgumentParser("Использование парсера для получения аргументов командной строки")
parser.add_argument("-input" ,type = str, default= "data.txt", help = "Путь к файлу данных")
parser.add_argument("-output", type = str, default = "result.txt", help = "Результат валидации данных")
args = parser.parse_args()
input_path = args.input
output_path = args.output
class File:
    def __init__(self,d ):
        self._inf = d.copy()

    def check_email(self):
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern,self._inf["email"]):
            return True
        return False
    def check_weight(self):
        if isinstance(self._inf["weight"],int):
            if self._inf["weight"] > 30 and self._inf["weight"] < 200:
                return True
        return False
    def check_snils(self):
        pattern  = "^\d{11}$"
        if re.match(pattern,self._inf["snils"]):
            return True
        return False

    def check_passport_number(self):
        if isinstance(self._inf["passport_number"], int):
            if self._inf["passport_number"] >= 100000 and self._inf["passport_number"] < 1000000:
                return True
        return False

    def check_university(self):
        pattern = "^.*(?:[Тт]ех|[Уу]нивер|[Аа]кадем|[Ии]нститут|им\.|СПбГУ|МФТИ|МГ(?:Т|)У).*$"
        if re.match(pattern,self._inf["university"]):
            return True
        return False

    def check_work_experience(self):
        if isinstance(self._inf["work_experience"],int):
            if self._inf["work_experience"] >= 0 and self._inf["work_experience"] <80:
                return True
        return False

    def check_academic_degree(self):
        pattern = "Бакалавр|Кандидат наук|Специалист|Магистр|Доктор наук|"
        if re.match(pattern, self._inf["academic_degree"]):
            return True
        return False

    def check_worldview(self):
        pattern = "^.+(?:изм|анство)$"
        if re.match(pattern,self._inf["worldview"]):
            return True
        return False

    def check_address(self):
        pattern = "(?:ул\.|Аллея) (?:им[\.\s]|)[^\s]+ [^\s]*(?:\s|)\d+"
        if re.match(pattern,self._inf["address"]):
            return True
        return False
