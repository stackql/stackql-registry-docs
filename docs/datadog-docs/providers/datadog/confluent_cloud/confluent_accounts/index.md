---
title: confluent_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - confluent_accounts
  - confluent_cloud
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
<tr><td><b>Name</b></td><td><code>confluent_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.confluent_cloud.confluent_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A randomly generated ID associated with a Confluent account. |
| <CopyableCode code="attributes" /> | `object` | The attributes of a Confluent account. |
| <CopyableCode code="type" /> | `string` | The JSON:API type for this API. Should always be `confluent-cloud-accounts`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_confluent_account" /> | `SELECT` | <CopyableCode code="account_id, dd_site" /> | Get the Confluent account with the provided account ID. |
| <CopyableCode code="list_confluent_account" /> | `SELECT` | <CopyableCode code="dd_site" /> | List Confluent accounts. |
| <CopyableCode code="create_confluent_account" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a Confluent account. |
| <CopyableCode code="delete_confluent_account" /> | `DELETE` | <CopyableCode code="account_id, dd_site" /> | Delete a Confluent account with the provided account ID. |
| <CopyableCode code="_get_confluent_account" /> | `EXEC` | <CopyableCode code="account_id, dd_site" /> | Get the Confluent account with the provided account ID. |
| <CopyableCode code="_list_confluent_account" /> | `EXEC` | <CopyableCode code="dd_site" /> | List Confluent accounts. |
| <CopyableCode code="update_confluent_account" /> | `EXEC` | <CopyableCode code="account_id, data__data, dd_site" /> | Update the Confluent account with the provided account ID. |
