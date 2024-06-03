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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.messages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the Message, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/hl7V2Stores/&#123;hl7_v2_store_id&#125;/messages/&#123;message_id&#125;`. Assigned by the server. |
| <CopyableCode code="createTime" /> | `string` | Output only. The datetime when the message was created. Set by the server. |
| <CopyableCode code="data" /> | `string` | Required. Raw message bytes. |
| <CopyableCode code="labels" /> | `object` | User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p&#123;Ll&#125;\p&#123;Lo&#125;&#123;0,62&#125; Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p&#123;Ll&#125;\p&#123;Lo&#125;\p&#123;N&#125;_-]&#123;0,63&#125; No more than 64 labels can be associated with a given store. |
| <CopyableCode code="messageType" /> | `string` | The message type for this message. MSH-9.1. |
| <CopyableCode code="parsedData" /> | `object` | The content of a HL7v2 message in a structured format. |
| <CopyableCode code="patientIds" /> | `array` | All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message. |
| <CopyableCode code="schematizedData" /> | `object` | The content of an HL7v2 message in a structured format as specified by a schema. |
| <CopyableCode code="sendFacility" /> | `string` | The hospital that this message came from. MSH-4. |
| <CopyableCode code="sendTime" /> | `string` | The datetime the sending application sent this message. MSH-7. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId" /> | Gets an HL7v2 message. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Lists all the messages in the given HL7v2 store with support for filtering. Note: HL7v2 messages are indexed asynchronously, so there might be a slight delay between the time a message is created and when it can be found through a filter. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId" /> | Deletes an HL7v2 message. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, messagesId, projectsId" /> | Update the message. The contents of the message in Message.data and data extracted from the contents such as Message.create_time cannot be altered. Only the Message.labels field is allowed to be updated. The labels in the request are merged with the existing set of labels. Existing labels with the same keys are updated. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Lists all the messages in the given HL7v2 store with support for filtering. Note: HL7v2 messages are indexed asynchronously, so there might be a slight delay between the time a message is created and when it can be found through a filter. |
| <CopyableCode code="ingest" /> | `EXEC` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received. If the method is successful, it generates a response containing an HL7v2 acknowledgment (`ACK`) message. If the method encounters an error, it returns a negative acknowledgment (`NACK`) message. This behavior is suitable for replying to HL7v2 interface systems that expect these acknowledgments. |
