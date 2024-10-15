---
title: capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities
  - fabric
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

Creates, updates, deletes, gets or lists a <code>capacities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fabric.capacities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_capacities', value: 'view', },
        { label: 'capacities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administration" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacityName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Represents the SKU name and Azure pricing tier for Microsoft Fabric capacity resource. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The Microsoft Fabric capacity properties. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for Microsoft Fabric capacity resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="capacityName, resourceGroupName, subscriptionId" /> | Get a FabricCapacity |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List FabricCapacity resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List FabricCapacity resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="capacityName, resourceGroupName, subscriptionId, data__properties, data__sku" /> | Create a FabricCapacity |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="capacityName, resourceGroupName, subscriptionId" /> | Delete a FabricCapacity |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="capacityName, resourceGroupName, subscriptionId" /> | Update a FabricCapacity |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Implements local CheckNameAvailability operations |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="capacityName, resourceGroupName, subscriptionId" /> | Resume operation of the specified Fabric capacity instance. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="capacityName, resourceGroupName, subscriptionId" /> | Suspend operation of the specified Fabric capacity instance. |

## `SELECT` examples

List FabricCapacity resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_capacities', value: 'view', },
        { label: 'capacities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administration,
capacityName,
location,
provisioning_state,
resourceGroupName,
sku,
state,
subscriptionId,
tags
FROM azure.fabric.vw_capacities
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.fabric.capacities
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>capacities</code> resource.

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
INSERT INTO azure.fabric.capacities (
capacityName,
resourceGroupName,
subscriptionId,
data__properties,
data__sku,
properties,
sku,
tags,
location
)
SELECT 
'{{ capacityName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ properties }}',
'{{ sku }}',
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
        - name: provisioningState
          value: []
        - name: state
          value: []
        - name: administration
          value:
            - name: members
              value:
                - string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>capacities</code> resource.

```sql
/*+ update */
UPDATE azure.fabric.capacities
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
capacityName = '{{ capacityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>capacities</code> resource.

```sql
/*+ delete */
DELETE FROM azure.fabric.capacities
WHERE capacityName = '{{ capacityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
