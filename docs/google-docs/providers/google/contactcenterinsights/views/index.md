---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - contactcenterinsights
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

Creates, updates, deletes, gets or lists a <code>views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the view. Format: projects/{project}/locations/{location}/views/{view} |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this view was created. |
| <CopyableCode code="displayName" /> | `string` | The human-readable display name of the view. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time at which the view was updated. |
| <CopyableCode code="value" /> | `string` | String with specific view properties, must be non-empty. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, viewsId" /> | Gets a view. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists views. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a view. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, viewsId" /> | Deletes a view. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, viewsId" /> | Updates a view. |

## `SELECT` examples

Lists views.

```sql
SELECT
name,
createTime,
displayName,
updateTime,
value
FROM google.contactcenterinsights.views
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>views</code> resource.

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
INSERT INTO google.contactcenterinsights.views (
locationsId,
projectsId,
value,
name,
displayName,
createTime,
updateTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ value }}',
'{{ name }}',
'{{ displayName }}',
'{{ createTime }}',
'{{ updateTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: value
        value: '{{ value }}'
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>views</code> resource.

```sql
/*+ update */
UPDATE google.contactcenterinsights.views
SET 
value = '{{ value }}',
name = '{{ name }}',
displayName = '{{ displayName }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND viewsId = '{{ viewsId }}';
```

## `DELETE` example

Deletes the specified <code>views</code> resource.

```sql
/*+ delete */
DELETE FROM google.contactcenterinsights.views
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND viewsId = '{{ viewsId }}';
```
