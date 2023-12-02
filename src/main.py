from youtube_transcript_api import YouTubeTranscriptApi
import json

print("Starting transcription")

# Set an array of YouTube IDs to transcribe
youtubeIdArray = []
with open('./src/youtube-ids.json', 'r') as file:
    youtubeIdArray = json.load(file)

# Iterate through the array of YouTube IDs
for youtubeId in youtubeIdArray:

    # Retrieve the transcript for the video
    try:
        retrievedTranscript = YouTubeTranscriptApi.get_transcript(youtubeId)
        print("Retrieved transcript for " + youtubeId)
        transcribedText = ""
    except:
        print("Could not retrieve transcript for " + youtubeId)
        continue
    finally:
        print("Continuing to next video")

    # Iterate through the transcript and add each section to a string
    for transcribedSection in retrievedTranscript:
        transcribedText += transcribedSection["text"] + " "

    # Write the transcribed text to a transcript file
    print("Writing transcript for " + youtubeId + " to file")
    transcriptionFile = open("./build/transcript.txt", "a")
    transcriptionFile.write(transcribedText)
    transcriptionFile.close()

print("Finished transcribing")
