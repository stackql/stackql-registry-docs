---
title: products_products
hide_title: false
hide_table_of_contents: false
keywords:
  - products_products
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

Creates, updates, deletes, gets or lists a <code>products_products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.products_products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="etag" /> | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="properties" /> | `object` | Properties portion of the product resource. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> | Returns the specified product. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> | Returns a list of products. |

## `SELECT` examples

Returns the specified product.


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure_stack.azure_stack.products_products
WHERE productName = '{{ productName }}'
AND registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```