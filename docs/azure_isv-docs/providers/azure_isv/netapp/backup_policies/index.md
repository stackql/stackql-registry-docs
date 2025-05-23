---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
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

Creates, updates, deletes, gets or lists a <code>backup_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.backup_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_policies', value: 'view', },
        { label: 'backup_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backupPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="daily_backups_to_keep" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="monthly_backups_to_keep" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="volume_backups" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumes_assigned" /> | `text` | field from the `properties` object |
| <CopyableCode code="weekly_backups_to_keep" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Backup policy properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, backupPolicyName, resourceGroupName, subscriptionId" /> | Get a particular backup Policy |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List backup policies for Netapp Account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, backupPolicyName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Create a backup policy for Netapp Account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, backupPolicyName, resourceGroupName, subscriptionId" /> | Delete backup policy |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, backupPolicyName, resourceGroupName, subscriptionId" /> | Patch a backup policy for Netapp Account |

## `SELECT` examples

List backup policies for Netapp Account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_policies', value: 'view', },
        { label: 'backup_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
backupPolicyName,
backup_policy_id,
daily_backups_to_keep,
enabled,
etag,
location,
monthly_backups_to_keep,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
volume_backups,
volumes_assigned,
weekly_backups_to_keep
FROM azure_isv.netapp.vw_backup_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure_isv.netapp.backup_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_policies</code> resource.

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
INSERT INTO azure_isv.netapp.backup_policies (
accountName,
backupPolicyName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ backupPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
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
    - name: etag
      value: string
    - name: properties
      value:
        - name: backupPolicyId
          value: string
        - name: provisioningState
          value: string
        - name: dailyBackupsToKeep
          value: integer
        - name: weeklyBackupsToKeep
          value: integer
        - name: monthlyBackupsToKeep
          value: integer
        - name: volumesAssigned
          value: integer
        - name: enabled
          value: boolean
        - name: volumeBackups
          value:
            - - name: volumeName
                value: string
              - name: volumeResourceId
                value: string
              - name: backupsCount
                value: integer
              - name: policyEnabled
                value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backup_policies</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.backup_policies
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND backupPolicyName = '{{ backupPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>backup_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.backup_policies
WHERE accountName = '{{ accountName }}'
AND backupPolicyName = '{{ backupPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
