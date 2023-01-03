---
title: hl7_v2_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - hl7_v2_stores
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
<tr><td><b>Name</b></td><td><code>hl7_v2_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.hl7_v2_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the HL7v2 store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`. |
| `rejectDuplicateMessage` | `boolean` | Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the IngestMessageResponse as has been returned previously. Note that only one resource is created in the store. When this field is set to true, CreateMessage/IngestMessage requests with a duplicate message will be rejected by the store, and IngestMessageErrorDetail returns a NACK message upon rejection. |
| `labels` | `object` | User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
| `notificationConfigs` | `array` | A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client. |
| `parserConfig` | `object` | The configuration for the parser. It determines how the server parses the messages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_hl7V2Stores_get` | `SELECT` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Gets the specified HL7v2 store. |
| `projects_locations_datasets_hl7V2Stores_list` | `SELECT` | `datasetsId, locationsId, projectsId` | Lists the HL7v2 stores in the given dataset. |
| `projects_locations_datasets_hl7V2Stores_create` | `INSERT` | `datasetsId, locationsId, projectsId` | Creates a new HL7v2 store within the parent dataset. |
| `projects_locations_datasets_hl7V2Stores_delete` | `DELETE` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Deletes the specified HL7v2 store and removes all messages that it contains. |
| `projects_locations_datasets_hl7V2Stores_export` | `EXEC` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Exports the messages to a destination. To filter messages to be exported, define a filter using the start and end time, relative to the message generation time (MSH.7). This API returns an Operation that can be used to track the status of the job by calling GetOperation. Immediate fatal errors appear in the error field. Otherwise, when the operation finishes, a detailed response of type ExportMessagesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata. |
| `projects_locations_datasets_hl7V2Stores_import` | `EXEC` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Import messages to the HL7v2 store by loading data from the specified sources. This method is optimized to load large quantities of data using import semantics that ignore some HL7v2 store configuration options and are not suitable for all use cases. It is primarily intended to load data into an empty HL7v2 store that is not being used by other clients. An existing message will be overwritten if a duplicate message is imported. A duplicate message is a message with the same raw bytes as a message that already exists in this HL7v2 store. When a message is overwritten, its labels will also be overwritten. The import operation is idempotent unless the input data contains multiple valid messages with the same raw bytes but different labels. In that case, after the import completes, the store contains exactly one message with those raw bytes but there is no ordering guarantee on which version of the labels it has. The operation result counters do not count duplicated raw bytes as an error and count one success for each message in the input, which might result in a success count larger than the number of messages in the HL7v2 store. If some messages fail to import, for example due to parsing errors, successfully imported messages are not rolled back. This method returns an Operation that can be used to track the status of the import by calling GetOperation. Immediate fatal errors appear in the error field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a response of type ImportMessagesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata. |
| `projects_locations_datasets_hl7V2Stores_patch` | `EXEC` | `datasetsId, hl7V2StoresId, locationsId, projectsId` | Updates the HL7v2 store. |
