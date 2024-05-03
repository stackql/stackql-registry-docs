---
title: sts_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - sts_accounts
  - gcp_integration
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
<tr><td><b>Name</b></td><td><code>sts_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.gcp_integration.sts_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Your service account's unique ID. |
| <CopyableCode code="attributes" /> | `object` | Attributes associated with your service account. |
| <CopyableCode code="meta" /> | `object` | Additional information related to your service account. |
| <CopyableCode code="type" /> | `string` | The type of account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_gcpsts_accounts" /> | `SELECT` | <CopyableCode code="dd_site" /> | List all GCP STS-enabled service accounts configured in your Datadog account. |
| <CopyableCode code="create_gcpsts_account" /> | `INSERT` | <CopyableCode code="dd_site" /> | Create a new entry within Datadog for your STS enabled service account. |
| <CopyableCode code="delete_gcpsts_account" /> | `DELETE` | <CopyableCode code="account_id, dd_site" /> | Delete an STS enabled GCP account from within Datadog. |
| <CopyableCode code="_list_gcpsts_accounts" /> | `EXEC` | <CopyableCode code="dd_site" /> | List all GCP STS-enabled service accounts configured in your Datadog account. |
| <CopyableCode code="update_gcpsts_account" /> | `EXEC` | <CopyableCode code="account_id, dd_site" /> | Update an STS enabled service account. |
