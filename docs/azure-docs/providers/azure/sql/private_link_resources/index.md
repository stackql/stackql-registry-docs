---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.private_link_resources</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupName, resourceGroupName, serverName, subscriptionId` | Gets a private link resource for SQL server. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets the private link resources for SQL server. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets the private link resources for SQL server. |
