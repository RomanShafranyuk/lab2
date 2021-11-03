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

class Validator:
    data: list

    def __init__(self, input):
        self.data = []
        tmp = json.load(open(input, encoding="windows-1251"))
        for i in tmp:
            self.data.append(File(i.copy()))

    def validation(self, index):
        result = {}
        result["email"] = self.data[index].check_email()
        result["weight"] = self.data[index].check_weight()
        result["snils"] = self.data[index].check_snils()
        result["passport_number"] = self.data[index].check_passport_number()
        result["university"] = self.data[index].check_university()
        result["work_experience"] = self.data[index].check_work_experience()
        result["academic_degree"] = self.data[index].check_academic_degree()
        result["worldview"] = self.data[index].check_worldview()
        result["adress"] = self.data[index].check_address()
        return result.copy()

    def count_valid_records(self):
        count_correct = 0
        for i in tqdm(range(len(self.data)), desc="Подсчёт корректных записей", ncols=100):
            if not (False in self.validation(i).values()):
                count_correct += 1
        return count_correct

    def invalid_record_print(self, index):
        print(self.data[index]._inf)

    def count_invalid_records(self):
        count_incorrect = 0
        for i in tqdm(range(len(self.data)), desc="Подсчёт некорректных записей", ncols=100):
            if False in self.validation(i).values():
                count_incorrect += 1
        return count_incorrect

    def result_file(self, output):
        tmp = []
        for i in tqdm(range(len(self.data)), desc="Запись результата валидации в файл", ncols=100):
            # if not(False in self.validation(i).values()):
            if False in self.validation(i).values():
                tmp.append(self.data[i]._inf.copy())
        json.dump(tmp, open(output, "w", encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)

    def count_invalid_arguments(self):
        lst_res = []
        count_inv_email = 0
        count_inv_weight = 0
        count_inv_snils = 0
        count_inv_passport_number = 0
        count_inv_university = 0
        count_inv_work_experience = 0
        count_inv_academic_degree = 0
        count_inv_worldview = 0
        count_inv_address = 0
        for i in tqdm(range(len(self.data)), desc="Подсчёт некорректных записей  данных", ncols=100):
            if self.data[i].check_email() == False:
                count_inv_email += 1
            if self.data[i].check_weight() == False:
                count_inv_weight += 1
            if self.data[i].check_snils() == False:
                count_inv_snils += 1
            if self.data[i].check_passport_number() == False:
                count_inv_passport_number += 1
            if self.data[i].check_university() == False:
                count_inv_university += 1
            if self.data[i].check_work_experience() == False:
                count_inv_work_experience += 1
            if self.data[i].check_academic_degree() == False:
                count_inv_academic_degree += 1
            if self.data[i].check_worldview() == False:
                count_inv_worldview += 1
            if self.data[i].check_address() == False:
                count_inv_address += 1
        lst_res.append(count_inv_email)
        lst_res.append(count_inv_weight)
        lst_res.append(count_inv_snils)
        lst_res.append(count_inv_passport_number)
        lst_res.append(count_inv_university)
        lst_res.append(count_inv_work_experience)
        lst_res.append(count_inv_academic_degree)
        lst_res.append(count_inv_worldview)
        lst_res.append(count_inv_address)
        return lst_res

val = Validator(input_path)
valid = val.count_valid_records()
invalid = val.count_invalid_records()
lst_result = val.count_invalid_arguments()
val.result_file(output_path)
print("Статистика:")
print("Число валидных записей:", valid)
print("Общее число невалидных записей:", invalid)
print("Число невалидных записей 'email':", lst_result[0])
print("Число невалидных записей 'weight':", lst_result[1])
print("Число невалидных записей 'snils':", lst_result[2])
print("Число невалидных записей 'pasport_number':", lst_result[3])
print("Число невалидных записей 'university':", lst_result[4])
print("Число невалидных записей 'work_experience':", lst_result[5])
print("Число невалидных записей 'academic_degree':", lst_result[6])
print("Число невалидных записей 'worldwiew':", lst_result[7])
print("Число невалидных записей 'address':", lst_result[8])
