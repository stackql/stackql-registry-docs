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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>relyingparty</code> resource or lists <code>relyingparty</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.identitytoolkit.relyingparty" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="download_account" /> | `EXEC` | <CopyableCode code="" /> | Batch download user accounts. |
| <CopyableCode code="email_link_signin" /> | `EXEC` | <CopyableCode code="" /> | Reset password for a user. |
| <CopyableCode code="reset_password" /> | `EXEC` | <CopyableCode code="" /> | Reset password for a user. |
| <CopyableCode code="send_verification_code" /> | `EXEC` | <CopyableCode code="" /> | Send SMS verification code. |
| <CopyableCode code="set_account_info" /> | `EXEC` | <CopyableCode code="" /> | Set account info for a user. |
| <CopyableCode code="set_project_config" /> | `EXEC` | <CopyableCode code="" /> | Set project configuration. |
| <CopyableCode code="sign_out_user" /> | `EXEC` | <CopyableCode code="" /> | Sign out user. |
| <CopyableCode code="signup_new_user" /> | `EXEC` | <CopyableCode code="" /> | Signup new user. |
| <CopyableCode code="upload_account" /> | `EXEC` | <CopyableCode code="" /> | Batch upload existing user accounts. |
| <CopyableCode code="verify_assertion" /> | `EXEC` | <CopyableCode code="" /> | Verifies the assertion returned by the IdP. |
| <CopyableCode code="verify_custom_token" /> | `EXEC` | <CopyableCode code="" /> | Verifies the developer asserted ID token. |
| <CopyableCode code="verify_password" /> | `EXEC` | <CopyableCode code="" /> | Verifies the user entered password. |
| <CopyableCode code="verify_phone_number" /> | `EXEC` | <CopyableCode code="" /> | Verifies ownership of a phone number and creates/updates the user account accordingly. |
