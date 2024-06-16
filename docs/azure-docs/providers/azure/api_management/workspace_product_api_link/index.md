---
title: workspace_product_api_link
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_product_api_link
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
<tr><td><b>Name</b></td><td><code>workspace_product_api_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_product_api_link" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiLinkId, productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the API link for the product. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of the API links associated with a product. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiLinkId, productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Adds an API to the specified product via link. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiLinkId, productId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the specified API from the specified product. |
