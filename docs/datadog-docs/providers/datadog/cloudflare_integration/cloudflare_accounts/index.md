---
title: cloudflare_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - cloudflare_accounts
  - cloudflare_integration
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
<tr><td><b>Name</b></td><td><code>cloudflare_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.cloudflare_integration.cloudflare_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the Cloudflare account, a hash of the account name. |
| <CopyableCode code="attributes" /> | `object` | Attributes object of a Cloudflare account. |
| <CopyableCode code="type" /> | `string` | The JSON:API type for this API. Should always be `cloudflare-accounts`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cloudflare_account" /> | `SELECT` | <CopyableCode code="account_id, dd_site" /> | Get a Cloudflare account. |
| <CopyableCode code="list_cloudflare_accounts" /> | `SELECT` | <CopyableCode code="dd_site" /> | List Cloudflare accounts. |
| <CopyableCode code="create_cloudflare_account" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a Cloudflare account. |
| <CopyableCode code="delete_cloudflare_account" /> | `DELETE` | <CopyableCode code="account_id, dd_site" /> | Delete a Cloudflare account. |
| <CopyableCode code="_get_cloudflare_account" /> | `EXEC` | <CopyableCode code="account_id, dd_site" /> | Get a Cloudflare account. |
| <CopyableCode code="_list_cloudflare_accounts" /> | `EXEC` | <CopyableCode code="dd_site" /> | List Cloudflare accounts. |
| <CopyableCode code="update_cloudflare_account" /> | `EXEC` | <CopyableCode code="account_id, data__data, dd_site" /> | Update a Cloudflare account. |
