---
title: deleted_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_servers
  - sql
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
<tr><td><b>Name</b></td><td><code>deleted_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.deleted_servers</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeletedServers_Get` | `SELECT` | `deletedServerName, locationName, subscriptionId` | Gets a deleted server. |
| `DeletedServers_List` | `SELECT` | `subscriptionId` | Gets a list of all deleted servers in a subscription. |
| `DeletedServers_ListByLocation` | `SELECT` | `locationName, subscriptionId` | Gets a list of deleted servers for a location. |
| `DeletedServers_Recover` | `EXEC` | `deletedServerName, locationName, subscriptionId` | Recovers a deleted server. |
