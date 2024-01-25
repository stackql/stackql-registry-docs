---
title: registry_environment_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_environment_versions
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
<tr><td><b>Name</b></td><td><code>registry_environment_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.registry_environment_versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `environmentName, registryName, resourceGroupName, subscriptionId, version` |
| `list` | `SELECT` | `environmentName, registryName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `environmentName, registryName, resourceGroupName, subscriptionId, version, data__properties` |
| `delete` | `DELETE` | `environmentName, registryName, resourceGroupName, subscriptionId, version` |
| `_list` | `EXEC` | `environmentName, registryName, resourceGroupName, subscriptionId` |
