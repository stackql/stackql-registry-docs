---
title: plans_vnet_route
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_vnet_route
  - app_service
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
<tr><td><b>Name</b></td><td><code>plans_vnet_route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.plans_vnet_route" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, routeName, subscriptionId, vnetName" /> | Description for Create or update a Virtual Network route in an App Service plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, routeName, subscriptionId, vnetName" /> | Description for Delete a Virtual Network route in an App Service plan. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, routeName, subscriptionId, vnetName" /> | Description for Create or update a Virtual Network route in an App Service plan. |
