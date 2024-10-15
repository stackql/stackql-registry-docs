---
title: product_wikis
hide_title: false
hide_table_of_contents: false
keywords:
  - product_wikis
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

Creates, updates, deletes, gets or lists a <code>product_wikis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_wikis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.product_wikis" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_wikis', value: 'view', },
        { label: 'product_wikis', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="documents" /> | `text` | field from the `properties` object |
| <CopyableCode code="productId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Wiki contract details |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Wiki for a Product specified by its identifier. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Wiki for a Product specified by its identifier. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Wiki for a Product or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, productId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified Wiki from a Product. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, productId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the Wiki for a Product specified by its identifier. |

## `SELECT` examples

Gets the details of the Wiki for a Product specified by its identifier.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_wikis', value: 'view', },
        { label: 'product_wikis', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
documents,
productId,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.api_management.vw_product_wikis
WHERE productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.product_wikis
WHERE productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>product_wikis</code> resource.

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
INSERT INTO azure.api_management.product_wikis (
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
        - name: documents
          value:
            - - name: documentationId
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>product_wikis</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.product_wikis
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

Deletes the specified <code>product_wikis</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.product_wikis
WHERE If-Match = '{{ If-Match }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
