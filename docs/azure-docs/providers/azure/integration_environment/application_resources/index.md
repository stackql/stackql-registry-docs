---
title: application_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - application_resources
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
<tr><td><b>Name</b></td><td><code>application_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.integration_environment.application_resources</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationName, resourceGroupName, resourceName, spaceName, subscriptionId` | Get a ApplicationResource |
| `list_by_application` | `SELECT` | `applicationName, resourceGroupName, spaceName, subscriptionId` | List ApplicationResource resources by Application |
| `create_or_update` | `INSERT` | `applicationName, resourceGroupName, resourceName, spaceName, subscriptionId` | Create a ApplicationResource |
| `delete` | `DELETE` | `applicationName, resourceGroupName, resourceName, spaceName, subscriptionId` | Delete a ApplicationResource |
| `_list_by_application` | `EXEC` | `applicationName, resourceGroupName, spaceName, subscriptionId` | List ApplicationResource resources by Application |
| `patch` | `EXEC` | `applicationName, resourceGroupName, resourceName, spaceName, subscriptionId` | Update a ApplicationResource |
