---
title: neighbor_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - neighbor_groups
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

Creates, updates, deletes, gets or lists a <code>neighbor_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>neighbor_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.neighbor_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_neighbor_groups', value: 'view', },
        { label: 'neighbor_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="neighborGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_tap_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_tap_rule_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Neighbor Group Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="neighborGroupName, resourceGroupName, subscriptionId" /> | Gets the Neighbor Group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays NeighborGroups list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays NeighborGroups list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="neighborGroupName, resourceGroupName, subscriptionId, data__properties" /> | Implements the Neighbor Group PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="neighborGroupName, resourceGroupName, subscriptionId" /> | Implements Neighbor Group DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="neighborGroupName, resourceGroupName, subscriptionId" /> | Updates the Neighbor Group. |

## `SELECT` examples

Displays NeighborGroups list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_neighbor_groups', value: 'view', },
        { label: 'neighbor_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
annotation,
destination,
location,
neighborGroupName,
network_tap_ids,
network_tap_rule_ids,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_neighbor_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.neighbor_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>neighbor_groups</code> resource.

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
INSERT INTO azure.managed_network_fabric.neighbor_groups (
neighborGroupName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ neighborGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: destination
          value:
            - name: ipv4Addresses
              value:
                - string
            - name: ipv6Addresses
              value:
                - string
        - name: networkTapIds
          value:
            - []
        - name: networkTapRuleIds
          value:
            - []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>neighbor_groups</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.neighbor_groups
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
neighborGroupName = '{{ neighborGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>neighbor_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.neighbor_groups
WHERE neighborGroupName = '{{ neighborGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
