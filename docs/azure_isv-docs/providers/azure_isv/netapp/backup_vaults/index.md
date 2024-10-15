---
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
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

Creates, updates, deletes, gets or lists a <code>backup_vaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.backup_vaults" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_vaults', value: 'view', },
        { label: 'backup_vaults', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backupVaultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Backup Vault properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId" /> | Get the Backup Vault |
| <CopyableCode code="list_by_netapp_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List and describe all Backup Vaults in the NetApp account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId, data__location" /> | Create or update the specified Backup Vault in the NetApp account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId" /> | Delete the specified Backup Vault |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId" /> | Patch the specified NetApp Backup Vault |

## `SELECT` examples

List and describe all Backup Vaults in the NetApp account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_vaults', value: 'view', },
        { label: 'backup_vaults', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
backupVaultName,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure_isv.netapp.vw_backup_vaults
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_isv.netapp.backup_vaults
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_vaults</code> resource.

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
INSERT INTO azure_isv.netapp.backup_vaults (
accountName,
backupVaultName,
resourceGroupName,
subscriptionId,
data__location,
tags,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ backupVaultName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backup_vaults</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.backup_vaults
SET 
tags = '{{ tags }}'
WHERE 
accountName = '{{ accountName }}'
AND backupVaultName = '{{ backupVaultName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>backup_vaults</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.backup_vaults
WHERE accountName = '{{ accountName }}'
AND backupVaultName = '{{ backupVaultName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
