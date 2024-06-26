---
title: workspace_tag_product_link
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_tag_product_link
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
<tr><td><b>Name</b></td><td><code>workspace_tag_product_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_tag_product_link" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productLinkId, resourceGroupName, serviceName, subscriptionId, tagId, workspaceId" /> | Gets the product link for the tag. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId, workspaceId" /> | Lists a collection of the product links associated with a tag. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="productLinkId, resourceGroupName, serviceName, subscriptionId, tagId, workspaceId" /> | Adds a product to the specified tag via link. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="productLinkId, resourceGroupName, serviceName, subscriptionId, tagId, workspaceId" /> | Deletes the specified product from the specified tag. |
