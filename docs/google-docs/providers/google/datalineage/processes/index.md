---
title: processes
hide_title: false
hide_table_of_contents: false
keywords:
  - processes
  - datalineage
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

Creates, updates, deletes, gets or lists a <code>processes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalineage.processes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the lineage process. Format: `projects/{project}/locations/{location}/processes/{process}`. Can be specified or auto-assigned. {process} must be not longer than 200 characters and only contain characters in a set: `a-zA-Z0-9_-:.` |
| <CopyableCode code="attributes" /> | `object` | Optional. The attributes of the process. Should only be used for the purpose of non-semantic management (classifying, describing or labeling the process). Up to 100 attributes are allowed. |
| <CopyableCode code="displayName" /> | `string` | Optional. A human-readable name you can set to display in a user interface. Must be not longer than 200 characters and only contain UTF-8 letters or numbers, spaces or characters like `_-:&.` |
| <CopyableCode code="origin" /> | `object` | Origin of a process. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, processesId, projectsId" /> | Gets the details of the specified process. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List processes in the given project and location. List order is descending by insertion time. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new process. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, processesId, projectsId" /> | Deletes the process with the specified name. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, processesId, projectsId" /> | Updates a process. |

## `SELECT` examples

List processes in the given project and location. List order is descending by insertion time.

```sql
SELECT
name,
attributes,
displayName,
origin
FROM google.datalineage.processes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>processes</code> resource.

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
INSERT INTO google.datalineage.processes (
locationsId,
projectsId,
name,
displayName,
origin,
attributes
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ origin }}',
'{{ attributes }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: origin
        value: '{{ origin }}'
      - name: attributes
        value: '{{ attributes }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>processes</code> resource.

```sql
/*+ update */
UPDATE google.datalineage.processes
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
origin = '{{ origin }}',
attributes = '{{ attributes }}'
WHERE 
locationsId = '{{ locationsId }}'
AND processesId = '{{ processesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>processes</code> resource.

```sql
/*+ delete */
DELETE FROM google.datalineage.processes
WHERE locationsId = '{{ locationsId }}'
AND processesId = '{{ processesId }}'
AND projectsId = '{{ projectsId }}';
```
