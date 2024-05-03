---
title: recaptcha_v3_config
hide_title: false
hide_table_of_contents: false
keywords:
  - recaptcha_v3_config
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
<tr><td><b>Name</b></td><td><code>recaptcha_v3_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebaseappcheck.recaptcha_v3_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The relative resource name of the reCAPTCHA v3 configuration object, in the format: ``` projects/&#123;project_number&#125;/apps/&#123;app_id&#125;/recaptchaV3Config ``` |
| <CopyableCode code="siteSecret" /> | `string` | Required. Input only. The site secret used to identify your service for reCAPTCHA v3 verification. For security reasons, this field will never be populated in any response. |
| <CopyableCode code="siteSecretSet" /> | `boolean` | Output only. Whether the `site_secret` field was previously set. Since we will never return the `site_secret` field, this field is the only way to find out whether it was previously set. |
| <CopyableCode code="tokenTtl" /> | `string` | Specifies the duration for which App Check tokens exchanged from reCAPTCHA tokens will be valid. If unset, a default value of 1 day is assumed. Must be between 30 minutes and 7 days, inclusive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_apps_recaptchaV3Config_get" /> | `SELECT` | <CopyableCode code="appsId, projectsId" /> | Gets the RecaptchaV3Config for the specified app. For security reasons, the `site_secret` field is never populated in the response. |
| <CopyableCode code="projects_apps_recaptchaV3Config_batchGet" /> | `EXEC` | <CopyableCode code="projectsId" /> | Atomically gets the RecaptchaV3Configs for the specified list of apps. For security reasons, the `site_secret` field is never populated in the response. |
| <CopyableCode code="projects_apps_recaptchaV3Config_patch" /> | `EXEC` | <CopyableCode code="appsId, projectsId" /> | Updates the RecaptchaV3Config for the specified app. While this configuration is incomplete or invalid, the app will be unable to exchange reCAPTCHA tokens for App Check tokens. For security reasons, the `site_secret` field is never populated in the response. |
