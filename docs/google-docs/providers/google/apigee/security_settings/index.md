---
title: security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_settings
  - apigee
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
<tr><td><b>Name</b></td><td><code>security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.security_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Full resource name is always `organizations/&#123;org&#125;/securitySettings`. |
| <CopyableCode code="mlRetrainingFeedbackEnabled" /> | `boolean` | Optional. If true the user consents to the use of ML models for Abuse detection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_get_security_settings" /> | `SELECT` | <CopyableCode code="organizationsId" /> | GetSecuritySettings gets the security settings for API Security. |
| <CopyableCode code="organizations_update_security_settings" /> | `EXEC` | <CopyableCode code="organizationsId" /> | UpdateSecuritySettings updates the current security settings for API Security. |
