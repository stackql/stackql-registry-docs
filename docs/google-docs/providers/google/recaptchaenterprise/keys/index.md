---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - recaptchaenterprise
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the Key in the format "projects/&#123;project&#125;/keys/&#123;key&#125;". |
| <CopyableCode code="androidSettings" /> | `object` | Settings specific to keys that can be used by Android apps. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp corresponding to the creation of this key. |
| <CopyableCode code="displayName" /> | `string` | Human-readable display name of this key. Modifiable by user. |
| <CopyableCode code="iosSettings" /> | `object` | Settings specific to keys that can be used by iOS apps. |
| <CopyableCode code="labels" /> | `object` | See Creating and managing labels. |
| <CopyableCode code="testingOptions" /> | `object` | Options for user acceptance testing. |
| <CopyableCode code="wafSettings" /> | `object` | Settings specific to keys that can be used for WAF (Web Application Firewall). |
| <CopyableCode code="webSettings" /> | `object` | Settings specific to keys that can be used by websites. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keysId, projectsId" /> | Returns the specified key. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns the list of all keys that belong to a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new reCAPTCHA Enterprise key. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keysId, projectsId" /> | Deletes the specified key. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Returns the list of all keys that belong to a project. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="keysId, projectsId" /> | Migrates an existing key from reCAPTCHA to reCAPTCHA Enterprise. Once a key is migrated, it can be used from either product. SiteVerify requests are billed as CreateAssessment calls. You must be authenticated as one of the current owners of the reCAPTCHA Key, and your user must have the reCAPTCHA Enterprise Admin IAM role in the destination project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="keysId, projectsId" /> | Updates the specified key. |
