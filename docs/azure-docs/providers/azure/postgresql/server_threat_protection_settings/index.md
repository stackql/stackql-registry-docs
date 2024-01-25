---
title: server_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - server_threat_protection_settings
  - postgresql
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
<tr><td><b>Name</b></td><td><code>server_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.server_threat_protection_settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverName, subscriptionId, threatProtectionName` | Get a server's Advanced Threat Protection settings. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Get a list of server's Threat Protection state. |
| `create_or_update` | `INSERT` | `resourceGroupName, serverName, subscriptionId, threatProtectionName` | Creates or updates a server's Advanced Threat Protection settings. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Get a list of server's Threat Protection state. |
