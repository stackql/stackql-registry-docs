---
title: active_directory_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - active_directory_connectors
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>active_directory_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_arc_data.active_directory_connectors</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `activeDirectoryConnectorName, api-version, dataControllerName, resourceGroupName, subscriptionId` | Retrieves an Active Directory connector resource |
| `list` | `SELECT` | `api-version, dataControllerName, resourceGroupName, subscriptionId` |  |
| `create` | `INSERT` | `activeDirectoryConnectorName, api-version, dataControllerName, resourceGroupName, subscriptionId, data__properties` | Creates or replaces an Active Directory connector resource. |
| `delete` | `DELETE` | `activeDirectoryConnectorName, api-version, dataControllerName, resourceGroupName, subscriptionId` | Deletes an Active Directory connector resource |
| `_list` | `EXEC` | `api-version, dataControllerName, resourceGroupName, subscriptionId` |  |
