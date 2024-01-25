---
title: builds
hide_title: false
hide_table_of_contents: false
keywords:
  - builds
  - container_apps
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
<tr><td><b>Name</b></td><td><code>builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.builds</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `buildName, builderName, resourceGroupName, subscriptionId` | Get a BuildResource |
| `list_by_builder_resource` | `SELECT` | `builderName, resourceGroupName, subscriptionId` | List BuildResource resources by BuilderResource |
| `create_or_update` | `INSERT` | `buildName, builderName, resourceGroupName, subscriptionId` | Create a BuildResource |
| `delete` | `DELETE` | `buildName, builderName, resourceGroupName, subscriptionId` | Delete a BuildResource |
| `_list_by_builder_resource` | `EXEC` | `builderName, resourceGroupName, subscriptionId` | List BuildResource resources by BuilderResource |
