---
title: okta_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - okta_accounts
  - okta_integration
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>okta_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.okta_integration.okta_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the Okta account, a UUID hash of the account name. |
| <CopyableCode code="attributes" /> | `object` | Attributes object for an Okta account. |
| <CopyableCode code="type" /> | `string` | Account type for an Okta account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_okta_account" /> | `SELECT` | <CopyableCode code="account_id, dd_site" /> | Get an Okta account. |
| <CopyableCode code="list_okta_accounts" /> | `SELECT` | <CopyableCode code="dd_site" /> | List Okta accounts. |
| <CopyableCode code="create_okta_account" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create an Okta account. |
| <CopyableCode code="delete_okta_account" /> | `DELETE` | <CopyableCode code="account_id, dd_site" /> | Delete an Okta account. |
| <CopyableCode code="_get_okta_account" /> | `EXEC` | <CopyableCode code="account_id, dd_site" /> | Get an Okta account. |
| <CopyableCode code="_list_okta_accounts" /> | `EXEC` | <CopyableCode code="dd_site" /> | List Okta accounts. |
| <CopyableCode code="update_okta_account" /> | `EXEC` | <CopyableCode code="account_id, data__data, dd_site" /> | Update an Okta account. |
