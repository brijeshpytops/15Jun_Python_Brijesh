# import math
# print(dir(math))
# print(math.factorial(5))

import random

# print(random.random())
# print(random.randint(1, 100))
# print(random.randrange(1, 100, 2))

# musics = ['m1', 'm2', 'm3', 'm4', 'm5']
# random.shuffle(musics)
# print(musics)


import datetime

# current_time = datetime.datetime.now()

# print(current_time.strftime('%d-%m-%Y, %I:%M:%S %p - %a - %j'))

# print(current_time)

# print("Date", current_time.date())
# print("Time", current_time.time())
# print("Weekday", current_time.weekday())
# print("Year", current_time.year)
# print("month", current_time.month)
# print("month", current_time.day)

# print(current_time + datetime.timedelta(hours=1))
# print(current_time - datetime.timedelta(hours=1))
# print(current_time)


from datetime import datetime
import pytz

countryTimezones = {
  'Afghanistan': 'Asia/Kabul',
  'Albania': 'Europe/Tirane',
  'Algeria': 'Africa/Algiers',
  'Andorra': 'Europe/Andorra',
  'Angola': 'Africa/Luanda',
  'Antarctica': 'Antarctica/Palmer',
  'Argentina': 'America/Argentina/Buenos_Aires',
  'Armenia': 'Asia/Yerevan',
  'Australia': 'Australia/Sydney',
  'Austria': 'Europe/Vienna',
  'Azerbaijan': 'Asia/Baku',
  'Bahamas': 'America/Nassau',
  'Bahrain': 'Asia/Bahrain',
  'Bangladesh': 'Asia/Dhaka',
  'Barbados': 'America/Barbados',
  'Belarus': 'Europe/Minsk',
  'Belgium': 'Europe/Brussels',
  'Belize': 'America/Belize',
  'Benin': 'Africa/Porto-Novo',
  'Bhutan': 'Asia/Thimphu',
  'Bolivia': 'America/La_Paz',
  'Bosnia and Herzegovina': 'Europe/Sarajevo',
  'Botswana': 'Africa/Gaborone',
  'Brazil': 'America/Sao_Paulo',
  'Brunei': 'Asia/Brunei',
  'Bulgaria': 'Europe/Sofia',
  'Burkina Faso': 'Africa/Ouagadougou',
  'Burundi': 'Africa/Bujumbura',
  'Cambodia': 'Asia/Phnom_Penh',
  'Cameroon': 'Africa/Douala',
  'Canada': 'America/Toronto',
  'Cape Verde': 'Atlantic/Cape_Verde',
  'Central African Republic': 'Africa/Bangui',
  'Chad': 'Africa/Ndjamena',
  'Chile': 'America/Santiago',
  'China': 'Asia/Shanghai',
  'Colombia': 'America/Bogota',
  'Comoros': 'Indian/Comoro',
  'Congo': 'Africa/Brazzaville',
  'Costa Rica': 'America/Costa_Rica',
  'Croatia': 'Europe/Zagreb',
  'Cuba': 'America/Havana',
  'Cyprus': 'Asia/Nicosia',
  'Czech Republic': 'Europe/Prague',
  'Denmark': 'Europe/Copenhagen',
  'Djibouti': 'Africa/Djibouti',
  'Dominican Republic': 'America/Santo_Domingo',
  'East Timor': 'Asia/Dili',
  'Ecuador': 'America/Guayaquil',
  'Egypt': 'Africa/Cairo',
  'El Salvador': 'America/El_Salvador',
  'Estonia': 'Europe/Tallinn',
  'Eswatini': 'Africa/Mbabane',
  'Ethiopia': 'Africa/Addis_Ababa',
  'Fiji': 'Pacific/Fiji',
  'Finland': 'Europe/Helsinki',
  'France': 'Europe/Paris',
  'Gabon': 'Africa/Libreville',
  'Gambia': 'Africa/Banjul',
  'Georgia': 'Asia/Tbilisi',
  'Germany': 'Europe/Berlin',
  'Ghana': 'Africa/Accra',
  'Greece': 'Europe/Athens',
  'Greenland': 'America/Godthab',
  'Guatemala': 'America/Guatemala',
  'Guinea': 'Africa/Conakry',
  'Guyana': 'America/Guyana',
  'Haiti': 'America/Port-au-Prince',
  'Honduras': 'America/Tegucigalpa',
  'Hong Kong': 'Asia/Hong_Kong',
  'Hungary': 'Europe/Budapest',
  'Iceland': 'Atlantic/Reykjavik',
  'India': 'Asia/Kolkata',
  'Indonesia': 'Asia/Jakarta',
  'Iran': 'Asia/Tehran',
  'Iraq': 'Asia/Baghdad',
  'Ireland': 'Europe/Dublin',
  'Israel': 'Asia/Jerusalem',
  'Italy': 'Europe/Rome',
  'Ivory Coast': 'Africa/Abidjan',
  'Jamaica': 'America/Jamaica',
  'Japan': 'Asia/Tokyo',
  'Jordan': 'Asia/Amman',
  'Kazakhstan': 'Asia/Almaty',
  'Kenya': 'Africa/Nairobi',
  'Kiribati': 'Pacific/Tarawa',
  'Kuwait': 'Asia/Kuwait',
  'Kyrgyzstan': 'Asia/Bishkek',
  'Laos': 'Asia/Vientiane',
  'Latvia': 'Europe/Riga',
  'Lebanon': 'Asia/Beirut',
  'Lesotho': 'Africa/Maseru',
  'Liberia': 'Africa/Monrovia',
  'Libya': 'Africa/Tripoli',
  'Liechtenstein': 'Europe/Vaduz',
  'Lithuania': 'Europe/Vilnius',
  'Luxembourg': 'Europe/Luxembourg',
  'Madagascar': 'Indian/Antananarivo',
  'Malawi': 'Africa/Blantyre',
  'Malaysia': 'Asia/Kuala_Lumpur',
  'Maldives': 'Indian/Maldives',
  'Mali': 'Africa/Bamako',
  'Malta': 'Europe/Malta',
  'Marshall Islands': 'Pacific/Majuro',
  'Mauritania': 'Africa/Nouakchott',
  'Mauritius': 'Indian/Mauritius',
  'Mexico': 'America/Mexico_City',
  'Moldova': 'Europe/Chisinau',
  'Monaco': 'Europe/Monaco',
  'Mongolia': 'Asia/Ulaanbaatar',
  'Montenegro': 'Europe/Podgorica',
  'Morocco': 'Africa/Casablanca',
  'Mozambique': 'Africa/Maputo',
  'Myanmar': 'Asia/Yangon',
  'Namibia': 'Africa/Windhoek',
  'Nauru': 'Pacific/Nauru',
  'Nepal': 'Asia/Kathmandu',
  'Netherlands': 'Europe/Amsterdam',
  'New Zealand': 'Pacific/Auckland',
  'Nicaragua': 'America/Managua',
  'Niger': 'Africa/Niamey',
  'Nigeria': 'Africa/Lagos',
  'North Macedonia': 'Europe/Skopje',
  'Norway': 'Europe/Oslo',
  'Oman': 'Asia/Muscat',
  'Pakistan': 'Asia/Karachi',
  'Palestine': 'Asia/Gaza',
  'Panama': 'America/Panama',
  'Papua New Guinea': 'Pacific/Port_Moresby',
  'Paraguay': 'America/Asuncion',
  'Peru': 'America/Lima',
  'Philippines': 'Asia/Manila',
  'Poland': 'Europe/Warsaw',
  'Portugal': 'Europe/Lisbon',
  'Qatar': 'Asia/Qatar',
  'Romania': 'Europe/Bucharest',
  'Russia': 'Europe/Moscow',
  'Rwanda': 'Africa/Kigali',
  'Samoa': 'Pacific/Apia',
  'Saudi Arabia': 'Asia/Riyadh',
  'Senegal': 'Africa/Dakar',
  'Serbia': 'Europe/Belgrade',
  'Seychelles': 'Indian/Mahe',
  'Sierra Leone': 'Africa/Freetown',
  'Singapore': 'Asia/Singapore',
  'Slovakia': 'Europe/Bratislava',
  'Slovenia': 'Europe/Ljubljana',
  'Solomon Islands': 'Pacific/Guadalcanal',
  'Somalia': 'Africa/Mogadishu',
  'South Africa': 'Africa/Johannesburg',
  'South Korea': 'Asia/Seoul',
  'Spain': 'Europe/Madrid',
  'Sri Lanka': 'Asia/Colombo',
  'Sudan': 'Africa/Khartoum',
  'Suriname': 'America/Paramaribo',
  'Sweden': 'Europe/Stockholm',
  'Switzerland': 'Europe/Zurich',
  'Syria': 'Asia/Damascus',
  'Taiwan': 'Asia/Taipei',
  'Tajikistan': 'Asia/Dushanbe',
  'Tanzania': 'Africa/Dar_es_Salaam',
  'Thailand': 'Asia/Bangkok',
  'Togo': 'Africa/Lome',
  'Tonga': 'Pacific/Tongatapu',
  'Trinidad and Tobago': 'America/Port_of_Spain',
  'Tunisia': 'Africa/Tunis',
  'Turkey': 'Europe/Istanbul',
  'Turkmenistan': 'Asia/Ashgabat',
  'Uganda': 'Africa/Kampala',
  'Ukraine': 'Europe/Kiev',
  'United Arab Emirates': 'Asia/Dubai',
  'United Kingdom': 'Europe/London',
  'United States': 'America/New_York',
  'Uruguay': 'America/Montevideo',
  'Uzbekistan': 'Asia/Tashkent',
  'Vanuatu': 'Pacific/Efate',
  'Venezuela': 'America/Caracas',
  'Vietnam': 'Asia/Bangkok',
  'Yemen': 'Asia/Aden',
  'Zambia': 'Africa/Lusaka',
  'Zimbabwe': 'Africa/Harare'
}

# Define the UTC time
utc_time = datetime.utcnow()

# Define the target time zone
target_timezone = pytz.timezone('Asia/Kolkata')  # Example: New York time zone

# Convert UTC time to the target time zone
localized_time = pytz.utc.localize(utc_time).astimezone(target_timezone)

# Display the result
print("UTC Time:", utc_time)
print("Localized Time:", localized_time)
