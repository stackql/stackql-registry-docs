---
title: registry_code_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_code_containers
  - ml_services
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
<tr><td><b>Name</b></td><td><code>registry_code_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.registry_code_containers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `codeName, registryName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `codeName, registryName, resourceGroupName, subscriptionId, data__properties` |
| `delete` | `DELETE` | `codeName, registryName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` |
