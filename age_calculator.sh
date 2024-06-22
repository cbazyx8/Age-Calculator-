#!/bin/bash

echo "Welcome to the Age Calculator!"
read -p "Enter your birthdate (YYYY-MM-DD): " birthdate

if [[ ! $birthdate =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo "Invalid date format. Please use YYYY-MM-DD."
    exit 1
fi

birth_year=${birthdate:0:4}
birth_month=${birthdate:5:2}
birth_day=${birthdate:8:2}

current_year=$(date +%Y)
current_month=$(date +%m)
current_day=$(date +%d)

age=$((current_year - birth_year))

if (( current_month < birth_month || (current_month == birth_month && current_day < birth_day) )); then
    age=$((age - 1))
fi

echo "Your age is: $age years old."
