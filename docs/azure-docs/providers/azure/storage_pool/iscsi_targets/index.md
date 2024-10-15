---
title: iscsi_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_targets
  - storage_pool
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

Creates, updates, deletes, gets or lists a <code>iscsi_targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iscsi_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.iscsi_targets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iscsi_targets', value: 'view', },
        { label: 'iscsi_targets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="acl_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="diskPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="iscsiTargetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="luns" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by_extended" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sessions" /> | `text` | field from the `properties` object |
| <CopyableCode code="static_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_iqn" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| <CopyableCode code="managedByExtended" /> | `array` | List of Azure resource ids that manage this resource. |
| <CopyableCode code="properties" /> | `object` | Response properties for iSCSI Target operations. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId" /> | Get an iSCSI Target. |
| <CopyableCode code="list_by_disk_pool" /> | `SELECT` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Get iSCSI Targets in a Disk pool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId, data__properties" /> | Create or Update an iSCSI Target. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId" /> | Delete an iSCSI Target. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId, data__properties" /> | Update an iSCSI Target. |

## `SELECT` examples

Get iSCSI Targets in a Disk pool.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iscsi_targets', value: 'view', },
        { label: 'iscsi_targets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
acl_mode,
diskPoolName,
endpoints,
iscsiTargetName,
luns,
managed_by,
managed_by_extended,
port,
provisioning_state,
resourceGroupName,
sessions,
static_acls,
status,
subscriptionId,
system_data,
target_iqn
FROM azure.storage_pool.vw_iscsi_targets
WHERE diskPoolName = '{{ diskPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
managedBy,
managedByExtended,
properties,
systemData
FROM azure.storage_pool.iscsi_targets
WHERE diskPoolName = '{{ diskPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iscsi_targets</code> resource.

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
INSERT INTO azure.storage_pool.iscsi_targets (
diskPoolName,
iscsiTargetName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
managedBy,
managedByExtended
)
SELECT 
'{{ diskPoolName }}',
'{{ iscsiTargetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ managedBy }}',
'{{ managedByExtended }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: aclMode
          value: []
        - name: targetIqn
          value: string
        - name: staticAcls
          value:
            - - name: initiatorIqn
                value: string
              - name: mappedLuns
                value:
                  - string
        - name: luns
          value:
            - - name: name
                value: string
              - name: managedDiskAzureResourceId
                value: string
              - name: lun
                value: integer
    - name: managedBy
      value: []
    - name: managedByExtended
      value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>iscsi_targets</code> resource.

```sql
/*+ update */
UPDATE azure.storage_pool.iscsi_targets
SET 
properties = '{{ properties }}',
managedBy = '{{ managedBy }}',
managedByExtended = '{{ managedByExtended }}'
WHERE 
diskPoolName = '{{ diskPoolName }}'
AND iscsiTargetName = '{{ iscsiTargetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}';
```

## `DELETE` example

Deletes the specified <code>iscsi_targets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_pool.iscsi_targets
WHERE diskPoolName = '{{ diskPoolName }}'
AND iscsiTargetName = '{{ iscsiTargetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
