---
title: verification_codes
hide_title: false
hide_table_of_contents: false
keywords:
  - verification_codes
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verification_codes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.verification_codes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `userId` | `string` | The obfuscated unique ID of the user. |
| `verificationCode` | `string` | A current verification code for the user. Invalidated or used verification codes are not returned as part of the result. |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | The type of the resource. This is always `admin#directory#verificationCode`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `userKey` | Returns the current set of valid backup verification codes for the specified user. |
| `generate` | `EXEC` | `userKey` | Generates new backup verification codes for the user. |
| `invalidate` | `EXEC` | `userKey` | Invalidates the current backup verification codes for the user. |
