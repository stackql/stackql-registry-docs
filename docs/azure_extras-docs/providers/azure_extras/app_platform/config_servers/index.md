---
title: config_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - config_servers
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
<tr><td><b>Name</b></td><td><code>config_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.config_servers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConfigServers_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get the config server and its properties. |
| `ConfigServers_UpdatePatch` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Update the config server. |
| `ConfigServers_UpdatePut` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Update the config server. |
| `ConfigServers_Validate` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Check if the config server settings are valid. |
