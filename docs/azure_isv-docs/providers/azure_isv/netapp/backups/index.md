---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - netapp
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.backups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backups', value: 'view', },
        { label: 'backups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backupVaultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_policy_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="failure_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="label" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshot_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_existing_snapshot" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Backup properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, backupName, backupVaultName, resourceGroupName, subscriptionId" /> | Get the specified Backup under Backup Vault. |
| <CopyableCode code="list_by_vault" /> | `SELECT` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId" /> | List all backups Under a Backup Vault |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, backupName, backupVaultName, resourceGroupName, subscriptionId, data__properties" /> | Create a backup under the Backup Vault |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, backupName, backupVaultName, resourceGroupName, subscriptionId" /> | Delete a Backup under the Backup Vault |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, backupName, backupVaultName, resourceGroupName, subscriptionId" /> | Patch a Backup under the Backup Vault |

## `SELECT` examples

List all backups Under a Backup Vault

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backups', value: 'view', },
        { label: 'backups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
backupName,
backupVaultName,
backup_id,
backup_policy_resource_id,
backup_type,
creation_date,
failure_reason,
label,
provisioning_state,
resourceGroupName,
size,
snapshot_name,
subscriptionId,
use_existing_snapshot,
volume_resource_id
FROM azure_isv.netapp.vw_backups
WHERE accountName = '{{ accountName }}'
AND backupVaultName = '{{ backupVaultName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.netapp.backups
WHERE accountName = '{{ accountName }}'
AND backupVaultName = '{{ backupVaultName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


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
INSERT INTO azure_isv.netapp.backups (
accountName,
backupName,
backupVaultName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ backupName }}',
'{{ backupVaultName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: backupId
          value: string
        - name: creationDate
          value: string
        - name: provisioningState
          value: string
        - name: size
          value: integer
        - name: label
          value: string
        - name: backupType
          value: string
        - name: failureReason
          value: string
        - name: volumeResourceId
          value: string
        - name: useExistingSnapshot
          value: boolean
        - name: snapshotName
          value: string
        - name: backupPolicyResourceId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backups</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.backups
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND backupName = '{{ backupName }}'
AND backupVaultName = '{{ backupVaultName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.backups
WHERE accountName = '{{ accountName }}'
AND backupName = '{{ backupName }}'
AND backupVaultName = '{{ backupVaultName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
