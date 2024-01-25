---
title: registry_data_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_data_versions
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
<tr><td><b>Name</b></td><td><code>registry_data_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.registry_data_versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `name, registryName, resourceGroupName, subscriptionId, version` |
| `list` | `SELECT` | `name, registryName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `name, registryName, resourceGroupName, subscriptionId, version, data__properties` |
| `delete` | `DELETE` | `name, registryName, resourceGroupName, subscriptionId, version` |
| `_list` | `EXEC` | `name, registryName, resourceGroupName, subscriptionId` |
| `create_or_get_start_pending_upload` | `EXEC` | `name, registryName, resourceGroupName, subscriptionId, version` |
