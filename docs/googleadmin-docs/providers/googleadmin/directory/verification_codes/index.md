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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verification_codes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.verification_codes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="kind" /> | `string` | The type of the resource. This is always `admin#directory#verificationCode`. |
| <CopyableCode code="userId" /> | `string` | The obfuscated unique ID of the user. |
| <CopyableCode code="verificationCode" /> | `string` | A current verification code for the user. Invalidated or used verification codes are not returned as part of the result. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="userKey" /> | Returns the current set of valid backup verification codes for the specified user. |
| <CopyableCode code="generate" /> | `EXEC` | <CopyableCode code="userKey" /> | Generates new backup verification codes for the user. |
| <CopyableCode code="invalidate" /> | `EXEC` | <CopyableCode code="userKey" /> | Invalidates the current backup verification codes for the user. |
