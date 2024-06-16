---
title: web_apps_vnet_connection_gateway_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_vnet_connection_gateway_slot
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
<tr><td><b>Name</b></td><td><code>web_apps_vnet_connection_gateway_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps_vnet_connection_gateway_slot" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | VnetGateway resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Gets an app's Virtual Network gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="gatewayName, name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
