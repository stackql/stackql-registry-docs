---
title: log_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - log_scopes
  - logging
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

Creates, updates, deletes, gets or lists a <code>log_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.log_scopes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the log scope.For example:projects/my-project/locations/global/logScopes/my-log-scope |
| <CopyableCode code="description" /> | `string` | Optional. Describes this log scope.The maximum length of the description is 8000 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of the log scope. |
| <CopyableCode code="resourceNames" /> | `array` | Required. Names of one or more parent resources: projects/[PROJECT_ID]May alternatively be one or more views: projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]A log scope can include a maximum of 50 projects and a maximum of 100 resources in total. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of the log scope. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_locations_log_scopes_get" /> | `SELECT` | <CopyableCode code="foldersId, locationsId, logScopesId" /> | Gets a log scope. |
| <CopyableCode code="folders_locations_log_scopes_list" /> | `SELECT` | <CopyableCode code="foldersId, locationsId" /> | Lists log scopes. |
| <CopyableCode code="organizations_locations_log_scopes_get" /> | `SELECT` | <CopyableCode code="locationsId, logScopesId, organizationsId" /> | Gets a log scope. |
| <CopyableCode code="organizations_locations_log_scopes_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists log scopes. |
| <CopyableCode code="projects_locations_log_scopes_get" /> | `SELECT` | <CopyableCode code="locationsId, logScopesId, projectsId" /> | Gets a log scope. |
| <CopyableCode code="projects_locations_log_scopes_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists log scopes. |
| <CopyableCode code="folders_locations_log_scopes_create" /> | `INSERT` | <CopyableCode code="foldersId, locationsId" /> | Creates a log scope. |
| <CopyableCode code="organizations_locations_log_scopes_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a log scope. |
| <CopyableCode code="projects_locations_log_scopes_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a log scope. |
| <CopyableCode code="folders_locations_log_scopes_delete" /> | `DELETE` | <CopyableCode code="foldersId, locationsId, logScopesId" /> | Deletes a log scope. |
| <CopyableCode code="organizations_locations_log_scopes_delete" /> | `DELETE` | <CopyableCode code="locationsId, logScopesId, organizationsId" /> | Deletes a log scope. |
| <CopyableCode code="projects_locations_log_scopes_delete" /> | `DELETE` | <CopyableCode code="locationsId, logScopesId, projectsId" /> | Deletes a log scope. |
| <CopyableCode code="folders_locations_log_scopes_patch" /> | `UPDATE` | <CopyableCode code="foldersId, locationsId, logScopesId" /> | Updates a log scope. |
| <CopyableCode code="organizations_locations_log_scopes_patch" /> | `UPDATE` | <CopyableCode code="locationsId, logScopesId, organizationsId" /> | Updates a log scope. |
| <CopyableCode code="projects_locations_log_scopes_patch" /> | `UPDATE` | <CopyableCode code="locationsId, logScopesId, projectsId" /> | Updates a log scope. |

## `SELECT` examples

Lists log scopes.

```sql
SELECT
name,
description,
createTime,
resourceNames,
updateTime
FROM google.logging.log_scopes
WHERE foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>log_scopes</code> resource.

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
INSERT INTO google.logging.log_scopes (
foldersId,
locationsId,
name,
resourceNames,
description,
createTime,
updateTime
)
SELECT 
'{{ foldersId }}',
'{{ locationsId }}',
'{{ name }}',
'{{ resourceNames }}',
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
    - name: resourceNames
      value: '{{ resourceNames }}'
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

Updates a <code>log_scopes</code> resource.

```sql
/*+ update */
UPDATE google.logging.log_scopes
SET 
name = '{{ name }}',
resourceNames = '{{ resourceNames }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}'
WHERE 
foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'
AND logScopesId = '{{ logScopesId }}';
```

## `DELETE` example

Deletes the specified <code>log_scopes</code> resource.

```sql
/*+ delete */
DELETE FROM google.logging.log_scopes
WHERE foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'
AND logScopesId = '{{ logScopesId }}';
```
