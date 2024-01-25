---
title: storages
hide_title: false
hide_table_of_contents: false
keywords:
  - storages
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.storages</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, storageName, subscriptionId` | Get the storage resource. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | List all the storages of one Azure Spring Apps resource. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, storageName, subscriptionId` | Create or update storage resource. |
| `delete` | `DELETE` | `resourceGroupName, serviceName, storageName, subscriptionId` | Delete the storage resource. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | List all the storages of one Azure Spring Apps resource. |
