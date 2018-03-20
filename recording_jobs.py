# -*- coding: utf-8 -*-
from swarms.sdk import services
import glob, os

config = lambda: None
config.base_url = 'https://api.swarms.com/'
config.username = os.environ['SWARMS_COMMON_VOICE_EMAIL']
config.password = os.environ['SWARMS_COMMON_VOICE_PASSWORD']

campaigns, jobs, tasks, results = services.get(config)


campaign = campaigns.create({
    "name": "record audio V1",
    "title": "Donate your Voice",
    "description": "The Common Voice project is Mozilla’s initiative to help teach machines how real people speak.\n\nHelp us to collect data to make machines understand the human voice!",
    "terms": "https://voice.mozilla.org/en/terms",
    "estDuration": "15 seconds",
    "workerPayment": 0.00,
    "results": 1
})

os.chdir("data")
i = 0
for file in glob.glob("*.txt"):
    f = open(file, "r")
    for line in f:
        i = i + 1
        sentence = line.replace("\n", "")
        
        job = jobs.create({
            "name": "record audio V1 - " + str(i),
            "properties": {
                "sentence": sentence,
                "dataset": file
            }
        })

        task = tasks.create({
            "name": "record audio V1 - " + str(i),
            "components": [
                {
                    "type": "Text",
                    "style": "Instruction",
                    "text": "Please tap to record, then read the following sentence aloud.",
                }, {
                    "type": "Text",
                    "style": "Quote",
                    "text": sentence,
                }, {
                    "type": "AudioRecording",
                    "minDurationInSeconds": 0,
                    "maxDurationInSeconds": 50
                }
            ],
            "properties": {
                "sentence": sentence,
                "dataset": file
            }
        })


        jobs.update_tasks(job, [task])
        print "created for " + sentence
        campaigns.add_jobs(campaign, [job])

campaigns.publish(campaign)
