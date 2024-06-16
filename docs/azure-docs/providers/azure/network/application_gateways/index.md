---
title: application_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways
  - network
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
<tr><td><b>Name</b></td><td><code>application_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the application gateway. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Gets the specified application gateway. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all application gateways in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Creates or updates the specified application gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Deletes the specified application gateway. |
| <CopyableCode code="backend_health" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Gets the backend health of the specified application gateway in a resource group. |
| <CopyableCode code="backend_health_on_demand" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Gets the backend health for given combination of backend pool and http setting of the specified application gateway in a resource group. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Starts the specified application gateway. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Stops the specified application gateway in a resource group. |
