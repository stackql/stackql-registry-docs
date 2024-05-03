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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.device_users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the DeviceUser in format: `devices/&#123;device&#125;/deviceUsers/&#123;device_user&#125;`, where `device_user` uniquely identifies a user's use of a device. |
| <CopyableCode code="compromisedState" /> | `string` | Compromised State of the DeviceUser object |
| <CopyableCode code="createTime" /> | `string` | When the user first signed in to the device |
| <CopyableCode code="firstSyncTime" /> | `string` | Output only. Most recent time when user registered with this service. |
| <CopyableCode code="languageCode" /> | `string` | Output only. Default locale used on device, in IETF BCP-47 format. |
| <CopyableCode code="lastSyncTime" /> | `string` | Output only. Last time when user synced with policies. |
| <CopyableCode code="managementState" /> | `string` | Output only. Management state of the user on the device. |
| <CopyableCode code="passwordState" /> | `string` | Password state of the DeviceUser object |
| <CopyableCode code="userAgent" /> | `string` | Output only. User agent on the device for this specific user |
| <CopyableCode code="userEmail" /> | `string` | Email address of the user registered on the device. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceUsersId, devicesId" /> | Retrieves the specified DeviceUser |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="devicesId" /> | Lists/Searches DeviceUsers. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceUsersId, devicesId" /> | Deletes the specified DeviceUser. This also revokes the user's access to device data. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="devicesId" /> | Lists/Searches DeviceUsers. |
| <CopyableCode code="approve" /> | `EXEC` | <CopyableCode code="deviceUsersId, devicesId" /> | Approves device to access user data. |
| <CopyableCode code="block" /> | `EXEC` | <CopyableCode code="deviceUsersId, devicesId" /> | Blocks device from accessing user data |
| <CopyableCode code="cancel_wipe" /> | `EXEC` | <CopyableCode code="deviceUsersId, devicesId" /> | Cancels an unfinished user account wipe. This operation can be used to cancel device wipe in the gap between the wipe operation returning success and the device being wiped. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="devicesId" /> | Looks up resource names of the DeviceUsers associated with the caller's credentials, as well as the properties provided in the request. This method must be called with end-user credentials with the scope: https://www.googleapis.com/auth/cloud-identity.devices.lookup If multiple properties are provided, only DeviceUsers having all of these properties are considered as matches - i.e. the query behaves like an AND. Different platforms require different amounts of information from the caller to ensure that the DeviceUser is uniquely identified. - iOS: No properties need to be passed, the caller's credentials are sufficient to identify the corresponding DeviceUser. - Android: Specifying the 'android_id' field is required. - Desktop: Specifying the 'raw_resource_id' field is required. |
| <CopyableCode code="wipe" /> | `EXEC` | <CopyableCode code="deviceUsersId, devicesId" /> | Wipes the user's account on a device. Other data on the device that is not associated with the user's work account is not affected. For example, if a Gmail app is installed on a device that is used for personal and work purposes, and the user is logged in to the Gmail app with their personal account as well as their work account, wiping the "deviceUser" by their work administrator will not affect their personal account within Gmail or other apps such as Photos. |
