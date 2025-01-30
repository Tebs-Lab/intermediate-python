# Kinds of Servers / Web APIs

* The most common type of server is a classic webserver
    * These serve websites mostly by sending clients CSS, JS, and HTML files.
    * We won't be doing an example of this, because we have not learned how to use HTML, JS, and CSS -- and it's too much background for one day.
* API servers though, are usually about data/resources. These are basically wrappers around CRUD operations.
    * Create, Read, Update, Delete
    * We CAN and WILL build these using just Python!
* Some APIs are focused on actions rather than data/resources
    * Some do both.
    * Sometimes the lines are blurred -- is posting on social media an action that "creates data" or "takes an action?"

## REST

* REST stands for REpresentational State Transfer.
* It's a set of rules, constraints, and guiding principles for developing Web APIs
* An API that applies these rules is called "restful"
* Some API's do not fully conform to REST principles, but do conform to most, we still usually call them restful. That's life.
* All of this is officially codified: [https://restfulapi.net/](https://restfulapi.net/)

### REST Principles:

#### 1 Uniform Interface

* In simple terms: 
    * All RESTful APIs should feel similar to use, and have similar structure.
    * Any given REST API should have a consistent and predictable structure.

* In the codified language:
    * Identification of resources – The interface must uniquely identify each resource involved in the interaction between the client and the server.

    * Manipulation of resources through representations – The resources should have uniform representations in the server response. API consumers should use these representations to modify the resource state in the server.

    * Self-descriptive messages – Each resource representation should carry enough information to describe how to process the message. It should also provide information of the additional actions that the client can perform on the resource.

    * Hypermedia as the engine of application state – The client should have only the initial URI of the application. The client application should dynamically drive all other resources and interactions with the use of hyperlinks.


* In practice this means:
    * REST APIs are almost always centered around CRUD operations on data ("resources"), though they can technically allow some function calling.
    * URLs in REST APIs follow a predictable structure
    * Each URL (or "endpoint") identifies a specific resource, collection of resources, or (rarely) a function calling endpoint.
    * host.com/resource_name/[individual_resource_identifier]
    * The API sends a consistent representation of the resource, and if the client wants to manipulate it, they must follow that same representation. 

#### 2. Client-Server

* Separation of concerns
* The API server manages the resources and data.
* The client uses that data to control the application
* If an underlying resource must be changed by the client, the server must be invoked to persist that change. e.g., To update the database, the client must go through the API.

### 3. Stateless

* When the client calls on the API it must provide ALL the relevant information in EVERY such call.
* Clients may have as much state as they wish, but the server will never store any information about a particular client or a particular session.
* i.e., servers are stateless and clients MAY or MAY NOT be stateful depending on the application.

### 4. Cacheable

* If a resource is cacheable the server should identify it as such.
* Typically a resource will have a cache expiry period, that indicates how long the client can store that resource before it should re-request it from the server (to ensure it hasn't changed, or get the new version)

#### 5. Layered System

* Individual components of the larger application should only interact with the layer "adjacent" to them.
* For example:
    * Web App (layer 1)
    * Server API (layer 2)
    * Database (layer 3)
    * In such a setup the Web App should never interact directly with the Database. 

* There is a lot of flexibility in defining the layers, but API designers should take care in doing so.
    * Clearly define the separation of concerns and which component is responsible for what process.

#### 6. Code on Demand (Optional)

* REST servers are allowed to return bits of code for the client to execute.
* But it's pretty rare.

## Remote Procedure Call (RPC)

* General term for a system that performs some action in response to a web request. 
    * The procedure can be literally anything
    * Unlike REST this is not a set of rules for making things simple
    * Technically speaking, REST does support remote function calling... but it's uncommon and perhaps lightly frowned upon
    * I urge you not to be too pedantic... lines are often blurred in this corner of software.

* An RPC API is fundamentally "Turing complete" which is to say: anything that can be done with software can be exposed with an RPC styled API. 

* An RPC API is going to be centered around "verbs" whereas a REST or CRUD API will be centered around nouns. 

* RPC APIs may or may not be "stateless" like a REST API
    * APIs with state can be tricky because:
        * they introduce possible race conditions 
        * each call is no longer independent, and those dependencies may become hard to manage and track
    * Stateful APIs can be beneficial because:
        * Streaming data can be more performant
        * Some applications 

* There are specific frameworks and tools for building these, like gRPC.
    * But none of that is specifically needed to build or use an RPC API.

## Examples

* Twillio or ClickSnd:
    * API for sending text messages

* SendGrid, Gmail, others
    * API for sending emails

* OpenAI and other GenAI APIs
    * API for calling a generative model and retrieving the output.

* https://math.tools/api/numbers/
    * Do math on someone else's server, without implementing it yourself.

* Lots of firms may develop internal APIs to do specific tasks.
    * Kick of a training session for an ML model
    * Deploy one of their pieces of software 
    * Generate a report
    * and so on

## Note: Unfortunately...

* The vast majority of RPC based APIs require money, significant amounts of configuration, and usually both.
* So, for this class session we're going to BUILD an API server that performs actions.
* After that, we're going to write a client that uses our API servers.

## A New Tool

* I want everyone to download Postman
    * https://www.postman.com/downloads/

* It's a super useful tool for probing, testing, building, and exploring APIs
* **Instructor note: demonstrate its use to make a couple simple requests to the Github API**
* **Micro-exercise: Students do the same, for a different API route**