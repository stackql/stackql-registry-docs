---
title: dev_tool_portals
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_tool_portals
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
<tr><td><b>Name</b></td><td><code>dev_tool_portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.dev_tool_portals</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `devToolPortalName, resourceGroupName, serviceName, subscriptionId` | Get the Application Live  and its properties. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `create_or_update` | `INSERT` | `devToolPortalName, resourceGroupName, serviceName, subscriptionId` | Create the default Dev Tool Portal or update the existing Dev Tool Portal. |
| `delete` | `DELETE` | `devToolPortalName, resourceGroupName, serviceName, subscriptionId` | Disable the default Dev Tool Portal. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
