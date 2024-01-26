---
title: arc_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - arc_settings
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
<tr><td><b>Name</b></td><td><code>arc_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.arc_settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Get ArcSetting resource details of HCI Cluster. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get ArcSetting resources of HCI Cluster. |
| `create` | `INSERT` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Create ArcSetting for HCI cluster. |
| `delete` | `DELETE` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Delete ArcSetting resource details of HCI Cluster. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Get ArcSetting resources of HCI Cluster. |
| `consent_and_install_default_extensions` | `EXEC` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Add consent time for default extensions and initiate extensions installation |
| `generate_password` | `EXEC` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Generate password for arc settings. |
| `initialize_disable_process` | `EXEC` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Initializes ARC Disable process on the cluster |
| `update` | `EXEC` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Update ArcSettings for HCI cluster. |
