---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - dataplex
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

Creates, updates, deletes or gets an <code>environment</code> resource or lists <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the environment, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id} |
| <CopyableCode code="description" /> | `string` | Optional. Description of the environment. |
| <CopyableCode code="createTime" /> | `string` | Output only. Environment creation time. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="endpoints" /> | `object` | URI Endpoints to access sessions associated with the Environment. |
| <CopyableCode code="infrastructureSpec" /> | `object` | Configuration for the underlying infrastructure used to run workloads. |
| <CopyableCode code="labels" /> | `object` | Optional. User defined labels for the environment. |
| <CopyableCode code="sessionSpec" /> | `object` | Configuration for sessions created for this environment. |
| <CopyableCode code="sessionStatus" /> | `object` | Status of sessions created for this environment. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the environment. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the environment. This ID will be different if the environment is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the environment was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_environments_get" /> | `SELECT` | <CopyableCode code="environmentsId, lakesId, locationsId, projectsId" /> | Get environment resource. |
| <CopyableCode code="projects_locations_lakes_environments_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Lists environments under the given lake. |
| <CopyableCode code="projects_locations_lakes_environments_create" /> | `INSERT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Create an environment resource. |
| <CopyableCode code="projects_locations_lakes_environments_delete" /> | `DELETE` | <CopyableCode code="environmentsId, lakesId, locationsId, projectsId" /> | Delete the environment resource. All the child resources must have been deleted before environment deletion can be initiated. |
| <CopyableCode code="projects_locations_lakes_environments_patch" /> | `UPDATE` | <CopyableCode code="environmentsId, lakesId, locationsId, projectsId" /> | Update the environment resource. |

## `SELECT` examples

Lists environments under the given lake.

```sql
SELECT
name,
description,
createTime,
displayName,
endpoints,
infrastructureSpec,
labels,
sessionSpec,
sessionStatus,
state,
uid,
updateTime
FROM google.dataplex.environments
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments</code> resource.

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
INSERT INTO google.dataplex.environments (
lakesId,
locationsId,
projectsId,
name,
displayName,
uid,
createTime,
updateTime,
labels,
description,
state,
infrastructureSpec,
sessionSpec,
sessionStatus,
endpoints
)
SELECT 
'{{ lakesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ state }}',
'{{ infrastructureSpec }}',
'{{ sessionSpec }}',
'{{ sessionStatus }}',
'{{ endpoints }}'
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
      - name: uid
        value: '{{ uid }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: description
        value: '{{ description }}'
      - name: state
        value: '{{ state }}'
      - name: infrastructureSpec
        value: '{{ infrastructureSpec }}'
      - name: sessionSpec
        value: '{{ sessionSpec }}'
      - name: sessionStatus
        value: '{{ sessionStatus }}'
      - name: endpoints
        value: '{{ endpoints }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a environment only if the necessary resources are available.

```sql
UPDATE google.dataplex.environments
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
state = '{{ state }}',
infrastructureSpec = '{{ infrastructureSpec }}',
sessionSpec = '{{ sessionSpec }}',
sessionStatus = '{{ sessionStatus }}',
endpoints = '{{ endpoints }}'
WHERE 
environmentsId = '{{ environmentsId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified environment resource.

```sql
DELETE FROM google.dataplex.environments
WHERE environmentsId = '{{ environmentsId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
