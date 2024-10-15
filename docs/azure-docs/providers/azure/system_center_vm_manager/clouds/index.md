---
title: clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - clouds
  - system_center_vm_manager
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

Creates, updates, deletes, gets or lists a <code>clouds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.clouds" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clouds', value: 'view', },
        { label: 'clouds', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cloudResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="inventory_item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_qo_s_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmm_server_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudResourceName, resourceGroupName, subscriptionId" /> | Implements Cloud GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List of Clouds in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of Clouds in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudResourceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Onboards the ScVmm fabric cloud as an Azure cloud resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudResourceName, resourceGroupName, subscriptionId" /> | Deregisters the ScVmm fabric cloud from Azure. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="cloudResourceName, resourceGroupName, subscriptionId" /> | Updates the Clouds resource. |

## `SELECT` examples

List of Clouds in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clouds', value: 'view', },
        { label: 'clouds', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cloudResourceName,
cloud_capacity,
cloud_name,
extended_location,
inventory_item_id,
location,
provisioning_state,
resourceGroupName,
storage_qo_s_policies,
subscriptionId,
tags,
uuid,
vmm_server_id
FROM azure.system_center_vm_manager.vw_clouds
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.system_center_vm_manager.clouds
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clouds</code> resource.

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
INSERT INTO azure.system_center_vm_manager.clouds (
cloudResourceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ cloudResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: inventoryItemId
          value: string
        - name: uuid
          value: string
        - name: vmmServerId
          value: string
        - name: cloudName
          value: string
        - name: cloudCapacity
          value:
            - name: cpuCount
              value: integer
            - name: memoryMB
              value: integer
            - name: vmCount
              value: integer
        - name: storageQoSPolicies
          value:
            - - name: name
                value: string
              - name: id
                value: string
              - name: iopsMaximum
                value: integer
              - name: iopsMinimum
                value: integer
              - name: bandwidthLimit
                value: integer
              - name: policyId
                value: string
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clouds</code> resource.

```sql
/*+ update */
UPDATE azure.system_center_vm_manager.clouds
SET 
tags = '{{ tags }}'
WHERE 
cloudResourceName = '{{ cloudResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clouds</code> resource.

```sql
/*+ delete */
DELETE FROM azure.system_center_vm_manager.clouds
WHERE cloudResourceName = '{{ cloudResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
