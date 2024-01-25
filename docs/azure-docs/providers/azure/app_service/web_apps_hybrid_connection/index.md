---
title: web_apps_hybrid_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_hybrid_connection
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_apps_hybrid_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_hybrid_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | HybridConnection resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App. |
| `create_or_update` | `INSERT` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Creates a new Hybrid Connection using a Service Bus relay. |
| `delete` | `DELETE` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Removes a Hybrid Connection from this site. |
| `update` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Creates a new Hybrid Connection using a Service Bus relay. |
