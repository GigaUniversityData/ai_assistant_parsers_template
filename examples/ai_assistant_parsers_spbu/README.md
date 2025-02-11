# AI Assistant Parsers SPBU

Данный шаблон написан для версии `ai-assistant-parsers-core` - `0.22.2`

## Введение

Упрощённая реализация парсеров для https://spbu.ru/ на основе шаблона [ai_assistant_parsers_template](https://github.com/GigaUniversity/ai_assistant_parsers_template).

## Задача

Реализовать код для сбора данных с 22х поддоменов сайта https://spbu.ru/ (Список ниже).

## Список URL-адресов, для которых создавалась поддержка

| URL-адрес                         | Парсер                         |
|-----------------------------------|--------------------------------|
| https://abiturient.spbu.ru        | MainAbiturientPageParser       | 
| https://students.spbu.ru/*        | TMContentMultipleDomainsParser |
| https://nauka.spbu.ru/*           | TMContentMultipleDomainsParser | 
| https://mil.spbu.ru/*             | TMContentMultipleDomainsParser | 
| https://ifea.spbu.ru/*            | TMContentMultipleDomainsParser | 
| https://guestbook.spbu.ru/*       | TMContentMultipleDomainsParser |  
| https://edu.spbu.ru/*             | TMContentMultipleDomainsParser | 
| https://library.spbu.ru/*         | TMContentMultipleDomainsParser |
| https://horizont.spbu.ru/*        | TMContentMultipleDomainsParser | 
| https://diaghilevmuseum.spbu.ru/* | TMContentMultipleDomainsParser | 
| https://cdop.chem.spbu.ru/*       | TMContentMultipleDomainsParser | 
| https://agym.spbu.ru/*            | TMContentMultipleDomainsParser | 
| https://philosophy.spbu.ru/*      | TMContentMultipleDomainsParser |
| https://apmath.spbu.ru/*          | TMContentMultipleDomainsParser |
| https://csd.spbu.ru/*             | TMContentMultipleDomainsParser |
| https://abiturient.spbu.ru/*      | AbiturientDomainParser         | 
| https://campus.spbu.ru/*          | CampusDomainParser             | 
| https://fund.spbu.ru/*            | FundDomainParser               | 
| https://studsovet.spbu.ru/*       | StudsovetDomainParser          | 
| https://spbu.ru/*                 | WWWDomainParser                |
| https://hortus.spbu.ru/*          | UniversalParser                | 
| https://300.spbu.ru/*             | UniversalParser                | 
