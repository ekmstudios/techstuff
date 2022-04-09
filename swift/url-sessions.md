Networking with URLSession

Concurrency - doing multiple things at once
DoSomething()
DoAnotherThing()
DoSomethingElse()

A single path of execution

A path of execution = thread

We write our code on the main thread


As we write more code, we create more threads

A Quad core processor has 4 threads that your code can run on. If your code requires more than 4 threads, the computer will use a scheduler to switch back and forth to different threads

If we do too much work on the main thread, 


Threading Options
NSThread where you mana

GCD (Grand Centra Dispatch) - framework used to handle concurrent operations

Operation Queues - built on top of GCDs

With iOS13, also can use Combine
Combine allows you to switch between threads with operators



URLSession - a collection of related tasks

URLSessionConfiguration Class
Three types of object
default - uses a persistent disk based cache, stores credentials in user’s keychain, etc
ephemeral - 
background(withIdentifier:)



Data Tasks

URLSessionDataTask
Response in memory
Not supported in background sessions
URLSessionUploadTask
Easier to provide request body
URLSessionDownloadTask
Response written to file on disk

When you start a task, is created in a waiting state.
You must call the resume method to start the task.


Downloading and Uploading

Priorities and cache policies
Download task
Show download progress
Pause, resume, and cancel downloads
Meet Vapor
Upload Task
