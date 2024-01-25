---
title: server_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - server_capabilities
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
<tr><td><b>Name</b></td><td><code>server_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.server_capabilities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of flexible servers capability |
| `fastProvisioningSupported` | `string` | Gets a value indicating whether fast provisioning is supported. "Enabled" means fast provisioning is supported. "Disabled" stands for fast provisioning is not supported. |
| `geoBackupSupported` | `string` | Determines if geo-backup is supported in this region. "Enabled" means geo-backup is supported. "Disabled" stands for geo-back is not supported. |
| `onlineResizeSupported` | `string` | A value indicating whether online resize is supported in this region for the given subscription. "Enabled" means storage online resize is supported. "Disabled" means storage online resize is not supported. |
| `reason` | `string` | The reason for the capability not being available. |
| `restricted` | `string` | A value indicating whether this region is restricted. "Enabled" means region is restricted. "Disabled" stands for region is not restricted. |
| `status` | `string` | The status of the capability. |
| `storageAutoGrowthSupported` | `string` | A value indicating whether storage auto-grow is supported in this region. "Enabled" means storage auto-grow is supported. "Disabled" stands for storage auto-grow is not supported. |
| `supportedFastProvisioningEditions` | `array` | List of supported server editions for fast provisioning |
| `supportedServerEditions` | `array` | List of supported flexible server editions |
| `supportedServerVersions` | `array` | The list of server versions supported for this capability. |
| `zoneRedundantHaAndGeoBackupSupported` | `string` | A value indicating whether Zone Redundant HA and Geo-backup is supported in this region. "Enabled" means zone redundant HA and geo-backup is supported. "Disabled" stands for zone redundant HA and geo-backup is not supported. |
| `zoneRedundantHaSupported` | `string` | A value indicating whether Zone Redundant HA is supported in this region. "Enabled" means zone redundant HA is supported. "Disabled" stands for zone redundant HA is not supported. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, serverName, subscriptionId` |
