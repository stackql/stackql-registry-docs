---
title: business_processes
hide_title: false
hide_table_of_contents: false
keywords:
  - business_processes
  - integration_environment
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
<tr><td><b>Name</b></td><td><code>business_processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.integration_environment.business_processes</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId` | Get a BusinessProcess |
| `list_by_application` | `SELECT` | `applicationName, resourceGroupName, spaceName, subscriptionId` | List BusinessProcess resources by Application |
| `create_or_update` | `INSERT` | `applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId` | Create a BusinessProcess |
| `delete` | `DELETE` | `applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId` | Delete a BusinessProcess |
| `_list_by_application` | `EXEC` | `applicationName, resourceGroupName, spaceName, subscriptionId` | List BusinessProcess resources by Application |
| `patch` | `EXEC` | `applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId` | Update a BusinessProcess |
