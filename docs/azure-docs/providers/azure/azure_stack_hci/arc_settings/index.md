---
title: arc_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - arc_settings
  - azure_stack_hci
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
<tr><td><b>Name</b></td><td><code>arc_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_stack_hci.arc_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | ArcSetting properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ArcSettings_Get` | `SELECT` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Get ArcSetting resource details of HCI Cluster. |
| `ArcSettings_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get ArcSetting resources of HCI Cluster. |
| `ArcSettings_Create` | `INSERT` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Create ArcSetting for HCI cluster. |
| `ArcSettings_Delete` | `DELETE` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Delete ArcSetting resource details of HCI Cluster. |
| `ArcSettings_CreateIdentity` | `EXEC` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Create Aad identity for arc settings. |
| `ArcSettings_GeneratePassword` | `EXEC` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Generate password for arc settings. |
| `ArcSettings_Update` | `EXEC` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | Update ArcSettings for HCI cluster. |
