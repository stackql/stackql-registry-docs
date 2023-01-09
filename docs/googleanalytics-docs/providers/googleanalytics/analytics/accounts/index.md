---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Account ID. |
| `name` | `string` | Account name. |
| `childLink` | `object` | Child link for an account entry. Points to the list of web properties for this account. |
| `updated` | `string` | Time the account was last modified. |
| `created` | `string` | Time the account was created. |
| `selfLink` | `string` | Link for this account. |
| `starred` | `boolean` | Indicates whether this account is starred or not. |
| `permissions` | `object` | Permissions the user has for this account. |
| `kind` | `string` | Resource type for Analytics account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `management_accounts_list` | `SELECT` |  |
