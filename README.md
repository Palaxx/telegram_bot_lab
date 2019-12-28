# Telegram Bot with Python
This repo is linked to a [presentation](https://slides.com/palaxx/telegrambot) on slides.com.

The goal of this lab is to introduce a programmer, without experience on python and telegram, on bot's
developments. 
I will use this repo and presentation for an internal lab for the company I'm working for. 

I'm not an expertise bot developer, so could the *guru* excuses me in case of mistakes. 

This repo is diveded into some incremental levels, from 0 to 5. 
I prefer to create a initial *requirements.txt* instead add record based on the current level, 
so you have to do install all the dependencies only the first time. 

```bash
pip install -r requirments.txt
```


## Level 0
```bash
git checkout level0
```
**Topics:**
- Introduce the *Telepot* package
- Use the *.env* file
- Retrieve the first messages

## Level 1
```bash
git checkout level1
```
**Topics:**
- Use the *Telepot MessageLoop*
- Send your first message

## Level 2
```bash
git checkout level2
```
**Topics:**
- How to detect the received commands
- Simple parameters parsing

## Level 3
```bash
git checkout level3
```
**Topics:**
- Send random photos using an external service
- Introduce custom keyboards

## Level 4
```bash
git checkout level4
```
**Topics:**
- Send different message based on chat_id
- Introduce the *schedule* package

## Level 5
```bash
git checkout level5
```
**Topics:**

Build a working bot to retrieve every X minutes the value of a selected cryptocurrency