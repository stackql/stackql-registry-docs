---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - metastore
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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.metastore.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The relative resource name of the backup, in the following form:projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id} |
| <CopyableCode code="description" /> | `string` | The description of the backup. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the backup was started. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time when the backup finished creating. |
| <CopyableCode code="restoringServices" /> | `array` | Output only. Services that are restoring from the backup. |
| <CopyableCode code="serviceRevision" /> | `object` | A managed metastore service that serves metadata queries. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, locationsId, projectsId, servicesId" /> | Gets details of a single backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists backups in a service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Creates a new backup in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, locationsId, projectsId, servicesId" /> | Deletes a single backup. |

## `SELECT` examples

Lists backups in a service.

```sql
SELECT
name,
description,
createTime,
endTime,
restoringServices,
serviceRevision,
state
FROM google.metastore.backups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backups</code> resource.

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
INSERT INTO google.metastore.backups (
locationsId,
projectsId,
servicesId,
name,
createTime,
endTime,
state,
serviceRevision,
description,
restoringServices
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ servicesId }}',
'{{ name }}',
'{{ createTime }}',
'{{ endTime }}',
'{{ state }}',
'{{ serviceRevision }}',
'{{ description }}',
'{{ restoringServices }}'
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
      - name: createTime
        value: '{{ createTime }}'
      - name: endTime
        value: '{{ endTime }}'
      - name: state
        value: '{{ state }}'
      - name: serviceRevision
        value: '{{ serviceRevision }}'
      - name: description
        value: '{{ description }}'
      - name: restoringServices
        value: '{{ restoringServices }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM google.metastore.backups
WHERE backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
