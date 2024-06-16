---
title: order_items
hide_title: false
hide_table_of_contents: false
keywords:
  - order_items
  - edge_order
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>order_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_order.order_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Msi identity details of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents order item properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId" /> | Get an order item. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List order items at resource group level. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List order items at subscription level. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId, data__properties" /> | Create an order item. Existing order item cannot be updated with this api and should instead be updated with the Update order item<br />API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId" /> | Delete an order item. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId, data__reason" /> | Cancel order item. |
| <CopyableCode code="return" /> | `EXEC` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId, data__returnReason" /> | Return order item. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="orderItemName, resourceGroupName, subscriptionId" /> | Update the properties of an existing order item. |
