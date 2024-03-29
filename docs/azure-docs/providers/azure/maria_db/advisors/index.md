---
title: advisors
hide_title: false
hide_table_of_contents: false
keywords:
  - advisors
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
<tr><td><b>Name</b></td><td><code>advisors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.advisors</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `advisorName, resourceGroupName, serverName, subscriptionId` | Get a recommendation action advisor. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List recommendation action advisors. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | List recommendation action advisors. |
