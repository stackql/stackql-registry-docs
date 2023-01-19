---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - adsensehost
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsensehost.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of this account. |
| `name` | `string` | Name of this account. |
| `status` | `string` | Approval status of this account. One of: PENDING, APPROVED, DISABLED. |
| `kind` | `string` | Kind of resource this is, in this case adsensehost#account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId` | Get information about the selected associated AdSense account. |
| `list` | `SELECT` | `filterAdClientId` | List hosted accounts associated with this AdSense account by ad client id. |
