---
title: factors
hide_title: false
hide_table_of_contents: false
keywords:
  - factors
  - userfactor
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>factors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.userfactor.factors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `created` | `string` |
| `_links` | `object` |
| `_embedded` | `object` |
| `status` | `string` |
| `lastUpdated` | `string` |
| `factorType` | `string` |
| `provider` | `string` |
| `verify` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `factorId, userId` | Fetches a factor for the specified user |
| `list` | `SELECT` | `userId` | Enumerates all the enrolled factors for the specified user |
| `insert` | `INSERT` | `userId` | Enrolls a user with a supported factor. |
| `delete` | `DELETE` | `factorId, userId` | Unenrolls an existing factor for the specified user, allowing the user to enroll a new factor. |
| `activate` | `EXEC` | `factorId, userId` | The `sms` and `token:software:totp` factor types require activation to complete the enrollment process. |
| `verify` | `EXEC` | `factorId, userId` | Verifies an OTP for a `token` or `token:hardware` factor |
