---
title: storages
hide_title: false
hide_table_of_contents: false
keywords:
  - storages
  - app_platform
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.storages</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Storages_Get` | `SELECT` | `resourceGroupName, serviceName, storageName, subscriptionId` | Get the storage resource. |
| `Storages_List` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | List all the storages of one Azure Spring Apps resource. |
| `Storages_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, storageName, subscriptionId` | Create or update storage resource. |
| `Storages_Delete` | `DELETE` | `resourceGroupName, serviceName, storageName, subscriptionId` | Delete the storage resource. |
