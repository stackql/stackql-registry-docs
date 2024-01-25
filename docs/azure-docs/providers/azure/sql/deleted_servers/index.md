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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deletedServerName, locationName, subscriptionId` | Gets a deleted server. |
| `list` | `SELECT` | `subscriptionId` | Gets a list of all deleted servers in a subscription. |
| `list_by_location` | `SELECT` | `locationName, subscriptionId` | Gets a list of deleted servers for a location. |
| `_list` | `EXEC` | `subscriptionId` | Gets a list of all deleted servers in a subscription. |
| `_list_by_location` | `EXEC` | `locationName, subscriptionId` | Gets a list of deleted servers for a location. |
| `recover` | `EXEC` | `deletedServerName, locationName, subscriptionId` | Recovers a deleted server. |
