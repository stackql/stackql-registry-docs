---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.extensions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Get particular Arc Extension of HCI Cluster. |
| `list_by_arc_setting` | `SELECT` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | List all Extensions under ArcSetting resource. |
| `create` | `INSERT` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Create Extension for HCI cluster. |
| `delete` | `DELETE` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Delete particular Arc Extension of HCI Cluster. |
| `_list_by_arc_setting` | `EXEC` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | List all Extensions under ArcSetting resource. |
| `update` | `EXEC` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Update Extension for HCI cluster. |
| `upgrade` | `EXEC` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Upgrade a particular Arc Extension of HCI Cluster. |
