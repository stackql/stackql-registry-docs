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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mobiledevices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.mobiledevices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `array` | The list of the owner's user names. If your application needs the current list of device owner names, use the [get](/admin-sdk/directory/v1/reference/mobiledevices/get.html) method. For more information about retrieving mobile device user information, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-users#get_user). |
| `deviceCompromisedStatus` | `string` | The compromised device status. |
| `wifiMacAddress` | `string` | The device's MAC address on Wi-Fi networks. |
| `supportsWorkProfile` | `boolean` | Work profile supported on device (Read-only) |
| `hardwareId` | `string` | The IMEI/MEID unique identifier for Android hardware. It is not applicable to Google Sync devices. When adding an Android mobile device, this is an optional property. When updating one of these devices, this is a read-only property. |
| `etag` | `string` | ETag of the resource. |
| `buildNumber` | `string` | The device's operating system build number. |
| `managedAccountIsOnOwnerProfile` | `boolean` | Boolean indicating if this account is on owner/primary profile or not. |
| `devicePasswordStatus` | `string` | DevicePasswordStatus (Read-only) |
| `hardware` | `string` | Mobile Device Hardware (Read-only) |
| `status` | `string` | The device's status. |
| `email` | `array` | The list of the owner's email addresses. If your application needs the current list of user emails, use the [get](/admin-sdk/directory/v1/reference/mobiledevices/get.html) method. For additional information, see the [retrieve a user](/admin-sdk/directory/v1/guides/manage-users#get_user) method. |
| `lastSync` | `string` | Date and time the device was last synchronized with the policy settings in the G Suite administrator control panel (Read-only) |
| `developerOptionsStatus` | `boolean` | Developer options enabled or disabled on device (Read-only) |
| `securityPatchLevel` | `string` | Mobile Device Security patch level (Read-only) |
| `bootloaderVersion` | `string` | Mobile Device Bootloader version (Read-only) |
| `type` | `string` | The type of mobile device. |
| `defaultLanguage` | `string` | The default locale used on the device. |
| `releaseVersion` | `string` | Mobile Device release version version (Read-only) |
| `kernelVersion` | `string` | The device's kernel version. |
| `otherAccountsInfo` | `array` | The list of accounts added on device (Read-only) |
| `imei` | `string` | The device's IMEI number. |
| `kind` | `string` | The type of the API resource. For Mobiledevices resources, the value is `admin#directory#mobiledevice`. |
| `model` | `string` | The mobile device's model name, for example Nexus S. This property can be [updated](/admin-sdk/directory/v1/reference/mobiledevices/update.html). For more information, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-mobile=devices#update_mobile_device). |
| `manufacturer` | `string` | Mobile Device manufacturer (Read-only) |
| `os` | `string` | The mobile device's operating system, for example IOS 4.3 or Android 2.3.5. This property can be [updated](/admin-sdk/directory/v1/reference/mobiledevices/update.html). For more information, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-mobile-devices#update_mobile_device). |
| `meid` | `string` | The device's MEID number. |
| `privilege` | `string` | DMAgentPermission (Read-only) |
| `adbStatus` | `boolean` | Adb (USB debugging) enabled or disabled on device (Read-only) |
| `brand` | `string` | Mobile Device Brand (Read-only) |
| `unknownSourcesStatus` | `boolean` | Unknown sources enabled or disabled on device (Read-only) |
| `basebandVersion` | `string` | The device's baseband version. |
| `encryptionStatus` | `string` | Mobile Device Encryption Status (Read-only) |
| `userAgent` | `string` | Gives information about the device such as `os` version. This property can be [updated](/admin-sdk/directory/v1/reference/mobiledevices/update.html). For more information, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-mobile-devices#update_mobile_device). |
| `firstSync` | `string` | Date and time the device was first synchronized with the policy settings in the G Suite administrator control panel (Read-only) |
| `networkOperator` | `string` | Mobile Device mobile or network operator (if available) (Read-only) |
| `resourceId` | `string` | The unique ID the API service uses to identify the mobile device. |
| `applications` | `array` | The list of applications installed on an Android mobile device. It is not applicable to Google Sync and iOS devices. The list includes any Android applications that access Google Workspace data. When updating an applications list, it is important to note that updates replace the existing list. If the Android device has two existing applications and the API updates the list with five applications, the is now the updated list of five applications. |
| `serialNumber` | `string` | The device's serial number. |
| `deviceId` | `string` | The serial number for a Google Sync mobile device. For Android and iOS devices, this is a software generated unique identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customerId, resourceId` | Retrieves a mobile device's properties. |
| `list` | `SELECT` | `customerId` | Retrieves a paginated list of all user-owned mobile devices for an account. To retrieve a list that includes company-owned devices, use the Cloud Identity [Devices API](https://cloud.google.com/identity/docs/concepts/overview-devices) instead. This method times out after 60 minutes. For more information, see [Troubleshoot error codes](https://developers.google.com/admin-sdk/directory/v1/guides/troubleshoot-error-codes). |
| `delete` | `DELETE` | `customerId, resourceId` | Removes a mobile device. |
| `_list` | `EXEC` | `customerId` | Retrieves a paginated list of all user-owned mobile devices for an account. To retrieve a list that includes company-owned devices, use the Cloud Identity [Devices API](https://cloud.google.com/identity/docs/concepts/overview-devices) instead. This method times out after 60 minutes. For more information, see [Troubleshoot error codes](https://developers.google.com/admin-sdk/directory/v1/guides/troubleshoot-error-codes). |
| `action` | `EXEC` | `customerId, resourceId` | Takes an action that affects a mobile device. For example, remotely wiping a device. |
