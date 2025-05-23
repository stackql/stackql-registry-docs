---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.devices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device}`, where device is the unique id assigned to the Device. |
| <CopyableCode code="androidSpecificAttributes" /> | `object` | Resource representing the Android specific attributes of a Device. |
| <CopyableCode code="assetTag" /> | `string` | Asset tag of the device. |
| <CopyableCode code="basebandVersion" /> | `string` | Output only. Baseband version of the device. |
| <CopyableCode code="bootloaderVersion" /> | `string` | Output only. Device bootloader version. Example: 0.6.7. |
| <CopyableCode code="brand" /> | `string` | Output only. Device brand. Example: Samsung. |
| <CopyableCode code="buildNumber" /> | `string` | Output only. Build number of the device. |
| <CopyableCode code="compromisedState" /> | `string` | Output only. Represents whether the Device is compromised. |
| <CopyableCode code="createTime" /> | `string` | Output only. When the Company-Owned device was imported. This field is empty for BYOD devices. |
| <CopyableCode code="deviceId" /> | `string` | Unique identifier for the device. |
| <CopyableCode code="deviceType" /> | `string` | Output only. Type of device. |
| <CopyableCode code="enabledDeveloperOptions" /> | `boolean` | Output only. Whether developer options is enabled on device. |
| <CopyableCode code="enabledUsbDebugging" /> | `boolean` | Output only. Whether USB debugging is enabled on device. |
| <CopyableCode code="encryptionState" /> | `string` | Output only. Device encryption state. |
| <CopyableCode code="endpointVerificationSpecificAttributes" /> | `object` | Resource representing the [Endpoint Verification-specific attributes](https://cloud.google.com/endpoint-verification/docs/device-information) of a device. |
| <CopyableCode code="hostname" /> | `string` | Host name of the device. |
| <CopyableCode code="imei" /> | `string` | Output only. IMEI number of device if GSM device; empty otherwise. |
| <CopyableCode code="kernelVersion" /> | `string` | Output only. Kernel version of the device. |
| <CopyableCode code="lastSyncTime" /> | `string` | Most recent time when device synced with this service. |
| <CopyableCode code="managementState" /> | `string` | Output only. Management state of the device |
| <CopyableCode code="manufacturer" /> | `string` | Output only. Device manufacturer. Example: Motorola. |
| <CopyableCode code="meid" /> | `string` | Output only. MEID number of device if CDMA device; empty otherwise. |
| <CopyableCode code="model" /> | `string` | Output only. Model name of device. Example: Pixel 3. |
| <CopyableCode code="networkOperator" /> | `string` | Output only. Mobile or network operator of device, if available. |
| <CopyableCode code="osVersion" /> | `string` | Output only. OS version of the device. Example: Android 8.1.0. |
| <CopyableCode code="otherAccounts" /> | `array` | Output only. Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if |ownership_privilege| is |PROFILE_OWNER| or |DEVICE_OWNER|. Does not include the account signed in to the device policy app if that account's domain has only one account. Examples: "com.example", "xyz.com". |
| <CopyableCode code="ownerType" /> | `string` | Output only. Whether the device is owned by the company or an individual |
| <CopyableCode code="releaseVersion" /> | `string` | Output only. OS release version. Example: 6.0. |
| <CopyableCode code="securityPatchTime" /> | `string` | Output only. OS security patch update time on device. |
| <CopyableCode code="serialNumber" /> | `string` | Serial Number of device. Example: HT82V1A01076. |
| <CopyableCode code="unifiedDeviceId" /> | `string` | Output only. Unified device id of the device. |
| <CopyableCode code="wifiMacAddresses" /> | `array` | WiFi MAC addresses of device. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devicesId" /> | Retrieves the specified device. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists/Searches devices. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a device. Only company-owned device may be created. **Note**: This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devicesId" /> | Deletes the specified device. |
| <CopyableCode code="cancel_wipe" /> | `EXEC` | <CopyableCode code="devicesId" /> | Cancels an unfinished device wipe. This operation can be used to cancel device wipe in the gap between the wipe operation returning success and the device being wiped. This operation is possible when the device is in a "pending wipe" state. The device enters the "pending wipe" state when a wipe device command is issued, but has not yet been sent to the device. The cancel wipe will fail if the wipe command has already been issued to the device. |
| <CopyableCode code="wipe" /> | `EXEC` | <CopyableCode code="devicesId" /> | Wipes all data on the specified device. |

## `SELECT` examples

Lists/Searches devices.

```sql
SELECT
name,
androidSpecificAttributes,
assetTag,
basebandVersion,
bootloaderVersion,
brand,
buildNumber,
compromisedState,
createTime,
deviceId,
deviceType,
enabledDeveloperOptions,
enabledUsbDebugging,
encryptionState,
endpointVerificationSpecificAttributes,
hostname,
imei,
kernelVersion,
lastSyncTime,
managementState,
manufacturer,
meid,
model,
networkOperator,
osVersion,
otherAccounts,
ownerType,
releaseVersion,
securityPatchTime,
serialNumber,
unifiedDeviceId,
wifiMacAddresses
FROM google.cloudidentity.devices
;
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>devices</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.cloudidentity.devices (
lastSyncTime,
serialNumber,
assetTag,
wifiMacAddresses,
deviceId,
hostname
)
SELECT 
'{{ lastSyncTime }}',
'{{ serialNumber }}',
'{{ assetTag }}',
'{{ wifiMacAddresses }}',
'{{ deviceId }}',
'{{ hostname }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: lastSyncTime
      value: string
    - name: ownerType
      value: string
    - name: model
      value: string
    - name: osVersion
      value: string
    - name: deviceType
      value: string
    - name: serialNumber
      value: string
    - name: assetTag
      value: string
    - name: imei
      value: string
    - name: meid
      value: string
    - name: wifiMacAddresses
      value:
        - string
    - name: networkOperator
      value: string
    - name: manufacturer
      value: string
    - name: releaseVersion
      value: string
    - name: brand
      value: string
    - name: buildNumber
      value: string
    - name: kernelVersion
      value: string
    - name: basebandVersion
      value: string
    - name: enabledDeveloperOptions
      value: boolean
    - name: otherAccounts
      value:
        - string
    - name: enabledUsbDebugging
      value: boolean
    - name: securityPatchTime
      value: string
    - name: bootloaderVersion
      value: string
    - name: encryptionState
      value: string
    - name: androidSpecificAttributes
      value:
        - name: enabledUnknownSources
          value: boolean
        - name: supportsWorkProfile
          value: boolean
        - name: ownerProfileAccount
          value: boolean
        - name: ownershipPrivilege
          value: string
        - name: verifiedBoot
          value: boolean
        - name: ctsProfileMatch
          value: boolean
        - name: verifyAppsEnabled
          value: boolean
        - name: hasPotentiallyHarmfulApps
          value: boolean
    - name: managementState
      value: string
    - name: compromisedState
      value: string
    - name: deviceId
      value: string
    - name: unifiedDeviceId
      value: string
    - name: endpointVerificationSpecificAttributes
      value:
        - name: certificateAttributes
          value:
            - - name: fingerprint
                value: string
              - name: thumbprint
                value: string
              - name: validationState
                value: string
              - name: serialNumber
                value: string
              - name: validityStartTime
                value: string
              - name: validityExpirationTime
                value: string
              - name: issuer
                value: string
              - name: subject
                value: string
              - name: certificateTemplate
                value:
                  - name: id
                    value: string
                  - name: majorVersion
                    value: integer
                  - name: minorVersion
                    value: integer
        - name: browserAttributes
          value:
            - - name: lastProfileSyncTime
                value: string
              - name: chromeBrowserInfo
                value:
                  - name: browserVersion
                    value: string
                  - name: browserManagementState
                    value: string
                  - name: isFileUploadAnalysisEnabled
                    value: boolean
                  - name: isFileDownloadAnalysisEnabled
                    value: boolean
                  - name: isBulkDataEntryAnalysisEnabled
                    value: boolean
                  - name: isSecurityEventAnalysisEnabled
                    value: boolean
                  - name: isRealtimeUrlCheckEnabled
                    value: boolean
                  - name: safeBrowsingProtectionLevel
                    value: string
                  - name: isSiteIsolationEnabled
                    value: boolean
                  - name: isBuiltInDnsClientEnabled
                    value: boolean
                  - name: passwordProtectionWarningTrigger
                    value: string
                  - name: isChromeRemoteDesktopAppBlocked
                    value: boolean
                  - name: isChromeCleanupEnabled
                    value: boolean
                  - name: isThirdPartyBlockingEnabled
                    value: boolean
              - name: chromeProfileId
                value: string
        - name: additionalSignals
          value: object
    - name: hostname
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>devices</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudidentity.devices
WHERE devicesId = '{{ devicesId }}';
```
