---
title: inventory_items
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_items
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

Creates, updates, deletes, gets or lists a <code>inventory_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inventory_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.inventory_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_inventory_items', value: 'view', },
        { label: 'inventory_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="inventoryItemResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="inventory_item_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="inventory_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="managed_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmmServerName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName" /> | Shows an inventory item. |
| <CopyableCode code="list_by_vmm_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmmServerName" /> | Returns the list of inventoryItems in the given VmmServer. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName" /> | Create Or Update InventoryItem. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName" /> | Deletes an inventoryItem. |

## `SELECT` examples

Returns the list of inventoryItems in the given VmmServer.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_inventory_items', value: 'view', },
        { label: 'inventory_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
inventoryItemResourceName,
inventory_item_name,
inventory_type,
kind,
managed_resource_id,
provisioning_state,
resourceGroupName,
subscriptionId,
uuid,
vmmServerName
FROM azure.system_center_vm_manager.vw_inventory_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmmServerName = '{{ vmmServerName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
properties
FROM azure.system_center_vm_manager.inventory_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmmServerName = '{{ vmmServerName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>inventory_items</code> resource.

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
INSERT INTO azure.system_center_vm_manager.inventory_items (
inventoryItemResourceName,
resourceGroupName,
subscriptionId,
vmmServerName,
properties,
kind
)
SELECT 
'{{ inventoryItemResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vmmServerName }}',
'{{ properties }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: inventoryType
          value: []
        - name: managedResourceId
          value: string
        - name: uuid
          value: string
        - name: inventoryItemName
          value: string
        - name: provisioningState
          value: []
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>inventory_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.system_center_vm_manager.inventory_items
WHERE inventoryItemResourceName = '{{ inventoryItemResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmmServerName = '{{ vmmServerName }}';
```
