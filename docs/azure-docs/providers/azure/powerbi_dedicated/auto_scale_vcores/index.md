---
title: auto_scale_vcores
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scale_vcores
  - powerbi_dedicated
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

Creates, updates, deletes, gets or lists a <code>auto_scale_vcores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scale_vcores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_dedicated.auto_scale_vcores" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_auto_scale_vcores', value: 'view', },
        { label: 'auto_scale_vcores', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | An identifier that represents the PowerBI Dedicated resource. |
| <CopyableCode code="name" /> | `text` | The name of the PowerBI Dedicated resource. |
| <CopyableCode code="capacity_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the PowerBI Dedicated resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Represents the SKU name and Azure pricing tier for auto scale v-core resource. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `text` | The type of the PowerBI Dedicated resource. |
| <CopyableCode code="vcoreName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the PowerBI Dedicated resource. |
| <CopyableCode code="name" /> | `string` | The name of the PowerBI Dedicated resource. |
| <CopyableCode code="location" /> | `string` | Location of the PowerBI Dedicated resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an auto scale v-core resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for auto scale v-core resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the PowerBI Dedicated resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vcoreName" /> | Gets details about the specified auto scale v-core. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the auto scale v-cores for the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the auto scale v-cores for the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vcoreName, data__sku" /> | Provisions the specified auto scale v-core based on the configuration specified in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vcoreName" /> | Deletes the specified auto scale v-core. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vcoreName" /> | Updates the current state of the specified auto scale v-core. |

## `SELECT` examples

Lists all the auto scale v-cores for the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_auto_scale_vcores', value: 'view', },
        { label: 'auto_scale_vcores', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
capacity_limit,
capacity_object_id,
location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
system_data,
tags,
type,
vcoreName
FROM azure.powerbi_dedicated.vw_auto_scale_vcores
WHERE subscriptionId = '{{ subscriptionId }}';
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
systemData,
tags,
type
FROM azure.powerbi_dedicated.auto_scale_vcores
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>auto_scale_vcores</code> resource.

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
INSERT INTO azure.powerbi_dedicated.auto_scale_vcores (
resourceGroupName,
subscriptionId,
vcoreName,
data__sku,
sku,
properties,
location,
tags,
systemData
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vcoreName }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ systemData }}'
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
        - name: capacity
          value: integer
    - name: properties
      value:
        - name: capacityObjectId
          value: string
        - name: provisioningState
          value: string
        - name: capacityLimit
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
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: []
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>auto_scale_vcores</code> resource.

```sql
/*+ update */
UPDATE azure.powerbi_dedicated.auto_scale_vcores
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vcoreName = '{{ vcoreName }}';
```

## `DELETE` example

Deletes the specified <code>auto_scale_vcores</code> resource.

```sql
/*+ delete */
DELETE FROM azure.powerbi_dedicated.auto_scale_vcores
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vcoreName = '{{ vcoreName }}';
```
