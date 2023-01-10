---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - fitness
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.fitness.data_sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | An end-user visible name for this data source. |
| `dataQualityStandard` | `array` | DO NOT POPULATE THIS FIELD. It is never populated in responses from the platform, and is ignored in queries. It will be removed in a future version entirely. |
| `dataStreamId` | `string` | A unique identifier for the data stream produced by this data source. The identifier includes: - The physical device's manufacturer, model, and serial number (UID). - The application's package name or name. Package name is used when the data source was created by an Android application. The developer project number is used when the data source was created by a REST client. - The data source's type. - The data source's stream name. Note that not all attributes of the data source are used as part of the stream identifier. In particular, the version of the hardware/the application isn't used. This allows us to preserve the same stream through version updates. This also means that two DataSource objects may represent the same data stream even if they're not equal. The exact format of the data stream ID created by an Android application is: type:dataType.name:application.packageName:device.manufacturer:device.model:device.uid:dataStreamName The exact format of the data stream ID created by a REST client is: type:dataType.name:developer project number:device.manufacturer:device.model:device.uid:dataStreamName When any of the optional fields that make up the data stream ID are absent, they will be omitted from the data stream ID. The minimum viable data stream ID would be: type:dataType.name:developer project number Finally, the developer project number and device UID are obfuscated when read by any REST or Android client that did not create the data source. Only the data source creator will see the developer project number in clear and normal form. This means a client will see a different set of data_stream_ids than another client with different credentials. |
| `dataStreamName` | `string` | The stream name uniquely identifies this particular data source among other data sources of the same type from the same underlying producer. Setting the stream name is optional, but should be done whenever an application exposes two streams for the same data type, or when a device has two equivalent sensors. |
| `dataType` | `object` |  |
| `device` | `object` | Representation of an integrated device (such as a phone or a wearable) that can hold sensors. Each sensor is exposed as a data source. The main purpose of the device information contained in this class is to identify the hardware of a particular data source. This can be useful in different ways, including: - Distinguishing two similar sensors on different devices (the step counter on two nexus 5 phones, for instance) - Display the source of data to the user (by using the device make / model) - Treat data differently depending on sensor type (accelerometers on a watch may give different patterns than those on a phone) - Build different analysis models for each device/version.  |
| `type` | `string` | A constant describing the type of this data source. Indicates whether this data source produces raw or derived data. |
| `application` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_dataSources_get` | `SELECT` | `dataSourceId, userId` | Returns the specified data source. |
| `users_dataSources_list` | `SELECT` | `userId` | Lists all data sources that are visible to the developer, using the OAuth scopes provided. The list is not exhaustive; the user may have private data sources that are only visible to other developers, or calls using other scopes. |
| `users_dataSources_create` | `INSERT` | `userId` | Creates a new data source that is unique across all data sources belonging to this user. A data source is a unique source of sensor data. Data sources can expose raw data coming from hardware sensors on local or companion devices. They can also expose derived data, created by transforming or merging other data sources. Multiple data sources can exist for the same data type. Every data point in every dataset inserted into or read from the Fitness API has an associated data source. Each data source produces a unique stream of dataset updates, with a unique data source identifier. Not all changes to data source affect the data stream ID, so that data collected by updated versions of the same application/device can still be considered to belong to the same data source. Data sources are identified using a string generated by the server, based on the contents of the source being created. The dataStreamId field should not be set when invoking this method. It will be automatically generated by the server with the correct format. If a dataStreamId is set, it must match the format that the server would generate. This format is a combination of some fields from the data source, and has a specific order. If it doesn't match, the request will fail with an error. Specifying a DataType which is not a known type (beginning with "com.google.") will create a DataSource with a *custom data type*. Custom data types are only readable by the application that created them. Custom data types are *deprecated*; use standard data types instead. In addition to the data source fields included in the data source ID, the developer project number that is authenticated when creating the data source is included. This developer project number is obfuscated when read by any other developer reading public data types. |
| `users_dataSources_delete` | `DELETE` | `dataSourceId, userId` | Deletes the specified data source. The request will fail if the data source contains any data points. |
| `users_dataSources_update` | `EXEC` | `dataSourceId, userId` | Updates the specified data source. The dataStreamId, dataType, type, dataStreamName, and device properties with the exception of version, cannot be modified. Data sources are identified by their dataStreamId. |
