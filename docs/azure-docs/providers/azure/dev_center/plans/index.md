---
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.plans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_plans', value: 'view', },
        { label: 'plans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="planName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the devcenter plan. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Gets a devcenter plan. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all devcenter plans in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all devcenter plans in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Creates or updates a devcenter plan resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Deletes a devcenter plan |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Partially updates a devcenter plan. |

## `SELECT` examples

Lists all devcenter plans in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_plans', value: 'view', },
        { label: 'plans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
planName,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags
FROM azure.dev_center.vw_plans
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
FROM azure.dev_center.plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>plans</code> resource.

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
INSERT INTO azure.dev_center.plans (
planName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
sku
)
SELECT 
'{{ planName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ sku }}'
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
        - name: provisioningState
          value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>plans</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.plans
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}'
WHERE 
planName = '{{ planName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>plans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.plans
WHERE planName = '{{ planName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
