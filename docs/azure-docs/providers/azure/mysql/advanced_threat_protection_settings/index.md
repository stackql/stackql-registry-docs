---
title: advanced_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - advanced_threat_protection_settings
  - mysql
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
<tr><td><b>Name</b></td><td><code>advanced_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.advanced_threat_protection_settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId` | Get a server's Advanced Threat Protection state |
| `list` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server's Advanced Threat Protection states. |
| `_list` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server's Advanced Threat Protection states. |
| `update` | `EXEC` | `advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId` | Updates a server's Advanced Threat Protection state. |
