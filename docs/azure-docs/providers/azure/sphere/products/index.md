---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - sphere
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

Creates, updates, deletes, gets or lists a <code>products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.products" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_products', value: 'view', },
        { label: 'products', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="productName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of product |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Get a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | List Product resources by Catalog |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Create a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Delete a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name' |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Update a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="count_devices" /> | `EXEC` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Counts devices in product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="generate_default_device_groups" /> | `EXEC` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | Generates default device groups for the product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |

## `SELECT` examples

List Product resources by Catalog

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_products', value: 'view', },
        { label: 'products', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
catalogName,
productName,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.sphere.vw_products
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sphere.products
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>products</code> resource.

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
INSERT INTO azure.sphere.products (
catalogName,
productName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ catalogName }}',
'{{ productName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>products</code> resource.

```sql
/*+ update */
UPDATE azure.sphere.products
SET 
properties = '{{ properties }}'
WHERE 
catalogName = '{{ catalogName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>products</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sphere.products
WHERE catalogName = '{{ catalogName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
