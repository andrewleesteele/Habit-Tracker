import googleapi
import dateparser
import json

SPREADSHEET_ID = '1T2n-ZdcHEm4vNqm0eXYeCnflD6gsBMuPkWTUyOga-LU'
RANGE_NAME = 'Location!A1:C'
WORKOUTS = ['Chest/Triceps', 'Back/Biceps', 'Shoulders', 'Legs']

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    # Call the Sheets API
    results = googleapi.getRawData(SPREADSHEET_ID, RANGE_NAME)
    results = cleanResults(results)
    results = toJson(results)

    file = open("events.json","w") 
    file.write(str(results).replace('\'',''))
    file.close() 

def cleanResults(results):
    dates = []

    for i in range(0, len(results), 2):
        start_time = dateparser.parse(results[i][0])
        end_time = dateparser.parse(results[i+1][0])
        dates.append([start_time, end_time])

    return dates

def toJson(results):

    entries = []

    for i in range(len(results)):
        info = {
            "title": WORKOUTS[i%4],
            "start": results[i][0].isoformat(),
            "end": results[i][1].isoformat()
        }
        entries.append(json.dumps(info))

    return entries


if __name__ == '__main__':
    main()
