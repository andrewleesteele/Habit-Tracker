# Habit-Tracker
Utilize applets on IFTT to track location & time data around a specific geofence. Location and time data are then recorded as events on a fully functional calendar.

## Future functionality
* Integrate with Google Calendar. Instead of creating stand-alone calendar, verify if activity was completed and if not, remove listing from calendar.
* Color code entries based on missed days.

## Workflow
![Screenshot](img/iftt.png?style=centerme)
![Screenshot](img/data.png?style=centerme)
![Screenshot](img/calendar.png?style=centerme)



## In order to run

Create a virtualenv to run app in:

```shell
virtualenv habit_tracker
cd habit_tracker
```

Activate virtualenv:

```shell
source bin/activate
```

Install Flask in your virtualenv:

```shell
pip install Flask
```

Update events data and then run flask web app:

```shell
python update_data.py
python main.py
```

Check out updated web calendar on your browser of choice at localhost:5000



