---
title: backup_plan_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_plan_associations
  - backupdr
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

Creates, updates, deletes, gets or lists a <code>backup_plan_associations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_plan_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.backup_plan_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId} |
| <CopyableCode code="backupPlan" /> | `string` | Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId} |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created. |
| <CopyableCode code="dataSource" /> | `string` | Output only. Output Only. Resource name of data source which will be used as storage location for backups taken. Format : projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource} |
| <CopyableCode code="resource" /> | `string` | Required. Immutable. Resource name of workload on which backupplan is applied |
| <CopyableCode code="resourceType" /> | `string` | Output only. Output Only. Resource type of workload on which backupplan is applied |
| <CopyableCode code="rulesConfigInfo" /> | `array` | Output only. The config info related to backup rules. |
| <CopyableCode code="state" /> | `string` | Output only. The BackupPlanAssociation resource state. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the instance was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupPlanAssociationsId, locationsId, projectsId" /> | Gets details of a single BackupPlanAssociation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists BackupPlanAssociations in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a BackupPlanAssociation |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupPlanAssociationsId, locationsId, projectsId" /> | Deletes a single BackupPlanAssociation. |
| <CopyableCode code="trigger_backup" /> | `EXEC` | <CopyableCode code="backupPlanAssociationsId, locationsId, projectsId" /> | Triggers a new Backup. |

## `SELECT` examples

Lists BackupPlanAssociations in a given project and location.

```sql
SELECT
name,
backupPlan,
createTime,
dataSource,
resource,
resourceType,
rulesConfigInfo,
state,
updateTime
FROM google.backupdr.backup_plan_associations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_plan_associations</code> resource.

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
INSERT INTO google.backupdr.backup_plan_associations (
locationsId,
projectsId,
resource,
backupPlan
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ resource }}',
'{{ backupPlan }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: resource
      value: '{{ resource }}'
    - name: backupPlan
      value: '{{ backupPlan }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backup_plan_associations</code> resource.

```sql
/*+ delete */
DELETE FROM google.backupdr.backup_plan_associations
WHERE backupPlanAssociationsId = '{{ backupPlanAssociationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
