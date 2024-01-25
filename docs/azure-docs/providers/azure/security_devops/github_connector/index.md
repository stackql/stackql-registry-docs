---
title: github_connector
hide_title: false
hide_table_of_contents: false
keywords:
  - github_connector
  - security_devops
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
<tr><td><b>Name</b></td><td><code>github_connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_devops.github_connector</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the ARM resource for /subscriptions/xxx/resourceGroups/xxx/providers/Microsoft.SecurityDevOps/gitHubConnectors. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `gitHubConnectorName, resourceGroupName, subscriptionId` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `list_by_subscription` | `SELECT` | `subscriptionId` |
| `create_or_update` | `INSERT` | `gitHubConnectorName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `gitHubConnectorName, resourceGroupName, subscriptionId` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `_list_by_subscription` | `EXEC` | `subscriptionId` |
| `update` | `EXEC` | `gitHubConnectorName, resourceGroupName, subscriptionId` |
