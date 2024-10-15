---
title: environments_capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_capacities
  - app_service
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

Creates, updates, deletes, gets or lists a <code>environments_capacities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_capacities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.environments_capacities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the stamp. |
| <CopyableCode code="availableCapacity" /> | `integer` | Available capacity (# of machines, bytes of storage etc...). |
| <CopyableCode code="computeMode" /> | `string` | Shared/dedicated workers. |
| <CopyableCode code="excludeFromCapacityAllocation" /> | `boolean` | If <code>true</code>, it includes basic apps.
Basic apps are not used for capacity allocation. |
| <CopyableCode code="isApplicableForAllComputeModes" /> | `boolean` | <code>true</code> if capacity is applicable for all apps; otherwise, <code>false</code>. |
| <CopyableCode code="isLinux" /> | `boolean` | Is this a linux stamp capacity |
| <CopyableCode code="siteMode" /> | `string` | Shared or Dedicated. |
| <CopyableCode code="totalCapacity" /> | `integer` | Total capacity (# of machines, bytes of storage etc...). |
| <CopyableCode code="unit" /> | `string` | Name of the unit. |
| <CopyableCode code="workerSize" /> | `string` | Size of the machines. |
| <CopyableCode code="workerSizeId" /> | `integer` | Size ID of machines: 
0 - Small
1 - Medium
2 - Large |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get the used, available, and total worker capacity an App Service Environment. |

## `SELECT` examples

Description for Get the used, available, and total worker capacity an App Service Environment.


```sql
SELECT
name,
availableCapacity,
computeMode,
excludeFromCapacityAllocation,
isApplicableForAllComputeModes,
isLinux,
siteMode,
totalCapacity,
unit,
workerSize,
workerSizeId
FROM azure.app_service.environments_capacities
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```