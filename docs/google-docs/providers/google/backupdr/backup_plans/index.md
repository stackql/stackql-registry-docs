---
title: backup_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_plans
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

Creates, updates, deletes or gets an <code>backup_plan</code> resource or lists <code>backup_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.backup_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name of the `BackupPlan`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}` |
| <CopyableCode code="description" /> | `string` | Optional. The description of the `BackupPlan` resource. The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters. |
| <CopyableCode code="backupRules" /> | `array` | Required. The backup rules for this `BackupPlan`. There must be at least one `BackupRule` message. |
| <CopyableCode code="backupVault" /> | `string` | Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault} |
| <CopyableCode code="backupVaultServiceAccount" /> | `string` | Output only. The Google Cloud Platform Service Account to be used by the BackupVault for taking backups. Specify the email address of the Backup Vault Service Account. |
| <CopyableCode code="createTime" /> | `string` | Output only. When the `BackupPlan` was created. |
| <CopyableCode code="etag" /> | `string` | Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources. |
| <CopyableCode code="labels" /> | `object` | Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}. |
| <CopyableCode code="resourceType" /> | `string` | Required. The resource type to which the `BackupPlan` will be applied. Examples include, "compute.googleapis.com/Instance" and "storage.googleapis.com/Bucket". |
| <CopyableCode code="state" /> | `string` | Output only. The `State` for the `BackupPlan`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. When the `BackupPlan` was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupPlansId, locationsId, projectsId" /> | Gets details of a single BackupPlan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists BackupPlans in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a BackupPlan |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupPlansId, locationsId, projectsId" /> | Deletes a single BackupPlan. |

## `SELECT` examples

Lists BackupPlans in a given project and location.

```sql
SELECT
name,
description,
backupRules,
backupVault,
backupVaultServiceAccount,
createTime,
etag,
labels,
resourceType,
state,
updateTime
FROM google.backupdr.backup_plans
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_plans</code> resource.

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
INSERT INTO google.backupdr.backup_plans (
locationsId,
projectsId,
name,
description,
labels,
createTime,
updateTime,
backupRules,
state,
resourceType,
etag,
backupVault,
backupVaultServiceAccount
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ backupRules }}',
'{{ state }}',
'{{ resourceType }}',
'{{ etag }}',
'{{ backupVault }}',
'{{ backupVaultServiceAccount }}'
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
      - name: description
        value: '{{ description }}'
      - name: labels
        value: '{{ labels }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: backupRules
        value: '{{ backupRules }}'
      - name: state
        value: '{{ state }}'
      - name: resourceType
        value: '{{ resourceType }}'
      - name: etag
        value: '{{ etag }}'
      - name: backupVault
        value: '{{ backupVault }}'
      - name: backupVaultServiceAccount
        value: '{{ backupVaultServiceAccount }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified backup_plan resource.

```sql
DELETE FROM google.backupdr.backup_plans
WHERE backupPlansId = '{{ backupPlansId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
