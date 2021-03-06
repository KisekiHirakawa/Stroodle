# AWS Transcribe Streaming Example Java Application 

Example Java Application using AWS SDK creating streaming transcriptions via AWS Transcribe

## License Summary

This sample code is made available under a modified MIT license. See the LICENSE file.

## Setup

This application assumes your credentials are defined in the same way the [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html#credentials-default)
requires.

To generate an executable jar, use the following commands:
```bash
export AWS_ACCESS_KEY_ID=<your access key>
export AWS_SECRET_KEY=<your secret key>
export AWS_REGION=us-west-2
mvn clean package
java -jar target/aws-transcribe-sample-application-1.0-SNAPSHOT-jar-with-dependencies.jar
```

## Description

This application demonstrates how to use AWS Transcribe's streaming API by wrapping it in a graphical user-interface. 
The code with the call to the Transcribe API is located in TranscribeStreamingClientWrapper.java, in the 
"startTranscription" method.

This API takes advantage of a more advanced AWS SDK feature: the EventStream. These allow for streaming APIs by defining
behaviors to execute for multiple types of events, including success and error events. You can see an example 
implementation of this behavior defined in the WindowController.java class, in the "getResponseHandlerForWindow" method.
These events are handled asynchronously, but you can see an example of treating the streaming API as a synchronous 
service in the TranscribeStreamingSynchronousClient.java class, which is used for reading files in the UI.

## Classes

|Class|Description|
|---|---|
| `TranscribeStreamingDemoApp` | Main method that launches the application, instantiates the `WindowController` |
| `WindowController` | Handles the GUI elements for the application. Also defines the behavior for the responses from the Stream API |
| `TranscribeStreamingClientWrapper` | Wrapper around the AWS SDK Transcribe Client, provides examples of how to call the SDK's methods properly |
| `AudioStreamPublisher` | Used to provide streaming events to the service, wraps `ByteToAudioEventSubscription` |
| `ByteToAudioEventSubscription` | Converts bytes from audio input into AudioEvents to send to the AWS Transcribe Service |
| `TranscribeStreamingRetryClient` | Wraps retry logic around the AWS Transcribe SDK, including resuming sessions in the case of disconnects |
| `StreamTranscriptionBehavior` | Class required by `TranscribeStreamingRetryClient` to determine response handling behavior |
| `TranscribeStreamingSynchronousClient` | Class providing example of turning the asynchronous event-stream API into a synchronous one | 

## See Also
https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html
