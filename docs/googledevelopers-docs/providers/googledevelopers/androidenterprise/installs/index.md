---
title: installs
hide_title: false
hide_table_of_contents: false
keywords:
  - installs
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
<tr><td><b>Name</b></td><td><code>installs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.installs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `installState` | `string` | Install state. The state "installPending" means that an install request has recently been made and download to the device is in progress. The state "installed" means that the app has been installed. This field is read-only. |
| `productId` | `string` | The ID of the product that the install is for. For example, "app:com.google.android.gm". |
| `versionCode` | `integer` | The version of the installed product. Guaranteed to be set only if the install state is "installed". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceId, enterpriseId, installId, userId` | Retrieves details of an installation of an app on a device. |
| `list` | `SELECT` | `deviceId, enterpriseId, userId` | Retrieves the details of all apps installed on the specified device. |
| `delete` | `DELETE` | `deviceId, enterpriseId, installId, userId` | Requests to remove an app from a device. A call to get or list will still show the app as installed on the device until it is actually removed. |
| `update` | `EXEC` | `deviceId, enterpriseId, installId, userId` | Requests to install the latest version of an app to a device. If the app is already installed, then it is updated to the latest version if necessary. |
