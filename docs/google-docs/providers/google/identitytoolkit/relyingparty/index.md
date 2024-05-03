---
title: relyingparty
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty
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
<tr><td><b>Name</b></td><td><code>relyingparty</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.identitytoolkit.relyingparty" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="download_account" /> | `EXEC` |  | Batch download user accounts. |
| <CopyableCode code="email_link_signin" /> | `EXEC` |  | Reset password for a user. |
| <CopyableCode code="reset_password" /> | `EXEC` |  | Reset password for a user. |
| <CopyableCode code="send_verification_code" /> | `EXEC` |  | Send SMS verification code. |
| <CopyableCode code="set_account_info" /> | `EXEC` |  | Set account info for a user. |
| <CopyableCode code="set_project_config" /> | `EXEC` |  | Set project configuration. |
| <CopyableCode code="sign_out_user" /> | `EXEC` |  | Sign out user. |
| <CopyableCode code="signup_new_user" /> | `EXEC` |  | Signup new user. |
| <CopyableCode code="upload_account" /> | `EXEC` |  | Batch upload existing user accounts. |
| <CopyableCode code="verify_assertion" /> | `EXEC` |  | Verifies the assertion returned by the IdP. |
| <CopyableCode code="verify_custom_token" /> | `EXEC` |  | Verifies the developer asserted ID token. |
| <CopyableCode code="verify_password" /> | `EXEC` |  | Verifies the user entered password. |
| <CopyableCode code="verify_phone_number" /> | `EXEC` |  | Verifies ownership of a phone number and creates/updates the user account accordingly. |
