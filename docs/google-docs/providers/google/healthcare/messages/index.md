---
title: messages
hide_title: false
hide_table_of_contents: false
keywords:
  - messages
  - healthcare
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.messages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `hl7V2Messages` | `array` | The returned Messages. Won't be more Messages than the value of page_size in the request. See view for populated fields. |
| `nextPageToken` | `string` | Token to retrieve the next page of results or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId` | Gets an HL7v2 message. |
| `list` | `SELECT` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Lists all the messages in the given HL7v2 store with support for filtering. Note: HL7v2 messages are indexed asynchronously, so there might be a slight delay between the time a message is created and when it can be found through a filter. |
| `create` | `INSERT` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received. |
| `delete` | `DELETE` | `datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId` | Deletes an HL7v2 message. |
| `ingest` | `EXEC` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received. If the method is successful, it generates a response containing an HL7v2 acknowledgment (`ACK`) message. If the method encounters an error, it returns a negative acknowledgment (`NACK`) message. This behavior is suitable for replying to HL7v2 interface systems that expect these acknowledgments. |
| `patch` | `EXEC` | `datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId` | Update the message. The contents of the message in Message.data and data extracted from the contents such as Message.create_time cannot be altered. Only the Message.labels field is allowed to be updated. The labels in the request are merged with the existing set of labels. Existing labels with the same keys are updated. |
