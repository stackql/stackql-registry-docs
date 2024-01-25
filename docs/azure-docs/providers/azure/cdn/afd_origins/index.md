---
title: afd_origins
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origins
  - cdn
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
<tr><td><b>Name</b></td><td><code>afd_origins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.afd_origins</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `originGroupName, originName, profileName, resourceGroupName, subscriptionId` | Gets an existing origin within an origin group. |
| `list_by_origin_group` | `SELECT` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing origins within an origin group. |
| `create` | `INSERT` | `originGroupName, originName, profileName, resourceGroupName, subscriptionId` | Creates a new origin within the specified origin group. |
| `delete` | `DELETE` | `originGroupName, originName, profileName, resourceGroupName, subscriptionId` | Deletes an existing origin within an origin group. |
| `_list_by_origin_group` | `EXEC` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing origins within an origin group. |
| `update` | `EXEC` | `originGroupName, originName, profileName, resourceGroupName, subscriptionId` | Updates an existing origin within an origin group. |
