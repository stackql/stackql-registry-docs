---
title: target_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - target_projects
  - vmmigration
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

Creates, updates, deletes, gets or lists a <code>target_projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.target_projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the target project. |
| <CopyableCode code="description" /> | `string` | The target project's description. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time this target project resource was created (not related to when the Compute Engine project it points to was created). |
| <CopyableCode code="project" /> | `string` | Required. The target project ID (number) or project name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time the target project resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, targetProjectsId" /> | Gets details of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists TargetProjects in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new TargetProject in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, targetProjectsId" /> | Deletes a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, targetProjectsId" /> | Updates the parameters of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |

## `SELECT` examples

Lists TargetProjects in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`.

```sql
SELECT
name,
description,
createTime,
project,
updateTime
FROM google.vmmigration.target_projects
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_projects</code> resource.

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
INSERT INTO google.vmmigration.target_projects (
locationsId,
projectsId,
name,
project,
description,
createTime,
updateTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ project }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: project
      value: '{{ project }}'
    - name: description
      value: '{{ description }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>target_projects</code> resource.

```sql
/*+ update */
UPDATE google.vmmigration.target_projects
SET 
name = '{{ name }}',
project = '{{ project }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND targetProjectsId = '{{ targetProjectsId }}';
```

## `DELETE` example

Deletes the specified <code>target_projects</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmmigration.target_projects
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND targetProjectsId = '{{ targetProjectsId }}';
```
