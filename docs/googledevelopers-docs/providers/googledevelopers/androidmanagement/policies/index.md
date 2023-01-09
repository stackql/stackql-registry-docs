---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidmanagement.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the policy in the form enterprises/&#123;enterpriseId&#125;/policies/&#123;policyId&#125;. |
| `outgoingBeamDisabled` | `boolean` | Whether using NFC to beam data from apps is disabled. |
| `permittedAccessibilityServices` | `object` | A list of package names. |
| `adjustVolumeDisabled` | `boolean` | Whether adjusting the master volume is disabled. Also mutes the device. |
| `playStoreMode` | `string` | This mode controls which apps are available to the user in the Play Store and the behavior on the device when apps are removed from the policy. |
| `autoDateAndTimeZone` | `string` | Whether auto date, time, and time zone are enabled on a company-owned device. If this is set, then autoTimeRequired is ignored. |
| `installAppsDisabled` | `boolean` | Whether user installation of apps is disabled. |
| `passwordRequirements` | `object` | Requirements for the password used to unlock a device. |
| `oncCertificateProviders` | `array` | This feature is not generally available. |
| `personalUsagePolicies` | `object` | Policies controlling personal usage on a company-owned device with a work profile. |
| `shortSupportMessage` | `object` | Provides a user-facing message with locale info. The maximum message length is 4096 characters. |
| `blockApplicationsEnabled` | `boolean` | Whether applications other than the ones configured in applications are blocked from being installed. When set, applications that were installed under a previous policy but no longer appear in the policy are automatically uninstalled. |
| `installUnknownSourcesAllowed` | `boolean` | This field has no effect. |
| `crossProfilePolicies` | `object` | Cross-profile policies applied on the device. |
| `microphoneAccess` | `string` | Controls the use of the microphone and whether the user has access to the microphone access toggle. This applies only on fully managed devices. |
| `longSupportMessage` | `object` | Provides a user-facing message with locale info. The maximum message length is 4096 characters. |
| `bluetoothConfigDisabled` | `boolean` | Whether configuring bluetooth is disabled. |
| `mountPhysicalMediaDisabled` | `boolean` | Whether the user mounting physical external media is disabled. |
| `complianceRules` | `array` | Rules declaring which mitigating actions to take when a device is not compliant with its policy. When the conditions for multiple rules are satisfied, all of the mitigating actions for the rules are taken. There is a maximum limit of 100 rules. Use policy enforcement rules instead. |
| `unmuteMicrophoneDisabled` | `boolean` | If microphone_access is set to any value other than MICROPHONE_ACCESS_UNSPECIFIED, this has no effect. Otherwise this field controls whether microphones are disabled: If true, all microphones are disabled, otherwise they are available. This is available only on fully managed devices. |
| `setUserIconDisabled` | `boolean` | Whether changing the user icon is disabled. |
| `permissionGrants` | `array` | Explicit permission or group grants or denials for all apps. These values override the default_permission_policy. |
| `passwordPolicies` | `array` | Password requirement policies. Different policies can be set for work profile or fully managed devices by setting the password_scope field in the policy. |
| `cameraDisabled` | `boolean` | If camera_access is set to any value other than CAMERA_ACCESS_UNSPECIFIED, this has no effect. Otherwise this field controls whether cameras are disabled: If true, all cameras are disabled, otherwise they are available. For fully managed devices this field applies for all apps on the device. For work profiles, this field applies only to apps in the work profile, and the camera access of apps outside the work profile is unaffected. |
| `statusBarDisabled` | `boolean` | Whether the status bar is disabled. This disables notifications, quick settings, and other screen overlays that allow escape from full-screen mode. DEPRECATED. To disable the status bar on a kiosk device, use InstallType KIOSK or kioskCustomLauncherEnabled. |
| `version` | `string` | The version of the policy. This is a read-only field. The version is incremented each time the policy is updated. |
| `maximumTimeToLock` | `string` | Maximum time in milliseconds for user activity until the device locks. A value of 0 means there is no restriction. |
| `usbFileTransferDisabled` | `boolean` | Whether transferring files over USB is disabled. This is supported only on company-owned devices. |
| `systemUpdate` | `object` | Configuration for managing system updates |
| `cellBroadcastsConfigDisabled` | `boolean` | Whether configuring cell broadcast is disabled. |
| `modifyAccountsDisabled` | `boolean` | Whether adding or removing accounts is disabled. |
| `addUserDisabled` | `boolean` | Whether adding new users and profiles is disabled. |
| `androidDevicePolicyTracks` | `array` | The app tracks for Android Device Policy the device can access. The device receives the latest version among all accessible tracks. If no tracks are specified, then the device only uses the production track. |
| `credentialsConfigDisabled` | `boolean` | Whether configuring user credentials is disabled. |
| `funDisabled` | `boolean` | Whether the user is allowed to have fun. Controls whether the Easter egg game in Settings is disabled. |
| `screenCaptureDisabled` | `boolean` | Whether screen capture is disabled. |
| `accountTypesWithManagementDisabled` | `array` | Account types that can't be managed by the user. |
| `autoTimeRequired` | `boolean` | Whether auto time is required, which prevents the user from manually setting the date and time. If autoDateAndTimeZone is set, this field is ignored. |
| `frpAdminEmails` | `array` | Email addresses of device administrators for factory reset protection. When the device is factory reset, it will require one of these admins to log in with the Google account email and password to unlock the device. If no admins are specified, the device won't provide factory reset protection. |
| `createWindowsDisabled` | `boolean` | Whether creating windows besides app windows is disabled. |
| `kioskCustomLauncherEnabled` | `boolean` | Whether the kiosk custom launcher is enabled. This replaces the home screen with a launcher that locks down the device to the apps installed via the applications setting. Apps appear on a single page in alphabetical order. Use kioskCustomization to further configure the kiosk device behavior. |
| `shareLocationDisabled` | `boolean` | Whether location sharing is disabled. share_location_disabled is supported for both fully managed devices and personally owned work profiles. |
| `persistentPreferredActivities` | `array` | Default intent handler activities. |
| `wifiConfigsLockdownEnabled` | `boolean` | DEPRECATED - Use wifi_config_disabled. |
| `mobileNetworksConfigDisabled` | `boolean` | Whether configuring mobile networks is disabled. |
| `defaultPermissionPolicy` | `string` | The default permission policy for runtime permission requests. |
| `networkEscapeHatchEnabled` | `boolean` | Whether the network escape hatch is enabled. If a network connection can't be made at boot time, the escape hatch prompts the user to temporarily connect to a network in order to refresh the device policy. After applying policy, the temporary network will be forgotten and the device will continue booting. This prevents being unable to connect to a network if there is no suitable network in the last policy and the device boots into an app in lock task mode, or the user is otherwise unable to reach device settings.Note: Setting wifiConfigDisabled to true will override this setting under specific circumstances. Please see wifiConfigDisabled for further details. |
| `uninstallAppsDisabled` | `boolean` | Whether user uninstallation of applications is disabled. This prevents apps from being uninstalled, even those removed using applications |
| `bluetoothContactSharingDisabled` | `boolean` | Whether bluetooth contact sharing is disabled. |
| `applications` | `array` | Policy applied to apps. |
| `encryptionPolicy` | `string` | Whether encryption is enabled |
| `alwaysOnVpnPackage` | `object` | Configuration for an always-on VPN connection. |
| `permittedInputMethods` | `object` | A list of package names. |
| `kioskCustomization` | `object` | Settings controlling the behavior of a device in kiosk mode. To enable kiosk mode, set kioskCustomLauncherEnabled to true or specify an app in the policy with installType KIOSK. |
| `stayOnPluggedModes` | `array` | The battery plugged in modes for which the device stays on. When using this setting, it is recommended to clear maximum_time_to_lock so that the device doesn't lock itself while it stays on. |
| `recommendedGlobalProxy` | `object` | Configuration info for an HTTP proxy. For a direct proxy, set the host, port, and excluded_hosts fields. For a PAC script proxy, set the pac_uri field. |
| `statusReportingSettings` | `object` | Settings controlling the behavior of status reports. |
| `deviceOwnerLockScreenInfo` | `object` | Provides a user-facing message with locale info. The maximum message length is 4096 characters. |
| `advancedSecurityOverrides` | `object` | Security policies set to secure values by default. To maintain the security posture of a device, we don't recommend overriding any of the default values. |
| `usbMassStorageEnabled` | `boolean` | Whether USB storage is enabled. Deprecated. |
| `factoryResetDisabled` | `boolean` | Whether factory resetting from settings is disabled. |
| `policyEnforcementRules` | `array` | Rules that define the behavior when a particular policy can not be applied on device |
| `minimumApiLevel` | `integer` | The minimum allowed Android API level. |
| `wifiConfigDisabled` | `boolean` | Whether configuring Wi-Fi access points is disabled. Note: If a network connection can't be made at boot time and configuring Wi-Fi is disabled then network escape hatch will be shown in order to refresh the device policy (see networkEscapeHatchEnabled). |
| `ensureVerifyAppsEnabled` | `boolean` | Whether app verification is force-enabled. |
| `keyguardDisabledFeatures` | `array` | Disabled keyguard customizations, such as widgets. |
| `removeUserDisabled` | `boolean` | Whether removing other users is disabled. |
| `outgoingCallsDisabled` | `boolean` | Whether outgoing calls are disabled. |
| `bluetoothDisabled` | `boolean` | Whether bluetooth is disabled. Prefer this setting over bluetooth_config_disabled because bluetooth_config_disabled can be bypassed by the user. |
| `appAutoUpdatePolicy` | `string` | Deprecated. Use autoUpdateMode instead.When autoUpdateMode is set to AUTO_UPDATE_POSTPONED or AUTO_UPDATE_HIGH_PRIORITY, this field has no effect.The app auto update policy, which controls when automatic app updates can be applied. |
| `locationMode` | `string` | The degree of location detection enabled. |
| `setupActions` | `array` | Action to take during the setup process. At most one action may be specified. |
| `privateKeySelectionEnabled` | `boolean` | Allows showing UI on a device for a user to choose a private key alias if there are no matching rules in ChoosePrivateKeyRules. For devices below Android P, setting this may leave enterprise keys vulnerable. |
| `openNetworkConfiguration` | `object` | Network configuration for the device. See configure networks for more information. |
| `smsDisabled` | `boolean` | Whether sending and receiving SMS messages is disabled. |
| `debuggingFeaturesAllowed` | `boolean` | Whether the user is allowed to enable debugging features. |
| `networkResetDisabled` | `boolean` | Whether resetting network settings is disabled. |
| `tetheringConfigDisabled` | `boolean` | Whether configuring tethering and portable hotspots is disabled. |
| `preferentialNetworkService` | `string` | Controls whether preferential network service is enabled on the work profile. For example, an organization may have an agreement with a carrier that all of the work data from its employees' devices will be sent via a network service dedicated for enterprise use. An example of a supported preferential network service is the enterprise slice on 5G networks. This has no effect on fully managed devices. |
| `cameraAccess` | `string` | Controls the use of the camera and whether the user has access to the camera access toggle. |
| `usageLog` | `object` | Controls types of device activity logs collected from the device and reported via Pub/Sub notification (https://developers.google.com/android/management/notifications). |
| `choosePrivateKeyRules` | `array` | Rules for determining apps' access to private keys. See ChoosePrivateKeyRule for details. |
| `setWallpaperDisabled` | `boolean` | Whether changing the wallpaper is disabled. |
| `safeBootDisabled` | `boolean` | Whether rebooting the device into safe boot is disabled. |
| `dataRoamingDisabled` | `boolean` | Whether roaming data services are disabled. |
| `vpnConfigDisabled` | `boolean` | Whether configuring VPN is disabled. |
| `keyguardDisabled` | `boolean` | If true, this disables the Lock Screen (https://source.android.com/docs/core/display/multi_display/lock-screen) for primary and/or secondary displays. |
| `skipFirstUseHintsEnabled` | `boolean` | Flag to skip hints on the first use. Enterprise admin can enable the system recommendation for apps to skip their user tutorial and other introductory hints on first start-up. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `enterprises_policies_get` | `SELECT` | `enterprisesId, policiesId` | Gets a policy. |
| `enterprises_policies_list` | `SELECT` | `enterprisesId` | Lists policies for a given enterprise. |
| `enterprises_policies_delete` | `DELETE` | `enterprisesId, policiesId` | Deletes a policy. This operation is only permitted if no devices are currently referencing the policy. |
| `enterprises_policies_patch` | `EXEC` | `enterprisesId, policiesId` | Updates or creates a policy. |
