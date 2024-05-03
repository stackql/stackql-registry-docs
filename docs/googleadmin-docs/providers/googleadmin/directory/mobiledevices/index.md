---
title: mobiledevices
hide_title: false
hide_table_of_contents: false
keywords:
  - mobiledevices
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mobiledevices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.mobiledevices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `array` | The list of the owner's user names. If your application needs the current list of device owner names, use the [get](/admin-sdk/directory/v1/reference/mobiledevices/get.html) method. For more information about retrieving mobile device user information, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-users#get_user). |
| <CopyableCode code="adbStatus" /> | `boolean` | Adb (USB debugging) enabled or disabled on device (Read-only) |
| <CopyableCode code="applications" /> | `array` | The list of applications installed on an Android mobile device. It is not applicable to Google Sync and iOS devices. The list includes any Android applications that access Google Workspace data. When updating an applications list, it is important to note that updates replace the existing list. If the Android device has two existing applications and the API updates the list with five applications, the is now the updated list of five applications. |
| <CopyableCode code="basebandVersion" /> | `string` | The device's baseband version. |
| <CopyableCode code="bootloaderVersion" /> | `string` | Mobile Device Bootloader version (Read-only) |
| <CopyableCode code="brand" /> | `string` | Mobile Device Brand (Read-only) |
| <CopyableCode code="buildNumber" /> | `string` | The device's operating system build number. |
| <CopyableCode code="defaultLanguage" /> | `string` | The default locale used on the device. |
| <CopyableCode code="developerOptionsStatus" /> | `boolean` | Developer options enabled or disabled on device (Read-only) |
| <CopyableCode code="deviceCompromisedStatus" /> | `string` | The compromised device status. |
| <CopyableCode code="deviceId" /> | `string` | The serial number for a Google Sync mobile device. For Android and iOS devices, this is a software generated unique identifier. |
| <CopyableCode code="devicePasswordStatus" /> | `string` | DevicePasswordStatus (Read-only) |
| <CopyableCode code="email" /> | `array` | The list of the owner's email addresses. If your application needs the current list of user emails, use the [get](/admin-sdk/directory/v1/reference/mobiledevices/get.html) method. For additional information, see the [retrieve a user](/admin-sdk/directory/v1/guides/manage-users#get_user) method. |
| <CopyableCode code="encryptionStatus" /> | `string` | Mobile Device Encryption Status (Read-only) |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="firstSync" /> | `string` | Date and time the device was first synchronized with the policy settings in the G Suite administrator control panel (Read-only) |
| <CopyableCode code="hardware" /> | `string` | Mobile Device Hardware (Read-only) |
| <CopyableCode code="hardwareId" /> | `string` | The IMEI/MEID unique identifier for Android hardware. It is not applicable to Google Sync devices. When adding an Android mobile device, this is an optional property. When updating one of these devices, this is a read-only property. |
| <CopyableCode code="imei" /> | `string` | The device's IMEI number. |
| <CopyableCode code="kernelVersion" /> | `string` | The device's kernel version. |
| <CopyableCode code="kind" /> | `string` | The type of the API resource. For Mobiledevices resources, the value is `admin#directory#mobiledevice`. |
| <CopyableCode code="lastSync" /> | `string` | Date and time the device was last synchronized with the policy settings in the G Suite administrator control panel (Read-only) |
| <CopyableCode code="managedAccountIsOnOwnerProfile" /> | `boolean` | Boolean indicating if this account is on owner/primary profile or not. |
| <CopyableCode code="manufacturer" /> | `string` | Mobile Device manufacturer (Read-only) |
| <CopyableCode code="meid" /> | `string` | The device's MEID number. |
| <CopyableCode code="model" /> | `string` | The mobile device's model name, for example Nexus S. This property can be [updated](/admin-sdk/directory/v1/reference/mobiledevices/update.html). For more information, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-mobile=devices#update_mobile_device). |
| <CopyableCode code="networkOperator" /> | `string` | Mobile Device mobile or network operator (if available) (Read-only) |
| <CopyableCode code="os" /> | `string` | The mobile device's operating system, for example IOS 4.3 or Android 2.3.5. This property can be [updated](/admin-sdk/directory/v1/reference/mobiledevices/update.html). For more information, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-mobile-devices#update_mobile_device). |
| <CopyableCode code="otherAccountsInfo" /> | `array` | The list of accounts added on device (Read-only) |
| <CopyableCode code="privilege" /> | `string` | DMAgentPermission (Read-only) |
| <CopyableCode code="releaseVersion" /> | `string` | Mobile Device release version version (Read-only) |
| <CopyableCode code="resourceId" /> | `string` | The unique ID the API service uses to identify the mobile device. |
| <CopyableCode code="securityPatchLevel" /> | `string` | Mobile Device Security patch level (Read-only) |
| <CopyableCode code="serialNumber" /> | `string` | The device's serial number. |
| <CopyableCode code="status" /> | `string` | The device's status. |
| <CopyableCode code="supportsWorkProfile" /> | `boolean` | Work profile supported on device (Read-only) |
| <CopyableCode code="type" /> | `string` | The type of mobile device. |
| <CopyableCode code="unknownSourcesStatus" /> | `boolean` | Unknown sources enabled or disabled on device (Read-only) |
| <CopyableCode code="userAgent" /> | `string` | Gives information about the device such as `os` version. This property can be [updated](/admin-sdk/directory/v1/reference/mobiledevices/update.html). For more information, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-mobile-devices#update_mobile_device). |
| <CopyableCode code="wifiMacAddress" /> | `string` | The device's MAC address on Wi-Fi networks. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customerId, resourceId" /> | Retrieves a mobile device's properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customerId" /> | Retrieves a paginated list of all user-owned mobile devices for an account. To retrieve a list that includes company-owned devices, use the Cloud Identity [Devices API](https://cloud.google.com/identity/docs/concepts/overview-devices) instead. This method times out after 60 minutes. For more information, see [Troubleshoot error codes](https://developers.google.com/admin-sdk/directory/v1/guides/troubleshoot-error-codes). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customerId, resourceId" /> | Removes a mobile device. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customerId" /> | Retrieves a paginated list of all user-owned mobile devices for an account. To retrieve a list that includes company-owned devices, use the Cloud Identity [Devices API](https://cloud.google.com/identity/docs/concepts/overview-devices) instead. This method times out after 60 minutes. For more information, see [Troubleshoot error codes](https://developers.google.com/admin-sdk/directory/v1/guides/troubleshoot-error-codes). |
| <CopyableCode code="action" /> | `EXEC` | <CopyableCode code="customerId, resourceId" /> | Takes an action that affects a mobile device. For example, remotely wiping a device. |
