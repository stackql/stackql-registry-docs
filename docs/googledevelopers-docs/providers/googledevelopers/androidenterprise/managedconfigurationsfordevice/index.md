---
title: managedconfigurationsfordevice
hide_title: false
hide_table_of_contents: false
keywords:
  - managedconfigurationsfordevice
  - androidenterprise
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
<tr><td><b>Name</b></td><td><code>managedconfigurationsfordevice</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.managedconfigurationsfordevice</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Deprecated. |
| `managedProperty` | `array` | The set of managed properties for this configuration. |
| `productId` | `string` | The ID of the product that the managed configuration is for, e.g. "app:com.google.android.gm". |
| `configurationVariables` | `object` | A configuration variables resource contains the managed configuration settings ID to be applied to a single user, as well as the variable set that is attributed to the user. The variable set will be used to replace placeholders in the managed configuration settings. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceId, enterpriseId, managedConfigurationForDeviceId, userId` | Retrieves details of a per-device managed configuration. |
| `list` | `SELECT` | `deviceId, enterpriseId, userId` | Lists all the per-device managed configurations for the specified device. Only the ID is set. |
| `delete` | `DELETE` | `deviceId, enterpriseId, managedConfigurationForDeviceId, userId` | Removes a per-device managed configuration for an app for the specified device. |
| `update` | `EXEC` | `deviceId, enterpriseId, managedConfigurationForDeviceId, userId` | Adds or updates a per-device managed configuration for an app for the specified device. |
