---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - androidmanagement
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidmanagement.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the device in the form enterprises/&#123;enterpriseId&#125;/devices/&#123;deviceId&#125;. |
| `user` | `object` | A user belonging to an enterprise. |
| `softwareInfo` | `object` | Information about device software. |
| `deviceSettings` | `object` | Information about security related device settings on device. |
| `lastPolicyComplianceReportTime` | `string` | Deprecated. |
| `disabledReason` | `object` | Provides a user-facing message with locale info. The maximum message length is 4096 characters. |
| `commonCriteriaModeInfo` | `object` | Information about Common Criteria Mode—security standards defined in the Common Criteria for Information Technology Security Evaluation (https://www.commoncriteriaportal.org/) (CC).This information is only available if statusReportingSettings.commonCriteriaModeEnabled is true in the device's policy. |
| `enrollmentTime` | `string` | The time of device enrollment. |
| `applicationReports` | `array` | Reports for apps installed on the device. This information is only available when application_reports_enabled is true in the device's policy. |
| `policyCompliant` | `boolean` | Whether the device is compliant with its policy. |
| `nonComplianceDetails` | `array` | Details about policy settings that the device is not compliant with. |
| `managementMode` | `string` | The type of management mode Android Device Policy takes on the device. This influences which policy settings are supported. |
| `ownership` | `string` | Ownership of the managed device. |
| `lastStatusReportTime` | `string` | The last time the device sent a status report. |
| `memoryEvents` | `array` | Events related to memory and storage measurements in chronological order. This information is only available if memoryInfoEnabled is true in the device's policy. |
| `systemProperties` | `object` | Map of selected system properties name and value related to the device. This information is only available if systemPropertiesEnabled is true in the device's policy. |
| `appliedState` | `string` | The state currently applied to the device. |
| `appliedPasswordPolicies` | `array` | The password requirements currently applied to the device. The applied requirements may be slightly different from those specified in passwordPolicies in some cases. fieldPath is set based on passwordPolicies. |
| `powerManagementEvents` | `array` | Power management events on the device in chronological order. This information is only available if powerManagementEventsEnabled is true in the device's policy. |
| `hardwareStatusSamples` | `array` | Hardware status samples in chronological order. This information is only available if hardwareStatusEnabled is true in the device's policy. |
| `state` | `string` | The state to be applied to the device. This field can be modified by a patch request. Note that when calling enterprises.devices.patch, ACTIVE and DISABLED are the only allowable values. To enter the device into a DELETED state, call enterprises.devices.delete. |
| `userName` | `string` | The resource name of the user that owns this device in the form enterprises/&#123;enterpriseId&#125;/users/&#123;userId&#125;. |
| `securityPosture` | `object` | The security posture of the device, as determined by the current device state and the policies applied. |
| `appliedPolicyName` | `string` | The name of the policy currently applied to the device. |
| `hardwareInfo` | `object` | Information about device hardware. The fields related to temperature thresholds are only available if hardwareStatusEnabled is true in the device's policy. |
| `previousDeviceNames` | `array` | If the same physical device has been enrolled multiple times, this field contains its previous device names. The serial number is used as the unique identifier to determine if the same physical device has enrolled previously. The names are in chronological order. |
| `appliedPolicyVersion` | `string` | The version of the policy currently applied to the device. |
| `networkInfo` | `object` | Device network info. |
| `enrollmentTokenName` | `string` | If the device was enrolled with an enrollment token, this field contains the name of the token. |
| `displays` | `array` | Detailed information about displays on the device. This information is only available if displayInfoEnabled is true in the device's policy. |
| `enrollmentTokenData` | `string` | If the device was enrolled with an enrollment token with additional data provided, this field contains that data. |
| `lastPolicySyncTime` | `string` | The last time the device fetched its policy. |
| `memoryInfo` | `object` | Information about device memory and storage. |
| `apiLevel` | `integer` | The API level of the Android platform version running on the device. |
| `policyName` | `string` | The name of the policy applied to the device, in the form enterprises/&#123;enterpriseId&#125;/policies/&#123;policyId&#125;. If not specified, the policy_name for the device's user is applied. This field can be modified by a patch request. You can specify only the policyId when calling enterprises.devices.patch, as long as the policyId doesn’t contain any slashes. The rest of the policy name is inferred. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `enterprises_devices_get` | `SELECT` | `devicesId, enterprisesId` | Gets a device. Deleted devices will respond with a 404 error. |
| `enterprises_devices_list` | `SELECT` | `enterprisesId` | Lists devices for a given enterprise. Deleted devices are not returned in the response. |
| `enterprises_devices_delete` | `DELETE` | `devicesId, enterprisesId` | Deletes a device. This operation wipes the device. Deleted devices do not show up in enterprises.devices.list calls and a 404 is returned from enterprises.devices.get. |
| `enterprises_devices_issueCommand` | `EXEC` | `devicesId, enterprisesId` | Issues a command to a device. The Operation resource returned contains a Command in its metadata field. Use the get operation method to get the status of the command. |
| `enterprises_devices_patch` | `EXEC` | `devicesId, enterprisesId` | Updates a device. |
