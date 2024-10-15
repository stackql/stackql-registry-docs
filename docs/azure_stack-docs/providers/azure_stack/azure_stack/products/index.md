---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - azure_stack
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.products" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_part_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="compatibility" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="gallery_item_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_uris" /> | `text` | field from the `properties` object |
| <CopyableCode code="legal_terms" /> | `text` | field from the `properties` object |
| <CopyableCode code="links" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="payload_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="privacy_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="productName" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="registrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroup" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
| <CopyableCode code="vm_extension_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="etag" /> | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="properties" /> | `object` | Properties portion of the product resource. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> | Returns the specified product. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registrationName, resourceGroup, subscriptionId" /> | Returns a list of products. |
| <CopyableCode code="upload_log" /> | `EXEC` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> | Returns the specified product. |

## `SELECT` examples

Returns a list of products.

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
billing_part_number,
compatibility,
display_name,
etag,
gallery_item_identity,
icon_uris,
legal_terms,
links,
offer,
offer_version,
payload_length,
privacy_policy,
productName,
product_kind,
product_properties,
publisher_display_name,
publisher_identifier,
registrationName,
resourceGroup,
sku,
subscriptionId,
type,
vm_extension_type
FROM azure_stack.azure_stack.vw_products
WHERE registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure_stack.azure_stack.products
WHERE registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

