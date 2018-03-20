# Purpose

Swarms supports Mozilla's [Common Voice Project](https://voice.mozilla.org/). We created a commission-free account for the project that can publish jobs without payments. Volunteers from our mobile crowd are encouraged to donate their voice to the project by working on charity jobs. The data is generated under the [terms of the Common Voice Project](https://voice.mozilla.org/en/terms) and the [terms of the Swarms Platform](https://www.swarms.com/terms-and-conditions/).

We will make the dataset available to the public and share it with the Common Voice Community.

# Recordings

For the first stage, `recording_jobs.py` creates and publishes new jobs in our platform, where the volunteers can record their voices. The texts for recordings are taken from the [common voice web repository](https://github.com/mozilla/voice-web/tree/master/server/data). Our mobile interface of the jobs looks like this:


<img src="https://s3.eu-central-1.amazonaws.com/swarmsblobstorage/common_voice_recording_ui.gif" alt="Recroding UI Sample" width= "300"/>

The volunteer can record the audio, replay the recording or rerecord it. Currently, each job requests only one recording.