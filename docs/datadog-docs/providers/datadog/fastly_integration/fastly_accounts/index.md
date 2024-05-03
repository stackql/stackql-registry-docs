---
title: fastly_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - fastly_accounts
  - fastly_integration
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
<tr><td><b>Name</b></td><td><code>fastly_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.fastly_integration.fastly_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the Fastly account, a hash of the account name. |
| <CopyableCode code="attributes" /> | `object` | Attributes object of a Fastly account. |
| <CopyableCode code="type" /> | `string` | The JSON:API type for this API. Should always be `fastly-accounts`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_fastly_account" /> | `SELECT` | <CopyableCode code="account_id, dd_site" /> | Get a Fastly account. |
| <CopyableCode code="list_fastly_accounts" /> | `SELECT` | <CopyableCode code="dd_site" /> | List Fastly accounts. |
| <CopyableCode code="create_fastly_account" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a Fastly account. |
| <CopyableCode code="delete_fastly_account" /> | `DELETE` | <CopyableCode code="account_id, dd_site" /> | Delete a Fastly account. |
| <CopyableCode code="_get_fastly_account" /> | `EXEC` | <CopyableCode code="account_id, dd_site" /> | Get a Fastly account. |
| <CopyableCode code="_list_fastly_accounts" /> | `EXEC` | <CopyableCode code="dd_site" /> | List Fastly accounts. |
| <CopyableCode code="update_fastly_account" /> | `EXEC` | <CopyableCode code="account_id, data__data, dd_site" /> | Update a Fastly account. |
