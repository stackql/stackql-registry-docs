---
title: gateway_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_custom_domains
  - app_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>gateway_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.gateway_custom_domains</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GatewayCustomDomains_Get` | `SELECT` | `domainName, gatewayName, resourceGroupName, serviceName, subscriptionId` | Get the Spring Cloud Gateway custom domain. |
| `GatewayCustomDomains_List` | `SELECT` | `gatewayName, resourceGroupName, serviceName, subscriptionId` | Handle requests to list all Spring Cloud Gateway custom domains. |
| `GatewayCustomDomains_CreateOrUpdate` | `INSERT` | `domainName, gatewayName, resourceGroupName, serviceName, subscriptionId` | Create or update the Spring Cloud Gateway custom domain. |
| `GatewayCustomDomains_Delete` | `DELETE` | `domainName, gatewayName, resourceGroupName, serviceName, subscriptionId` | Delete the Spring Cloud Gateway custom domain. |
