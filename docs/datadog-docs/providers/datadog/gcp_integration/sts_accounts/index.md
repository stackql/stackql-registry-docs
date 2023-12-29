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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sts_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.gcp_integration.sts_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Your service account's unique ID. |
| `attributes` | `object` | Attributes associated with your service account. |
| `meta` | `object` | Additional information related to your service account. |
| `type` | `string` | The type of account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_gcpsts_accounts` | `SELECT` | `dd_site` | List all GCP STS-enabled service accounts configured in your Datadog account. |
| `create_gcpsts_account` | `INSERT` | `dd_site` | Create a new entry within Datadog for your STS enabled service account. |
| `delete_gcpsts_account` | `DELETE` | `account_id, dd_site` | Delete an STS enabled GCP account from within Datadog. |
| `_list_gcpsts_accounts` | `EXEC` | `dd_site` | List all GCP STS-enabled service accounts configured in your Datadog account. |
| `update_gcpsts_account` | `EXEC` | `account_id, dd_site` | Update an STS enabled service account. |
