---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Spring Cloud Gateway properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gatewayName, resourceGroupName, serviceName, subscriptionId` | Get the Spring Cloud Gateway and its properties. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `create_or_update` | `INSERT` | `gatewayName, resourceGroupName, serviceName, subscriptionId` | Create the default Spring Cloud Gateway or update the existing Spring Cloud Gateway. |
| `delete` | `DELETE` | `gatewayName, resourceGroupName, serviceName, subscriptionId` | Disable the default Spring Cloud Gateway. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `restart` | `EXEC` | `gatewayName, resourceGroupName, serviceName, subscriptionId` | Restart the Spring Cloud Gateway. |
| `validate_domain` | `EXEC` | `gatewayName, resourceGroupName, serviceName, subscriptionId, data__name` | Check the domains are valid as well as not in use. |
