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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.application_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | Resource location. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `properties` | `object` | Properties of the application gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplicationGateways_Get` | `SELECT` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the specified application gateway. |
| `ApplicationGateways_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all application gateways in a resource group. |
| `ApplicationGateways_ListAll` | `SELECT` | `subscriptionId` | Gets all the application gateways in a subscription. |
| `ApplicationGateways_CreateOrUpdate` | `INSERT` | `applicationGatewayName, resourceGroupName, subscriptionId` | Creates or updates the specified application gateway. |
| `ApplicationGateways_Delete` | `DELETE` | `applicationGatewayName, resourceGroupName, subscriptionId` | Deletes the specified application gateway. |
| `ApplicationGateways_BackendHealth` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the backend health of the specified application gateway in a resource group. |
| `ApplicationGateways_BackendHealthOnDemand` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Gets the backend health for given combination of backend pool and http setting of the specified application gateway in a resource group. |
| `ApplicationGateways_GetSslPredefinedPolicy` | `EXEC` | `predefinedPolicyName, subscriptionId` | Gets Ssl predefined policy with the specified policy name. |
| `ApplicationGateways_ListAvailableRequestHeaders` | `EXEC` | `subscriptionId` | Lists all available request headers. |
| `ApplicationGateways_ListAvailableResponseHeaders` | `EXEC` | `subscriptionId` | Lists all available response headers. |
| `ApplicationGateways_ListAvailableServerVariables` | `EXEC` | `subscriptionId` | Lists all available server variables. |
| `ApplicationGateways_ListAvailableSslOptions` | `EXEC` | `subscriptionId` | Lists available Ssl options for configuring Ssl policy. |
| `ApplicationGateways_ListAvailableSslPredefinedPolicies` | `EXEC` | `subscriptionId` | Lists all SSL predefined policies for configuring Ssl policy. |
| `ApplicationGateways_ListAvailableWafRuleSets` | `EXEC` | `subscriptionId` | Lists all available web application firewall rule sets. |
| `ApplicationGateways_Start` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Starts the specified application gateway. |
| `ApplicationGateways_Stop` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Stops the specified application gateway in a resource group. |
| `ApplicationGateways_UpdateTags` | `EXEC` | `applicationGatewayName, resourceGroupName, subscriptionId` | Updates the specified application gateway tags. |
