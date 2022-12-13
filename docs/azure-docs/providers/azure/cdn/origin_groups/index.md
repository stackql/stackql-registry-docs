---
title: origin_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_groups
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
<tr><td><b>Name</b></td><td><code>origin_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.origin_groups</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OriginGroups_Get` | `SELECT` | `endpointName, originGroupName, profileName, resourceGroupName, subscriptionId` | Gets an existing origin group within an endpoint. |
| `OriginGroups_ListByEndpoint` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing origin groups within an endpoint. |
| `OriginGroups_Create` | `INSERT` | `endpointName, originGroupName, profileName, resourceGroupName, subscriptionId` | Creates a new origin group within the specified endpoint. |
| `OriginGroups_Delete` | `DELETE` | `endpointName, originGroupName, profileName, resourceGroupName, subscriptionId` | Deletes an existing origin group within an endpoint. |
| `OriginGroups_Update` | `EXEC` | `endpointName, originGroupName, profileName, resourceGroupName, subscriptionId` | Updates an existing origin group within an endpoint. |
