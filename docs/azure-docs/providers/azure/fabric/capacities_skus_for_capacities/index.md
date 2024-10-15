---
title: capacities_skus_for_capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities_skus_for_capacities
  - fabric
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fabric.capacities_skus_for_capacities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceType" /> | `string` | The resource type |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for Microsoft Fabric capacity resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="capacityName, resourceGroupName, subscriptionId" /> | List eligible SKUs for a Microsoft Fabric resource |

## `SELECT` examples

List eligible SKUs for a Microsoft Fabric resource


```sql
SELECT
resourceType,
sku
FROM azure.fabric.capacities_skus_for_capacities
WHERE capacityName = '{{ capacityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```