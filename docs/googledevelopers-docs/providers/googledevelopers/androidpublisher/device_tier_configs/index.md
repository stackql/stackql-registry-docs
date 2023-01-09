---
title: device_tier_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - device_tier_configs
  - androidpublisher
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_tier_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.device_tier_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `deviceTierConfigId` | `string` | Output only. The device tier config ID. |
| `deviceTierSet` | `object` | A set of device tiers. A tier set determines what variation of app content gets served to a specific device, for device-targeted content. You should assign a priority level to each tier, which determines the ordering by which they are evaluated by Play. See the documentation of DeviceTier.level for more details. |
| `deviceGroups` | `array` | Definition of device groups for the app. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `applications_deviceTierConfigs_get` | `SELECT` | `deviceTierConfigId, packageName` | Returns a particular device tier config. |
| `applications_deviceTierConfigs_list` | `SELECT` | `packageName` | Returns created device tier configs, ordered by descending creation time. |
| `applications_deviceTierConfigs_create` | `INSERT` | `packageName` | Creates a new device tier config for an app. |
