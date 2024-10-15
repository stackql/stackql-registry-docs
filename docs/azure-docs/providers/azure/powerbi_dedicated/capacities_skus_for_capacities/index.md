---
title: capacities_skus_for_capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities_skus_for_capacities
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

Creates, updates, deletes, gets or lists a <code>capacities_skus_for_capacities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacities_skus_for_capacities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_dedicated.capacities_skus_for_capacities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceType" /> | `string` | The resource type |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dedicatedCapacityName, resourceGroupName, subscriptionId" /> | Lists eligible SKUs for a PowerBI Dedicated resource. |

## `SELECT` examples

Lists eligible SKUs for a PowerBI Dedicated resource.


```sql
SELECT
resourceType,
sku
FROM azure.powerbi_dedicated.capacities_skus_for_capacities
WHERE dedicatedCapacityName = '{{ dedicatedCapacityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```