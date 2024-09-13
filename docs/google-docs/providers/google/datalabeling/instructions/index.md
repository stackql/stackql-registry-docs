---
title: instructions
hide_title: false
hide_table_of_contents: false
keywords:
  - instructions
  - datalabeling
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

Creates, updates, deletes, gets or lists a <code>instructions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instructions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.instructions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Instruction resource name, format: projects/{project_id}/instructions/{instruction_id} |
| <CopyableCode code="description" /> | `string` | Optional. User-provided description of the instruction. The description can be up to 10000 characters long. |
| <CopyableCode code="blockingResources" /> | `array` | Output only. The names of any related resources that are blocking changes to the instruction. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of instruction. |
| <CopyableCode code="csvInstruction" /> | `object` | Deprecated: this instruction format is not supported any more. Instruction from a CSV file. |
| <CopyableCode code="dataType" /> | `string` | Required. The data type of this instruction. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the instruction. Maximum of 64 characters. |
| <CopyableCode code="pdfInstruction" /> | `object` | Instruction from a PDF file. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of instruction. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instructions_get" /> | `SELECT` | <CopyableCode code="instructionsId, projectsId" /> | Gets an instruction by resource name. |
| <CopyableCode code="projects_instructions_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists instructions for a project. Pagination is supported. |
| <CopyableCode code="projects_instructions_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an instruction for how data should be labeled. |
| <CopyableCode code="projects_instructions_delete" /> | `DELETE` | <CopyableCode code="instructionsId, projectsId" /> | Deletes an instruction object by resource name. |

## `SELECT` examples

Lists instructions for a project. Pagination is supported.

```sql
SELECT
name,
description,
blockingResources,
createTime,
csvInstruction,
dataType,
displayName,
pdfInstruction,
updateTime
FROM google.datalabeling.instructions
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instructions</code> resource.

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
INSERT INTO google.datalabeling.instructions (
projectsId,
instruction
)
SELECT 
'{{ projectsId }}',
'{{ instruction }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: instruction
        value: '{{ instruction }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>instructions</code> resource.

```sql
/*+ delete */
DELETE FROM google.datalabeling.instructions
WHERE instructionsId = '{{ instructionsId }}'
AND projectsId = '{{ projectsId }}';
```
