---
title: resource_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_skus
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>resource_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.resource_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Sku name |
| <CopyableCode code="apiVersion" /> | `string` | StoragePool RP API version |
| <CopyableCode code="capabilities" /> | `array` | List of additional capabilities for StoragePool resource. |
| <CopyableCode code="locationInfo" /> | `object` | Zone and capability info for resource sku |
| <CopyableCode code="resourceType" /> | `string` | StoragePool resource type |
| <CopyableCode code="restrictions" /> | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| <CopyableCode code="tier" /> | `string` | Sku tier |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |
