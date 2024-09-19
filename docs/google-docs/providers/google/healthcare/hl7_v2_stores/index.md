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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>hl7_v2_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hl7_v2_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.hl7_v2_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the HL7v2 store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`. |
| <CopyableCode code="labels" /> | `object` | User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
| <CopyableCode code="notificationConfigs" /> | `array` | A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client. |
| <CopyableCode code="parserConfig" /> | `object` | The configuration for the parser. It determines how the server parses the messages. |
| <CopyableCode code="rejectDuplicateMessage" /> | `boolean` | Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the IngestMessageResponse as has been returned previously. Note that only one resource is created in the store. When this field is set to true, CreateMessage/IngestMessage requests with a duplicate message will be rejected by the store, and IngestMessageErrorDetail returns a NACK message upon rejection. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Gets the specified HL7v2 store. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists the HL7v2 stores in the given dataset. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Creates a new HL7v2 store within the parent dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Deletes the specified HL7v2 store and removes all messages that it contains. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Updates the HL7v2 store. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Exports the messages to a destination. To filter messages to be exported, define a filter using the start and end time, relative to the message generation time (MSH.7). This API returns an Operation that can be used to track the status of the job by calling GetOperation. Immediate fatal errors appear in the error field. Otherwise, when the operation finishes, a detailed response of type ExportMessagesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Import messages to the HL7v2 store by loading data from the specified sources. This method is optimized to load large quantities of data using import semantics that ignore some HL7v2 store configuration options and are not suitable for all use cases. It is primarily intended to load data into an empty HL7v2 store that is not being used by other clients. An existing message will be overwritten if a duplicate message is imported. A duplicate message is a message with the same raw bytes as a message that already exists in this HL7v2 store. When a message is overwritten, its labels will also be overwritten. The import operation is idempotent unless the input data contains multiple valid messages with the same raw bytes but different labels. In that case, after the import completes, the store contains exactly one message with those raw bytes but there is no ordering guarantee on which version of the labels it has. The operation result counters do not count duplicated raw bytes as an error and count one success for each message in the input, which might result in a success count larger than the number of messages in the HL7v2 store. If some messages fail to import, for example due to parsing errors, successfully imported messages are not rolled back. This method returns an Operation that can be used to track the status of the import by calling GetOperation. Immediate fatal errors appear in the error field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a response of type ImportMessagesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Rolls back messages from the HL7v2 store to the specified time. This method returns an Operation that can be used to track the status of the rollback by calling GetOperation. Immediate fatal errors appear in the error field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a detailed response of type RollbackHl7V2MessagesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata. |

## `SELECT` examples

Lists the HL7v2 stores in the given dataset.

```sql
SELECT
name,
labels,
notificationConfigs,
parserConfig,
rejectDuplicateMessage
FROM google.healthcare.hl7_v2_stores
WHERE datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hl7_v2_stores</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.healthcare.hl7_v2_stores (
datasetsId,
locationsId,
projectsId,
name,
parserConfig,
labels,
notificationConfigs,
rejectDuplicateMessage
)
SELECT 
'{{ datasetsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ parserConfig }}',
'{{ labels }}',
'{{ notificationConfigs }}',
{{ rejectDuplicateMessage }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: parserConfig
      value:
        - name: allowNullHeader
          value: boolean
        - name: segmentTerminator
          value: string
        - name: schema
          value:
            - name: schematizedParsingType
              value: string
            - name: schemas
              value:
                - - name: version
                    value:
                      - - name: mshField
                          value: string
                        - name: value
                          value: string
                  - name: messageSchemaConfigs
                    value: object
            - name: types
              value:
                - - name: version
                    value:
                      - - name: mshField
                          value: string
                        - name: value
                          value: string
                  - name: type
                    value:
                      - - name: name
                          value: string
                        - name: primitive
                          value: string
                        - name: fields
                          value:
                            - - name: name
                                value: string
                              - name: type
                                value: string
                              - name: table
                                value: string
                              - name: minOccurs
                                value: integer
                              - name: maxOccurs
                                value: integer
            - name: ignoreMinOccurs
              value: boolean
            - name: unexpectedSegmentHandling
              value: string
        - name: version
          value: string
    - name: labels
      value: object
    - name: notificationConfigs
      value:
        - - name: pubsubTopic
            value: string
          - name: filter
            value: string
    - name: rejectDuplicateMessage
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>hl7_v2_stores</code> resource.

```sql
/*+ update */
UPDATE google.healthcare.hl7_v2_stores
SET 
name = '{{ name }}',
parserConfig = '{{ parserConfig }}',
labels = '{{ labels }}',
notificationConfigs = '{{ notificationConfigs }}',
rejectDuplicateMessage = true|false
WHERE 
datasetsId = '{{ datasetsId }}'
AND hl7V2StoresId = '{{ hl7V2StoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>hl7_v2_stores</code> resource.

```sql
/*+ delete */
DELETE FROM google.healthcare.hl7_v2_stores
WHERE datasetsId = '{{ datasetsId }}'
AND hl7V2StoresId = '{{ hl7V2StoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
