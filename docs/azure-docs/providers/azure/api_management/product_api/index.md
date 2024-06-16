---
title: product_api
hide_title: false
hide_table_of_contents: false
keywords:
  - product_api
  - api_management
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
<tr><td><b>Name</b></td><td><code>product_api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.product_api" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of the APIs associated with a product. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, productId, resourceGroupName, serviceName, subscriptionId" /> | Adds an API to the specified product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiId, productId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified API from the specified product. |
