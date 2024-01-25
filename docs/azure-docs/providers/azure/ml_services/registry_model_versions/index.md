---
title: registry_model_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_model_versions
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
<tr><td><b>Name</b></td><td><code>registry_model_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.registry_model_versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `modelName, registryName, resourceGroupName, subscriptionId, version` |
| `list` | `SELECT` | `modelName, registryName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `modelName, registryName, resourceGroupName, subscriptionId, version, data__properties` |
| `delete` | `DELETE` | `modelName, registryName, resourceGroupName, subscriptionId, version` |
| `_list` | `EXEC` | `modelName, registryName, resourceGroupName, subscriptionId` |
| `create_or_get_start_pending_upload` | `EXEC` | `modelName, registryName, resourceGroupName, subscriptionId, version` |
| `package` | `EXEC` | `modelName, registryName, resourceGroupName, subscriptionId, version, data__inferencingServer, data__targetEnvironmentId` |
