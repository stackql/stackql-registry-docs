---
title: product_api_links
hide_title: false
hide_table_of_contents: false
keywords:
  - product_api_links
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

Creates, updates, deletes, gets or lists a <code>product_api_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_api_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.product_api_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_api_links', value: 'view', },
        { label: 'product_api_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiLinkId" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="productId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Product-API link entity properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiLinkId, productId, resourceGroupName, serviceName, subscriptionId" /> | Gets the API link for the product. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of the API links associated with a product. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiLinkId, productId, resourceGroupName, serviceName, subscriptionId" /> | Adds an API to the specified product via link. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiLinkId, productId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified API from the specified product. |

## `SELECT` examples

Lists a collection of the API links associated with a product.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_product_api_links', value: 'view', },
        { label: 'product_api_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiLinkId,
api_id,
productId,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.api_management.vw_product_api_links
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
FROM azure.api_management.product_api_links
WHERE productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>product_api_links</code> resource.

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
INSERT INTO azure.api_management.product_api_links (
apiLinkId,
productId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiLinkId }}',
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
        - name: apiId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>product_api_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.product_api_links
WHERE apiLinkId = '{{ apiLinkId }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
