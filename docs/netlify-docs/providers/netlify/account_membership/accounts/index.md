---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - account_membership
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.account_membership.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="billing_details" /> | `string` |
| <CopyableCode code="billing_email" /> | `string` |
| <CopyableCode code="billing_name" /> | `string` |
| <CopyableCode code="billing_period" /> | `string` |
| <CopyableCode code="capabilities" /> | `object` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="owner_ids" /> | `array` |
| <CopyableCode code="payment_method_id" /> | `string` |
| <CopyableCode code="roles_allowed" /> | `array` |
| <CopyableCode code="slug" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="type_id" /> | `string` |
| <CopyableCode code="type_name" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getAccount" /> | `SELECT` | <CopyableCode code="account_id" /> |
| <CopyableCode code="listAccountsForUser" /> | `SELECT` |  |
| <CopyableCode code="createAccount" /> | `INSERT` | <CopyableCode code="data__name, data__type_id" /> |
| <CopyableCode code="cancelAccount" /> | `EXEC` | <CopyableCode code="account_id" /> |
| <CopyableCode code="updateAccount" /> | `EXEC` | <CopyableCode code="account_id" /> |
