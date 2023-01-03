---
title: relyingparty_oob_confirmation_code
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_oob_confirmation_code
  - identitytoolkit
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty_oob_confirmation_code</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.identitytoolkit.relyingparty_oob_confirmation_code</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `oobCode` | `string` | The code to be send to the user. |
| `email` | `string` | The email address that the email is sent to. |
| `kind` | `string` | The fixed string "identitytoolkit#GetOobConfirmationCodeResponse". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `relyingparty_getOobConfirmationCode` | `SELECT` |  |
