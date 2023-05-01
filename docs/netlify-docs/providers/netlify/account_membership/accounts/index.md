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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.account_membership.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `billing_name` | `string` |
| `billing_period` | `string` |
| `billing_details` | `string` |
| `slug` | `string` |
| `billing_email` | `string` |
| `roles_allowed` | `array` |
| `payment_method_id` | `string` |
| `capabilities` | `object` |
| `updated_at` | `string` |
| `type_name` | `string` |
| `owner_ids` | `array` |
| `type_id` | `string` |
| `type` | `string` |
| `created_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getAccount` | `SELECT` | `account_id` |
| `listAccountsForUser` | `SELECT` |  |
| `createAccount` | `INSERT` | `data__name, data__type_id` |
| `cancelAccount` | `EXEC` | `account_id` |
| `updateAccount` | `EXEC` | `account_id` |
