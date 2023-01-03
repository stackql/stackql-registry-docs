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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Resource name of the Message, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}`. Assigned by the server. |
| `labels` | `object` | User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
| `sendTime` | `string` | The datetime the sending application sent this message. MSH-7. |
| `patientIds` | `array` | All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message. |
| `schematizedData` | `object` | The content of an HL7v2 message in a structured format as specified by a schema. |
| `sendFacility` | `string` | The hospital that this message came from. MSH-4. |
| `createTime` | `string` | Output only. The datetime when the message was created. Set by the server. |
| `messageType` | `string` | The message type for this message. MSH-9.1. |
| `data` | `string` | Raw message bytes. |
| `parsedData` | `object` | The content of a HL7v2 message in a structured format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_hl7V2Stores_messages_get` | `SELECT` | `datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId` | Gets an HL7v2 message. |
| `projects_locations_datasets_hl7V2Stores_messages_list` | `SELECT` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Lists all the messages in the given HL7v2 store with support for filtering. Note: HL7v2 messages are indexed asynchronously, so there might be a slight delay between the time a message is created and when it can be found through a filter. |
| `projects_locations_datasets_hl7V2Stores_messages_create` | `INSERT` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received. |
| `projects_locations_datasets_hl7V2Stores_messages_delete` | `DELETE` | `datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId` | Deletes an HL7v2 message. |
| `projects_locations_datasets_hl7V2Stores_messages_ingest` | `EXEC` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received. If the method is successful, it generates a response containing an HL7v2 acknowledgment (`ACK`) message. If the method encounters an error, it returns a negative acknowledgment (`NACK`) message. This behavior is suitable for replying to HL7v2 interface systems that expect these acknowledgments. |
| `projects_locations_datasets_hl7V2Stores_messages_patch` | `EXEC` | `datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId` | Update the message. The contents of the message in Message.data and data extracted from the contents such as Message.create_time cannot be altered. Only the Message.labels field is allowed to be updated. The labels in the request are merged with the existing set of labels. Existing labels with the same keys are updated. |
