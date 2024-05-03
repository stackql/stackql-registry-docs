---
title: emails
hide_title: false
hide_table_of_contents: false
keywords:
  - emails
  - users
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>emails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.users.emails" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="primary" /> | `boolean` |
| <CopyableCode code="verified" /> | `boolean` |
| <CopyableCode code="visibility" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_emails_for_authenticated_user" /> | `SELECT` |  | Lists all of your email addresses, and specifies which one is visible to the public. This endpoint is accessible with the `user:email` scope. |
| <CopyableCode code="add_email_for_authenticated_user" /> | `INSERT` |  | This endpoint is accessible with the `user` scope. |
| <CopyableCode code="delete_email_for_authenticated_user" /> | `DELETE` |  | This endpoint is accessible with the `user` scope. |
| <CopyableCode code="set_primary_email_visibility_for_authenticated_user" /> | `EXEC` | <CopyableCode code="data__visibility" /> | Sets the visibility for your primary email addresses. |
