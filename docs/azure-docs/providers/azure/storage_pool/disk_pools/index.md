---
title: disk_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_pools
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

Creates, updates, deletes, gets or lists a <code>disk_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.disk_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_pools', value: 'view', },
        { label: 'disk_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="additional_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zones" /> | `text` | field from the `properties` object |
| <CopyableCode code="diskPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives. |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by_extended" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku for ARM resource |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives. |
| <CopyableCode code="managedBy" /> | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| <CopyableCode code="managedByExtended" /> | `array` | List of Azure resource ids that manage this resource. |
| <CopyableCode code="properties" /> | `object` | Disk Pool response properties. |
| <CopyableCode code="sku" /> | `object` | Sku for ARM resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Get a Disk pool. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of DiskPools in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of Disk Pools in a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId, data__location, data__properties, data__sku" /> | Create or Update Disk pool. This create or update operation can take 15 minutes to complete. This is expected service behavior. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Delete a Disk pool; attached disks are not affected. This delete operation can take 10 minutes to complete. This is expected service behavior. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId, data__properties" /> | Update a Disk pool. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Shuts down the Disk Pool and releases the compute resources. You are not billed for the compute resources that this Disk Pool uses. This operation can take 10 minutes to complete. This is expected service behavior. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | The operation to start a Disk Pool. This start operation can take 10 minutes to complete. This is expected service behavior. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Upgrade replaces the underlying virtual machine hosts one at a time. This operation can take 10-15 minutes to complete. This is expected service behavior. |

## `SELECT` examples

Gets a list of Disk Pools in a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_pools', value: 'view', },
        { label: 'disk_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
additional_capabilities,
availability_zones,
diskPoolName,
disks,
location,
managed_by,
managed_by_extended,
provisioning_state,
resourceGroupName,
sku,
status,
subnet_id,
subscriptionId,
system_data,
tags
FROM azure.storage_pool.vw_disk_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
managedBy,
managedByExtended,
properties,
sku,
systemData,
tags
FROM azure.storage_pool.disk_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>disk_pools</code> resource.

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
INSERT INTO azure.storage_pool.disk_pools (
diskPoolName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
data__sku,
sku,
properties,
tags,
location,
managedBy,
managedByExtended
)
SELECT 
'{{ diskPoolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ managedBy }}',
'{{ managedByExtended }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: properties
      value:
        - name: availabilityZones
          value:
            - []
        - name: disks
          value:
            - - name: id
                value: string
        - name: subnetId
          value: string
        - name: additionalCapabilities
          value:
            - []
    - name: tags
      value: object
    - name: location
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: managedBy
      value: []
    - name: managedByExtended
      value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>disk_pools</code> resource.

```sql
/*+ update */
UPDATE azure.storage_pool.disk_pools
SET 
managedBy = '{{ managedBy }}',
managedByExtended = '{{ managedByExtended }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
diskPoolName = '{{ diskPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}';
```

## `DELETE` example

Deletes the specified <code>disk_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_pool.disk_pools
WHERE diskPoolName = '{{ diskPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
