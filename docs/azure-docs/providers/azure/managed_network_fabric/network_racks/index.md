---
title: network_racks
hide_title: false
hide_table_of_contents: false
keywords:
  - network_racks
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_racks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_racks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_racks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_racks', value: 'view', },
        { label: 'network_racks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="networkRackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_devices" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_rack_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Rack Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkRackName, resourceGroupName, subscriptionId" /> | Get Network Rack resource details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Network Rack resources in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Network Rack resources in the given subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkRackName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Create Network Rack resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkRackName, resourceGroupName, subscriptionId" /> | Delete Network Rack resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkRackName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Rack resource. |

## `SELECT` examples

List all Network Rack resources in the given subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_racks', value: 'view', },
        { label: 'network_racks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
annotation,
location,
networkRackName,
network_devices,
network_fabric_id,
network_rack_type,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_network_racks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.network_racks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_racks</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_racks (
networkRackName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ networkRackName }}',
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
    - name: properties
      value:
        - name: annotation
          value: string
        - name: networkRackType
          value: string
        - name: networkFabricId
          value: []
        - name: networkDevices
          value:
            - []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_racks</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_racks
SET 

WHERE 
networkRackName = '{{ networkRackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_racks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_racks
WHERE networkRackName = '{{ networkRackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
