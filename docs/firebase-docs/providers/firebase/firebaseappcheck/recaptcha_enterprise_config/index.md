---
title: recaptcha_enterprise_config
hide_title: false
hide_table_of_contents: false
keywords:
  - recaptcha_enterprise_config
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
<tr><td><b>Name</b></td><td><code>recaptcha_enterprise_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebaseappcheck.recaptcha_enterprise_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The relative resource name of the reCAPTCHA Enterprise configuration object, in the format: ``` projects/&#123;project_number&#125;/apps/&#123;app_id&#125;/recaptchaEnterpriseConfig ``` |
| <CopyableCode code="siteKey" /> | `string` | The score-based site key [created in reCAPTCHA Enterprise](https://cloud.google.com/recaptcha-enterprise/docs/create-key#creating_a_site_key) used to [invoke reCAPTCHA and generate the reCAPTCHA tokens](https://cloud.google.com/recaptcha-enterprise/docs/instrument-web-pages) for your application. Important: This is *not* the `site_secret` (as it is in reCAPTCHA v3), but rather your score-based reCAPTCHA Enterprise site key. |
| <CopyableCode code="tokenTtl" /> | `string` | Specifies the duration for which App Check tokens exchanged from reCAPTCHA Enterprise tokens will be valid. If unset, a default value of 1 hour is assumed. Must be between 30 minutes and 7 days, inclusive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_apps_recaptchaEnterpriseConfig_get" /> | `SELECT` | <CopyableCode code="appsId, projectsId" /> | Gets the RecaptchaEnterpriseConfig for the specified app. |
| <CopyableCode code="projects_apps_recaptchaEnterpriseConfig_batchGet" /> | `EXEC` | <CopyableCode code="projectsId" /> | Atomically gets the RecaptchaEnterpriseConfigs for the specified list of apps. |
| <CopyableCode code="projects_apps_recaptchaEnterpriseConfig_patch" /> | `EXEC` | <CopyableCode code="appsId, projectsId" /> | Updates the RecaptchaEnterpriseConfig for the specified app. While this configuration is incomplete or invalid, the app will be unable to exchange reCAPTCHA Enterprise tokens for App Check tokens. |
