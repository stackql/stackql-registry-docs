---
title: server_configuration_options
hide_title: false
hide_table_of_contents: false
keywords:
  - server_configuration_options
  - sql
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
<tr><td><b>Name</b></td><td><code>server_configuration_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_configuration_options</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managedInstanceName, resourceGroupName, serverConfigurationOptionName, subscriptionId` | Gets managed instance server configuration option. |
| `list_by_managed_instance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance server configuration options. |
| `create_or_update` | `INSERT` | `managedInstanceName, resourceGroupName, serverConfigurationOptionName, subscriptionId` | Updates managed instance server configuration option. |
| `_list_by_managed_instance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance server configuration options. |
