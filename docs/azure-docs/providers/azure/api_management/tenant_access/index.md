---
title: tenant_access
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_access
  - api_management
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
<tr><td><b>Name</b></td><td><code>tenant_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tenant_access</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accessName, resourceGroupName, serviceName, subscriptionId` | Get tenant access information details without secrets. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Returns list of access infos - for Git and Management endpoints. |
| `create` | `INSERT` | `If-Match, accessName, resourceGroupName, serviceName, subscriptionId` | Update tenant access information details. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Returns list of access infos - for Git and Management endpoints. |
| `regenerate_primary_key` | `EXEC` | `accessName, resourceGroupName, serviceName, subscriptionId` | Regenerate primary access key |
| `regenerate_secondary_key` | `EXEC` | `accessName, resourceGroupName, serviceName, subscriptionId` | Regenerate secondary access key |
| `update` | `EXEC` | `If-Match, accessName, resourceGroupName, serviceName, subscriptionId` | Update tenant access information details. |
