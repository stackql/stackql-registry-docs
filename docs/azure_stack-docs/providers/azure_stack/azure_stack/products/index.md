---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - azure_stack
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextLink" /> | `string` | URI to the next page. |
| <CopyableCode code="value" /> | `array` | List of products. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registrationName, resourceGroup, subscriptionId" /> | Returns a list of products. |
| <CopyableCode code="list_by_product_name" /> | `SELECT` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> | Returns a list of products. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registrationName, resourceGroup, subscriptionId" /> | Returns a list of products. |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> | Returns a list of products. |
| <CopyableCode code="upload_log" /> | `EXEC` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> | Returns the specified product. |
