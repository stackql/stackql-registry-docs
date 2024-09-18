---
title: processors
hide_title: false
hide_table_of_contents: false
keywords:
  - processors
  - documentai
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

Creates, updates, deletes, gets or lists a <code>processors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>processors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.documentai.processors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Immutable. The resource name of the processor. Format: `projects/{project}/locations/{location}/processors/{processor}` |
| <CopyableCode code="createTime" /> | `string` | The time the processor was created. |
| <CopyableCode code="defaultProcessorVersion" /> | `string` | The default processor version. |
| <CopyableCode code="displayName" /> | `string` | The display name of the processor. |
| <CopyableCode code="kmsKeyName" /> | `string` | The [KMS key](https://cloud.google.com/security-key-management) used for encryption and decryption in CMEK scenarios. |
| <CopyableCode code="processEndpoint" /> | `string` | Output only. Immutable. The http endpoint that can be called to invoke processing. |
| <CopyableCode code="processorVersionAliases" /> | `array` | Output only. The processor version aliases. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the processor. |
| <CopyableCode code="type" /> | `string` | The processor type, such as: `OCR_PROCESSOR`, `INVOICE_PROCESSOR`. To get a list of processor types, see FetchProcessorTypes. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_processors_get" /> | `SELECT` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Gets a processor detail. |
| <CopyableCode code="projects_locations_processors_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all processors which belong to this project. |
| <CopyableCode code="projects_locations_processors_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a processor from the ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. Note that this method requires the `documentai.processors.create` permission on the project, which is highly privileged. A user or service account with this permission can create new processors that can interact with any gcs bucket in your project. |
| <CopyableCode code="projects_locations_processors_delete" /> | `DELETE` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor. |
| <CopyableCode code="projects_locations_processors_batch_process" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |
| <CopyableCode code="projects_locations_processors_disable" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Disables a processor |
| <CopyableCode code="projects_locations_processors_enable" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Enables a processor |
| <CopyableCode code="projects_locations_processors_process" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Processes a single document. |
| <CopyableCode code="projects_locations_processors_set_default_processor_version" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Set the default (active) version of a Processor that will be used in ProcessDocument and BatchProcessDocuments. |

## `SELECT` examples

Lists all processors which belong to this project.

```sql
SELECT
name,
createTime,
defaultProcessorVersion,
displayName,
kmsKeyName,
processEndpoint,
processorVersionAliases,
satisfiesPzi,
satisfiesPzs,
state,
type
FROM google.documentai.processors
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>processors</code> resource.

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
INSERT INTO google.documentai.processors (
locationsId,
projectsId,
defaultProcessorVersion,
displayName,
kmsKeyName,
type
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ defaultProcessorVersion }}',
'{{ displayName }}',
'{{ kmsKeyName }}',
'{{ type }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
state: string
createTime: string
defaultProcessorVersion: string
processorVersionAliases:
  - processorVersion: string
    alias: string
satisfiesPzs: boolean
displayName: string
processEndpoint: string
kmsKeyName: string
satisfiesPzi: boolean
name: string
type: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>processors</code> resource.

```sql
/*+ delete */
DELETE FROM google.documentai.processors
WHERE locationsId = '{{ locationsId }}'
AND processorsId = '{{ processorsId }}'
AND projectsId = '{{ projectsId }}';
```
