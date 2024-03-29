---
title: api_portals
hide_title: false
hide_table_of_contents: false
keywords:
  - api_portals
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
<tr><td><b>Name</b></td><td><code>api_portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.api_portals</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | API portal properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiPortalName, resourceGroupName, serviceName, subscriptionId` | Get the API portal and its properties. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `create_or_update` | `INSERT` | `apiPortalName, resourceGroupName, serviceName, subscriptionId` | Create the default API portal or update the existing API portal. |
| `delete` | `DELETE` | `apiPortalName, resourceGroupName, serviceName, subscriptionId` | Delete the default API portal. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `validate_domain` | `EXEC` | `apiPortalName, resourceGroupName, serviceName, subscriptionId, data__name` | Check the domains are valid as well as not in use. |
