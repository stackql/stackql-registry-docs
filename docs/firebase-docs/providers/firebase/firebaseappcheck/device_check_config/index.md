---
title: device_check_config
hide_title: false
hide_table_of_contents: false
keywords:
  - device_check_config
  - firebaseappcheck
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_check_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebaseappcheck.device_check_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The relative resource name of the DeviceCheck configuration object, in the format: ``` projects/&#123;project_number&#125;/apps/&#123;app_id&#125;/deviceCheckConfig ``` |
| <CopyableCode code="keyId" /> | `string` | Required. The key identifier of a private key enabled with DeviceCheck, created in your Apple Developer account. |
| <CopyableCode code="privateKey" /> | `string` | Required. Input only. The contents of the private key (`.p8`) file associated with the key specified by `key_id`. For security reasons, this field will never be populated in any response. |
| <CopyableCode code="privateKeySet" /> | `boolean` | Output only. Whether the `private_key` field was previously set. Since we will never return the `private_key` field, this field is the only way to find out whether it was previously set. |
| <CopyableCode code="tokenTtl" /> | `string` | Specifies the duration for which App Check tokens exchanged from DeviceCheck tokens will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_apps_deviceCheckConfig_get" /> | `SELECT` | <CopyableCode code="appsId, projectsId" /> | Gets the DeviceCheckConfig for the specified app. For security reasons, the `private_key` field is never populated in the response. |
| <CopyableCode code="projects_apps_deviceCheckConfig_batchGet" /> | `EXEC` | <CopyableCode code="projectsId" /> | Atomically gets the DeviceCheckConfigs for the specified list of apps. For security reasons, the `private_key` field is never populated in the response. |
| <CopyableCode code="projects_apps_deviceCheckConfig_patch" /> | `EXEC` | <CopyableCode code="appsId, projectsId" /> | Updates the DeviceCheckConfig for the specified app. While this configuration is incomplete or invalid, the app will be unable to exchange DeviceCheck tokens for App Check tokens. For security reasons, the `private_key` field is never populated in the response. |
