---
title: security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_settings
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.security_settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, securitySettingsName, subscriptionId` | Get a SecuritySetting |
| `list_by_clusters` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | List SecuritySetting resources by Clusters |
| `create_or_update` | `INSERT` | `clusterName, resourceGroupName, securitySettingsName, subscriptionId` | Create a security setting |
| `delete` | `DELETE` | `clusterName, resourceGroupName, securitySettingsName, subscriptionId` | Delete a SecuritySetting |
| `_list_by_clusters` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | List SecuritySetting resources by Clusters |
