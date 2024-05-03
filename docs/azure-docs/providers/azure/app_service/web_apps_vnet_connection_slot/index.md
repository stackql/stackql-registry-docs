---
title: web_apps_vnet_connection_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_vnet_connection_slot
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
<tr><td><b>Name</b></td><td><code>web_apps_vnet_connection_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps_vnet_connection_slot" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Virtual Network information contract. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Gets a virtual network the app (or deployment slot) is connected to by name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Deletes a connection from an app (or deployment slot to a named virtual network. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, vnetName" /> | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |
