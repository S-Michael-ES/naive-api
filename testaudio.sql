ALTER TABLE track ADD COLUMN audio_file_url TEXT;
UPDATE track
SET audio_file_url = 'https://naive-streaming-audio.s3.us-east-2.amazonaws.com/roadkill.wav'
WHERE track_title = 'Roadkill';
ALTER TABLE track ALTER COLUMN audio_file_url SET NOT NULL;