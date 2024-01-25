---
title: infrastructure_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_resources
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
<tr><td><b>Name</b></td><td><code>infrastructure_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.integration_environment.infrastructure_resources</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `infrastructureResourceName, resourceGroupName, spaceName, subscriptionId` | Get a InfrastructureResource |
| `list_by_space` | `SELECT` | `resourceGroupName, spaceName, subscriptionId` | List InfrastructureResource resources by Space |
| `create_or_update` | `INSERT` | `infrastructureResourceName, resourceGroupName, spaceName, subscriptionId` | Create a InfrastructureResource |
| `delete` | `DELETE` | `infrastructureResourceName, resourceGroupName, spaceName, subscriptionId` | Delete a InfrastructureResource |
| `_list_by_space` | `EXEC` | `resourceGroupName, spaceName, subscriptionId` | List InfrastructureResource resources by Space |
| `patch` | `EXEC` | `infrastructureResourceName, resourceGroupName, spaceName, subscriptionId` | Update a InfrastructureResource |
