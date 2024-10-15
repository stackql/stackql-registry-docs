---
title: dedicated_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hosts
  - compute
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

Creates, updates, deletes, gets or lists a <code>dedicated_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.dedicated_hosts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_hosts', value: 'view', },
        { label: 'dedicated_hosts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="auto_replace_on_failure" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostName" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="platform_fault_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="virtual_machines" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the dedicated host. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Retrieves information about a dedicated host. |
| <CopyableCode code="list_by_host_group" /> | `SELECT` | <CopyableCode code="hostGroupName, resourceGroupName, subscriptionId" /> | Lists all of the dedicated hosts in the specified dedicated host group. Use the nextLink property in the response to get the next page of dedicated hosts. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId, data__sku" /> | Create or update a dedicated host . |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Delete a dedicated host. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Update a dedicated host . |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Redeploy the dedicated host. The operation will complete successfully once the dedicated host has migrated to a new node and is running. To determine the health of VMs deployed on the dedicated host after the redeploy check the Resource Health Center in the Azure Portal. Please refer to https://docs.microsoft.com/azure/service-health/resource-health-overview for more details. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Restart the dedicated host. The operation will complete successfully once the dedicated host has restarted and is running. To determine the health of VMs deployed on the dedicated host after the restart check the Resource Health Center in the Azure Portal. Please refer to https://docs.microsoft.com/azure/service-health/resource-health-overview for more details. |

## `SELECT` examples

Lists all of the dedicated hosts in the specified dedicated host group. Use the nextLink property in the response to get the next page of dedicated hosts.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_hosts', value: 'view', },
        { label: 'dedicated_hosts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
auto_replace_on_failure,
hostGroupName,
hostName,
host_id,
instance_view,
license_type,
location,
platform_fault_domain,
provisioning_state,
provisioning_time,
resourceGroupName,
sku,
subscriptionId,
tags,
time_created,
type,
virtual_machines
FROM azure.compute.vw_dedicated_hosts
WHERE hostGroupName = '{{ hostGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
sku,
tags,
type
FROM azure.compute.dedicated_hosts
WHERE hostGroupName = '{{ hostGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dedicated_hosts</code> resource.

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
INSERT INTO azure.compute.dedicated_hosts (
hostGroupName,
hostName,
resourceGroupName,
subscriptionId,
data__sku,
properties,
sku,
location,
tags
)
SELECT 
'{{ hostGroupName }}',
'{{ hostName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ properties }}',
'{{ sku }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: platformFaultDomain
          value: integer
        - name: autoReplaceOnFailure
          value: boolean
        - name: hostId
          value: string
        - name: virtualMachines
          value:
            - - name: id
                value: string
        - name: licenseType
          value: []
        - name: provisioningTime
          value: string
        - name: provisioningState
          value: string
        - name: instanceView
          value:
            - name: assetId
              value: string
            - name: availableCapacity
              value:
                - name: allocatableVMs
                  value:
                    - - name: vmSize
                        value: string
                      - name: count
                        value: number
            - name: statuses
              value:
                - - name: code
                    value: string
                  - name: level
                    value: string
                  - name: displayStatus
                    value: string
                  - name: message
                    value: string
                  - name: time
                    value: string
        - name: timeCreated
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dedicated_hosts</code> resource.

```sql
/*+ update */
UPDATE azure.compute.dedicated_hosts
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
hostGroupName = '{{ hostGroupName }}'
AND hostName = '{{ hostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dedicated_hosts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.dedicated_hosts
WHERE hostGroupName = '{{ hostGroupName }}'
AND hostName = '{{ hostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
