---
title: product_group
hide_title: false
hide_table_of_contents: false
keywords:
  - product_group
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
<tr><td><b>Name</b></td><td><code>product_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.product_group" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Lists the collection of developer groups associated with the specified product. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupId, productId, resourceGroupName, serviceName, subscriptionId" /> | Adds the association between the specified developer group with the specified product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId, productId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the association between the specified group and product. |
