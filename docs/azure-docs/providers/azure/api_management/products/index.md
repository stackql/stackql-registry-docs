---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - api_management
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.products" /></td></tr>
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
| <CopyableCode code="approval_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="productId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptions_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="terms" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Product profile. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the product specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of products in the specified service instance. |
| <CopyableCode code="list_by_tags" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of products associated with tags. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Creates or Updates a product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, productId, resourceGroupName, serviceName, subscriptionId" /> | Delete product. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, productId, resourceGroupName, serviceName, subscriptionId" /> | Update existing product details. |

## `SELECT` examples

Lists a collection of products in the specified service instance.

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
approval_required,
display_name,
productId,
resourceGroupName,
serviceName,
state,
subscriptionId,
subscription_required,
subscriptions_limit,
terms
FROM azure.api_management.vw_products
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.products
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
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
INSERT INTO azure.api_management.products (
productId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ productId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: displayName
          value: string
        - name: description
          value: string
        - name: terms
          value: string
        - name: subscriptionRequired
          value: boolean
        - name: approvalRequired
          value: boolean
        - name: subscriptionsLimit
          value: integer
        - name: state
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>products</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.products
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>products</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.products
WHERE If-Match = '{{ If-Match }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
