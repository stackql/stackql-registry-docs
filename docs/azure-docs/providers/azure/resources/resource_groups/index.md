---
title: resource_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_groups
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>resource_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.resource_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_groups', value: 'view', },
        { label: 'resource_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource group. |
| <CopyableCode code="name" /> | `text` | The name of the resource group. |
| <CopyableCode code="location" /> | `text` | The location of the resource group. It cannot be changed after the resource group has been created. It must be one of the supported Azure locations. |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags attached to the resource group. |
| <CopyableCode code="type" /> | `text` | The type of the resource group. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource group. |
| <CopyableCode code="name" /> | `string` | The name of the resource group. |
| <CopyableCode code="location" /> | `string` | The location of the resource group. It cannot be changed after the resource group has been created. It must be one of the supported Azure locations. |
| <CopyableCode code="managedBy" /> | `string` | The ID of the resource that manages this resource group. |
| <CopyableCode code="properties" /> | `object` | The resource group properties. |
| <CopyableCode code="tags" /> | `object` | The tags attached to the resource group. |
| <CopyableCode code="type" /> | `string` | The type of the resource group. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the resource groups for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, data__location" /> | Creates or updates a resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId" /> | When you delete a resource group, all of its resources are also deleted. Deleting a resource group deletes all of its template deployments and currently stored operations. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Resource groups can be updated through a simple PATCH operation to a group address. The format of the request is the same as that for creating a resource group. If a field is unspecified, the current value is retained. |
| <CopyableCode code="export_template" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Captures the specified resource group as a template. |

## `SELECT` examples

Gets all the resource groups for a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_groups', value: 'view', },
        { label: 'resource_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
managed_by,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.resources.vw_resource_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
managedBy,
properties,
tags,
type
FROM azure.resources.resource_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_groups</code> resource.

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
INSERT INTO azure.resources.resource_groups (
resourceGroupName,
subscriptionId,
data__location,
properties,
location,
managedBy,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ properties }}',
'{{ location }}',
'{{ managedBy }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
    - name: location
      value: string
    - name: managedBy
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>resource_groups</code> resource.

```sql
/*+ update */
UPDATE azure.resources.resource_groups
SET 
name = '{{ name }}',
properties = '{{ properties }}',
managedBy = '{{ managedBy }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>resource_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resources.resource_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
