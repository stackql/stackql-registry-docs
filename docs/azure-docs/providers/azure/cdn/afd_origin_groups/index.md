---
title: afd_origin_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origin_groups
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
<tr><td><b>Name</b></td><td><code>afd_origin_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.afd_origin_groups</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Gets an existing origin group within a profile. |
| `list_by_profile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists all of the existing origin groups within a profile. |
| `create` | `INSERT` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Creates a new origin group within the specified profile. |
| `delete` | `DELETE` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Deletes an existing origin group within a profile. |
| `_list_by_profile` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Lists all of the existing origin groups within a profile. |
| `update` | `EXEC` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Updates an existing origin group within a profile. |
