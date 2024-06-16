---
title: addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - addresses
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
<tr><td><b>Name</b></td><td><code>addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_order.addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Address Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="addressName, resourceGroupName, subscriptionId" /> | Get information about the specified address. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the addresses available under the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the addresses available under the subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="addressName, resourceGroupName, subscriptionId, data__properties" /> | Create a new address with the specified parameters. Existing address cannot be updated with this API and should<br />instead be updated with the Update address API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="addressName, resourceGroupName, subscriptionId" /> | Delete an address. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="addressName, resourceGroupName, subscriptionId" /> | Update the properties of an existing address. |
