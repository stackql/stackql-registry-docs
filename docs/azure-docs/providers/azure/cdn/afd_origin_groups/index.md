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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AFDOriginGroups_Get` | `SELECT` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Gets an existing origin group within a profile. |
| `AFDOriginGroups_ListByProfile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists all of the existing origin groups within a profile. |
| `AFDOriginGroups_Create` | `INSERT` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Creates a new origin group within the specified profile. |
| `AFDOriginGroups_Delete` | `DELETE` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Deletes an existing origin group within a profile. |
| `AFDOriginGroups_ListResourceUsage` | `EXEC` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Checks the quota and actual usage of endpoints under the given CDN profile. |
| `AFDOriginGroups_Update` | `EXEC` | `originGroupName, profileName, resourceGroupName, subscriptionId` | Updates an existing origin group within a profile. |
