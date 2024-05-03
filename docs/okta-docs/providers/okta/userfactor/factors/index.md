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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>factors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.userfactor.factors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="factorType" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="provider" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="verify" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factorId, userId, subdomain" /> | Fetches a factor for the specified user |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="userId, subdomain" /> | Enumerates all the enrolled factors for the specified user |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="userId, subdomain" /> | Enrolls a user with a supported factor. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="factorId, userId, subdomain" /> | Unenrolls an existing factor for the specified user, allowing the user to enroll a new factor. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="factorId, userId, subdomain" /> | The `sms` and `token:software:totp` factor types require activation to complete the enrollment process. |
| <CopyableCode code="verify" /> | `EXEC` | <CopyableCode code="factorId, userId, subdomain" /> | Verifies an OTP for a `token` or `token:hardware` factor |
