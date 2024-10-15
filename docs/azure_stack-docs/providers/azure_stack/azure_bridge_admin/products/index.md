---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - azure_bridge_admin
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_bridge_admin.products" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="activationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_part_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="compatibility" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="gallery_item_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_uris" /> | `text` | field from the `properties` object |
| <CopyableCode code="legal_terms" /> | `text` | field from the `properties` object |
| <CopyableCode code="links" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="payload_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="privacy_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="productName" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="vm_extension_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for a product. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Return product name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="activationName, resourceGroupName, subscriptionId" /> | Return product name. |
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Downloads a product from azure marketplace. |

## `SELECT` examples

Return product name.

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
id,
name,
description,
activationName,
billing_part_number,
compatibility,
display_name,
gallery_item_identity,
icon_uris,
legal_terms,
links,
location,
offer,
offer_version,
payload_length,
privacy_policy,
productName,
product_kind,
product_properties,
provisioning_state,
publisher_display_name,
publisher_identifier,
resourceGroupName,
sku,
subscriptionId,
tags,
type,
vm_extension_type
FROM azure_stack.azure_bridge_admin.vw_products
WHERE activationName = '{{ activationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.azure_bridge_admin.products
WHERE activationName = '{{ activationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

