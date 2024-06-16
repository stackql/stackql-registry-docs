---
title: product
hide_title: false
hide_table_of_contents: false
keywords:
  - product
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
<tr><td><b>Name</b></td><td><code>product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.product" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the product specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of products in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Creates or Updates a product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, productId, resourceGroupName, serviceName, subscriptionId" /> | Delete product. |
| <CopyableCode code="list_by_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of products associated with tags. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, productId, resourceGroupName, serviceName, subscriptionId" /> | Update existing product details. |
