---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - migrationcenter
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

Creates, updates, deletes, gets or lists a <code>sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the source. |
| <CopyableCode code="description" /> | `string` | Free-text description. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the source was created. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. |
| <CopyableCode code="errorFrameCount" /> | `integer` | Output only. The number of frames that were reported by the source and contained errors. |
| <CopyableCode code="managed" /> | `boolean` | If `true`, the source is managed by other service(s). |
| <CopyableCode code="pendingFrameCount" /> | `integer` | Output only. Number of frames that are still being processed. |
| <CopyableCode code="priority" /> | `integer` | The information confidence of the source. The higher the value, the higher the confidence. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the source. |
| <CopyableCode code="type" /> | `string` | Data source type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the source was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Gets the details of a source. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the sources in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new source in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Deletes a source. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Updates the parameters of a source. |

## `SELECT` examples

Lists all the sources in a given project and location.

```sql
SELECT
name,
description,
createTime,
displayName,
errorFrameCount,
managed,
pendingFrameCount,
priority,
state,
type,
updateTime
FROM google.migrationcenter.sources
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sources</code> resource.

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
INSERT INTO google.migrationcenter.sources (
locationsId,
projectsId,
displayName,
description,
type,
priority,
managed
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ description }}',
'{{ type }}',
'{{ priority }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'
    - name: type
      value: '{{ type }}'
    - name: priority
      value: '{{ priority }}'
    - name: managed
      value: '{{ managed }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sources</code> resource.

```sql
/*+ update */
UPDATE google.migrationcenter.sources
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
type = '{{ type }}',
priority = '{{ priority }}',
managed = true|false
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```

## `DELETE` example

Deletes the specified <code>sources</code> resource.

```sql
/*+ delete */
DELETE FROM google.migrationcenter.sources
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```
