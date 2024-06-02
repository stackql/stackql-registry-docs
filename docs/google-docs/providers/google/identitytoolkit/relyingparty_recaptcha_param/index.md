---
title: relyingparty_recaptcha_param
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_recaptcha_param
  - identitytoolkit
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
<tr><td><b>Name</b></td><td><code>relyingparty_recaptcha_param</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="identitytoolkit.relyingparty_recaptcha_param" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The fixed string "identitytoolkit#GetRecaptchaParamResponse". |
| <CopyableCode code="recaptchaSiteKey" /> | `string` | Site key registered at recaptcha. |
| <CopyableCode code="recaptchaStoken" /> | `string` | The stoken field for the recaptcha widget, used to request captcha challenge. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_recaptcha_param" /> | `SELECT` |  |
