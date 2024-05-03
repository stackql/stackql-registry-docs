---
title: app_attest_config
hide_title: false
hide_table_of_contents: false
keywords:
  - app_attest_config
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
<tr><td><b>Name</b></td><td><code>app_attest_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebaseappcheck.app_attest_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The relative resource name of the App Attest configuration object, in the format: ``` projects/&#123;project_number&#125;/apps/&#123;app_id&#125;/appAttestConfig ``` |
| <CopyableCode code="tokenTtl" /> | `string` | Specifies the duration for which App Check tokens exchanged from App Attest artifacts will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_apps_appAttestConfig_get" /> | `SELECT` | <CopyableCode code="appsId, projectsId" /> | Gets the AppAttestConfig for the specified app. |
| <CopyableCode code="projects_apps_appAttestConfig_batchGet" /> | `EXEC` | <CopyableCode code="projectsId" /> | Atomically gets the AppAttestConfigs for the specified list of apps. |
| <CopyableCode code="projects_apps_appAttestConfig_patch" /> | `EXEC` | <CopyableCode code="appsId, projectsId" /> | Updates the AppAttestConfig for the specified app. While this configuration is incomplete or invalid, the app will be unable to exchange AppAttest tokens for App Check tokens. |
