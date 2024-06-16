---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - storage_cache
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of this SKU. |
| <CopyableCode code="capabilities" /> | `array` | A list of capabilities of this SKU, such as throughput or ops/sec. |
| <CopyableCode code="locationInfo" /> | `array` | The set of locations where the SKU is available. |
| <CopyableCode code="locations" /> | `array` | The set of locations where the SKU is available. This is the supported and registered Azure Geo Regions (e.g., West US, East US, Southeast Asia, etc.). |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the SKU applies to. |
| <CopyableCode code="restrictions" /> | `array` | The restrictions preventing this SKU from being used. This is empty if there are no restrictions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
