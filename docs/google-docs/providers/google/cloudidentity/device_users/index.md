---
title: device_users
hide_title: false
hide_table_of_contents: false
keywords:
  - device_users
  - cloudidentity
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.device_users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the DeviceUser in format: `devices/&#123;device&#125;/deviceUsers/&#123;device_user&#125;`, where `device_user` uniquely identifies a user's use of a device. |
| `compromisedState` | `string` | Compromised State of the DeviceUser object |
| `managementState` | `string` | Output only. Management state of the user on the device. |
| `firstSyncTime` | `string` | Output only. Most recent time when user registered with this service. |
| `lastSyncTime` | `string` | Output only. Last time when user synced with policies. |
| `userAgent` | `string` | Output only. User agent on the device for this specific user |
| `userEmail` | `string` | Email address of the user registered on the device. |
| `languageCode` | `string` | Output only. Default locale used on device, in IETF BCP-47 format. |
| `createTime` | `string` | When the user first signed in to the device |
| `passwordState` | `string` | Password state of the DeviceUser object |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceUsersId, devicesId` | Retrieves the specified DeviceUser |
| `list` | `SELECT` | `devicesId` | Lists/Searches DeviceUsers. |
| `delete` | `DELETE` | `deviceUsersId, devicesId` | Deletes the specified DeviceUser. This also revokes the user's access to device data. |
| `_list` | `EXEC` | `devicesId` | Lists/Searches DeviceUsers. |
| `approve` | `EXEC` | `deviceUsersId, devicesId` | Approves device to access user data. |
| `block` | `EXEC` | `deviceUsersId, devicesId` | Blocks device from accessing user data |
| `cancel_wipe` | `EXEC` | `deviceUsersId, devicesId` | Cancels an unfinished user account wipe. This operation can be used to cancel device wipe in the gap between the wipe operation returning success and the device being wiped. |
| `lookup` | `EXEC` | `devicesId` | Looks up resource names of the DeviceUsers associated with the caller's credentials, as well as the properties provided in the request. This method must be called with end-user credentials with the scope: https://www.googleapis.com/auth/cloud-identity.devices.lookup If multiple properties are provided, only DeviceUsers having all of these properties are considered as matches - i.e. the query behaves like an AND. Different platforms require different amounts of information from the caller to ensure that the DeviceUser is uniquely identified. - iOS: No properties need to be passed, the caller's credentials are sufficient to identify the corresponding DeviceUser. - Android: Specifying the 'android_id' field is required. - Desktop: Specifying the 'raw_resource_id' field is required. |
| `wipe` | `EXEC` | `deviceUsersId, devicesId` | Wipes the user's account on a device. Other data on the device that is not associated with the user's work account is not affected. For example, if a Gmail app is installed on a device that is used for personal and work purposes, and the user is logged in to the Gmail app with their personal account as well as their work account, wiping the "deviceUser" by their work administrator will not affect their personal account within Gmail or other apps such as Photos. |
