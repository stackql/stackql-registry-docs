---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - maria_db
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.configurations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Configurations_Get` | `SELECT` | `configurationName, resourceGroupName, serverName, subscriptionId` | Gets information about a configuration of server. |
| `Configurations_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the configurations in a given server. |
| `Configurations_CreateOrUpdate` | `INSERT` | `configurationName, resourceGroupName, serverName, subscriptionId` | Updates a configuration of a server. |
