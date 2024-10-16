---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - managedidentities
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.managedidentities.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The unique name of the Backup in the form of `projects/{project_id}/locations/global/domains/{domain_name}/backups/{name}` |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the backups was created. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user provided metadata. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |
| <CopyableCode code="statusMessage" /> | `string` | Output only. Additional information about the current status of this backup, if available. |
| <CopyableCode code="type" /> | `string` | Output only. Indicates whether it’s an on-demand backup or scheduled. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, domainsId, projectsId" /> | Gets details of a single Backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainsId, projectsId" /> | Lists Backup in a given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="domainsId, projectsId" /> | Creates a Backup for a domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, domainsId, projectsId" /> | Deletes identified Backup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupsId, domainsId, projectsId" /> | Updates the labels for specified Backup. |

## `SELECT` examples

Lists Backup in a given project.

```sql
SELECT
name,
createTime,
labels,
state,
statusMessage,
type,
updateTime
FROM google.managedidentities.backups
WHERE domainsId = '{{ domainsId }}'
AND projectsId = '{{ projectsId }}';
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
INSERT INTO google.managedidentities.backups (
domainsId,
projectsId,
labels
)
SELECT 
'{{ domainsId }}',
'{{ projectsId }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: labels
      value: object
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: type
      value: string
    - name: state
      value: string
    - name: statusMessage
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backups</code> resource.

```sql
/*+ update */
UPDATE google.managedidentities.backups
SET 
labels = '{{ labels }}'
WHERE 
backupsId = '{{ backupsId }}'
AND domainsId = '{{ domainsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM google.managedidentities.backups
WHERE backupsId = '{{ backupsId }}'
AND domainsId = '{{ domainsId }}'
AND projectsId = '{{ projectsId }}';
```
