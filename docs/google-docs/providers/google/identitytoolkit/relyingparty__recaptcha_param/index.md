---
title: relyingparty__recaptcha_param
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty__recaptcha_param
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty__recaptcha_param</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.identitytoolkit.relyingparty__recaptcha_param</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The fixed string "identitytoolkit#GetRecaptchaParamResponse". |
| `recaptchaSiteKey` | `string` | Site key registered at recaptcha. |
| `recaptchaStoken` | `string` | The stoken field for the recaptcha widget, used to request captcha challenge. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `relyingparty_getRecaptchaParam` | `SELECT` |  |
