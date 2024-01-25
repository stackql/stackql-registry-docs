---
title: origins
hide_title: false
hide_table_of_contents: false
keywords:
  - origins
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
<tr><td><b>Name</b></td><td><code>origins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.origins</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointName, originName, profileName, resourceGroupName, subscriptionId` | Gets an existing origin within an endpoint. |
| `list_by_endpoint` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing origins within an endpoint. |
| `create` | `INSERT` | `endpointName, originName, profileName, resourceGroupName, subscriptionId` | Creates a new origin within the specified endpoint. |
| `delete` | `DELETE` | `endpointName, originName, profileName, resourceGroupName, subscriptionId` | Deletes an existing origin within an endpoint. |
| `_list_by_endpoint` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing origins within an endpoint. |
| `update` | `EXEC` | `endpointName, originName, profileName, resourceGroupName, subscriptionId` | Updates an existing origin within an endpoint. |
