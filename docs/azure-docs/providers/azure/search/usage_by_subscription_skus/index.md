---
title: usage_by_subscription_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_by_subscription_skus
  - search
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

Creates, updates, deletes, gets or lists a <code>usage_by_subscription_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_by_subscription_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.usage_by_subscription_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID of the quota usage SKU endpoint for Microsoft.Search provider. |
| <CopyableCode code="name" /> | `object` | The name of the SKU supported by Azure AI Search. |
| <CopyableCode code="currentValue" /> | `integer` | The currently used up value for the particular search SKU. |
| <CopyableCode code="limit" /> | `integer` | The quota limit for the particular search SKU. |
| <CopyableCode code="unit" /> | `string` | The unit of measurement for the search SKU. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, skuName, subscriptionId" /> | Gets the quota usage for a search sku in the given subscription. |

## `SELECT` examples

Gets the quota usage for a search sku in the given subscription.


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.search.usage_by_subscription_skus
WHERE location = '{{ location }}'
AND skuName = '{{ skuName }}'
AND subscriptionId = '{{ subscriptionId }}';
```