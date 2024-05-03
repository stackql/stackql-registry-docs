---
title: skus_nested_resource_type_second
hide_title: false
hide_table_of_contents: false
keywords:
  - skus_nested_resource_type_second
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>skus_nested_resource_type_second</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.skus_nested_resource_type_second" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId" /> | Gets the sku details for the given resource type and sku name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId" /> | Creates or updates the resource type skus in the given resource type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId" /> | Deletes a resource type sku. |
