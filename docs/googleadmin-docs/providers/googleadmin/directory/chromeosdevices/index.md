---
title: chromeosdevices
hide_title: false
hide_table_of_contents: false
keywords:
  - chromeosdevices
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
<tr><td><b>Name</b></td><td><code>chromeosdevices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.chromeosdevices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activeTimeRanges" /> | `array` | A list of active time ranges (Read-only). |
| <CopyableCode code="annotatedAssetId" /> | `string` | The asset identifier as noted by an administrator or specified during enrollment. |
| <CopyableCode code="annotatedLocation" /> | `string` | The address or location of the device as noted by the administrator. Maximum length is `200` characters. Empty values are allowed. |
| <CopyableCode code="annotatedUser" /> | `string` | The user of the device as noted by the administrator. Maximum length is 100 characters. Empty values are allowed. |
| <CopyableCode code="autoUpdateExpiration" /> | `string` | (Read-only) The timestamp after which the device will stop receiving Chrome updates or support |
| <CopyableCode code="bootMode" /> | `string` | The boot mode for the device. The possible values are: * `Verified`: The device is running a valid version of the Chrome OS. * `Dev`: The devices's developer hardware switch is enabled. When booted, the device has a command line shell. For an example of a developer switch, see the [Chromebook developer information](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/samsung-series-5-chromebook#TOC-Developer-switch). |
| <CopyableCode code="cpuInfo" /> | `array` | Information regarding CPU specs in the device. |
| <CopyableCode code="cpuStatusReports" /> | `array` | Reports of CPU utilization and temperature (Read-only) |
| <CopyableCode code="deprovisionReason" /> | `string` | (Read-only) Deprovision reason. |
| <CopyableCode code="deviceFiles" /> | `array` | A list of device files to download (Read-only) |
| <CopyableCode code="deviceId" /> | `string` | The unique ID of the Chrome device. |
| <CopyableCode code="diskVolumeReports" /> | `array` | Reports of disk space and other info about mounted/connected volumes. |
| <CopyableCode code="dockMacAddress" /> | `string` | (Read-only) Built-in MAC address for the docking station that the device connected to. Factory sets Media access control address (MAC address) assigned for use by a dock. It is reserved specifically for MAC pass through device policy. The format is twelve (12) hexadecimal digits without any delimiter (uppercase letters). This is only relevant for some devices. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="ethernetMacAddress" /> | `string` | The device's MAC address on the ethernet network interface. |
| <CopyableCode code="ethernetMacAddress0" /> | `string` | (Read-only) MAC address used by the Chromebook’s internal ethernet port, and for onboard network (ethernet) interface. The format is twelve (12) hexadecimal digits without any delimiter (uppercase letters). This is only relevant for some devices. |
| <CopyableCode code="firmwareVersion" /> | `string` | The Chrome device's firmware version. |
| <CopyableCode code="firstEnrollmentTime" /> | `string` | Date and time for the first time the device was enrolled. |
| <CopyableCode code="kind" /> | `string` | The type of resource. For the Chromeosdevices resource, the value is `admin#directory#chromeosdevice`. |
| <CopyableCode code="lastDeprovisionTimestamp" /> | `string` | (Read-only) Date and time for the last deprovision of the device. |
| <CopyableCode code="lastEnrollmentTime" /> | `string` | Date and time the device was last enrolled (Read-only) |
| <CopyableCode code="lastKnownNetwork" /> | `array` | Contains last known network (Read-only) |
| <CopyableCode code="lastSync" /> | `string` | Date and time the device was last synchronized with the policy settings in the G Suite administrator control panel (Read-only) |
| <CopyableCode code="macAddress" /> | `string` | The device's wireless MAC address. If the device does not have this information, it is not included in the response. |
| <CopyableCode code="manufactureDate" /> | `string` | (Read-only) The date the device was manufactured in yyyy-mm-dd format. |
| <CopyableCode code="meid" /> | `string` | The Mobile Equipment Identifier (MEID) or the International Mobile Equipment Identity (IMEI) for the 3G mobile card in a mobile device. A MEID/IMEI is typically used when adding a device to a wireless carrier's post-pay service plan. If the device does not have this information, this property is not included in the response. For more information on how to export a MEID/IMEI list, see the [Developer's Guide](/admin-sdk/directory/v1/guides/manage-chrome-devices.html#export_meid). |
| <CopyableCode code="model" /> | `string` | The device's model information. If the device does not have this information, this property is not included in the response. |
| <CopyableCode code="notes" /> | `string` | Notes about this device added by the administrator. This property can be [searched](https://support.google.com/chrome/a/answer/1698333) with the [list](/admin-sdk/directory/v1/reference/chromeosdevices/list) method's `query` parameter. Maximum length is 500 characters. Empty values are allowed. |
| <CopyableCode code="orderNumber" /> | `string` | The device's order number. Only devices directly purchased from Google have an order number. |
| <CopyableCode code="orgUnitId" /> | `string` | The unique ID of the organizational unit. orgUnitPath is the human readable version of orgUnitId. While orgUnitPath may change by renaming an organizational unit within the path, orgUnitId is unchangeable for one organizational unit. This property can be [updated](/admin-sdk/directory/v1/guides/manage-chrome-devices#move_chrome_devices_to_ou) using the API. For more information about how to create an organizational structure for your device, see the [administration help center](https://support.google.com/a/answer/182433). |
| <CopyableCode code="orgUnitPath" /> | `string` | The full parent path with the organizational unit's name associated with the device. Path names are case insensitive. If the parent organizational unit is the top-level organization, it is represented as a forward slash, `/`. This property can be [updated](/admin-sdk/directory/v1/guides/manage-chrome-devices#move_chrome_devices_to_ou) using the API. For more information about how to create an organizational structure for your device, see the [administration help center](https://support.google.com/a/answer/182433). |
| <CopyableCode code="osUpdateStatus" /> | `object` | Contains information regarding the current OS update status. |
| <CopyableCode code="osVersion" /> | `string` | The Chrome device's operating system version. |
| <CopyableCode code="platformVersion" /> | `string` | The Chrome device's platform version. |
| <CopyableCode code="recentUsers" /> | `array` | A list of recent device users, in descending order, by last login time. |
| <CopyableCode code="screenshotFiles" /> | `array` | A list of screenshot files to download. Type is always "SCREENSHOT_FILE". (Read-only) |
| <CopyableCode code="serialNumber" /> | `string` | The Chrome device serial number entered when the device was enabled. This value is the same as the Admin console's *Serial Number* in the *Chrome OS Devices* tab. |
| <CopyableCode code="status" /> | `string` | The status of the device. |
| <CopyableCode code="supportEndDate" /> | `string` | Final date the device will be supported (Read-only) |
| <CopyableCode code="systemRamFreeReports" /> | `array` | Reports of amounts of available RAM memory (Read-only) |
| <CopyableCode code="systemRamTotal" /> | `string` | Total RAM on the device [in bytes] (Read-only) |
| <CopyableCode code="tpmVersionInfo" /> | `object` | Trusted Platform Module (TPM) (Read-only) |
| <CopyableCode code="willAutoRenew" /> | `boolean` | Determines if the device will auto renew its support after the support end date. This is a read-only property. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customerId, deviceId" /> | Retrieves a Chrome OS device's properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customerId" /> | Retrieves a paginated list of Chrome OS devices within an account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customerId" /> | Retrieves a paginated list of Chrome OS devices within an account. |
| <CopyableCode code="action" /> | `EXEC` | <CopyableCode code="customerId, resourceId" /> | Takes an action that affects a Chrome OS Device. This includes deprovisioning, disabling, and re-enabling devices. *Warning:* * Deprovisioning a device will stop device policy syncing and remove device-level printers. After a device is deprovisioned, it must be wiped before it can be re-enrolled. * Lost or stolen devices should use the disable action. * Re-enabling a disabled device will consume a device license. If you do not have sufficient licenses available when completing the re-enable action, you will receive an error. For more information about deprovisioning and disabling devices, visit the [help center](https://support.google.com/chrome/a/answer/3523633). |
| <CopyableCode code="moveDevicesToOu" /> | `EXEC` | <CopyableCode code="customerId, orgUnitPath" /> | Moves or inserts multiple Chrome OS devices to an organizational unit. You can move up to 50 devices at once. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="customerId, deviceId" /> | Updates a device's updatable properties, such as `annotatedUser`, `annotatedLocation`, `notes`, `orgUnitPath`, or `annotatedAssetId`. This method supports [patch semantics](/admin-sdk/directory/v1/guides/performance#patch). |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="customerId, deviceId" /> | Updates a device's updatable properties, such as `annotatedUser`, `annotatedLocation`, `notes`, `orgUnitPath`, or `annotatedAssetId`. |
