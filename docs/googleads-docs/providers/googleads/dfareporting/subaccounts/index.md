---
title: subaccounts
hide_title: false
hide_table_of_contents: false
keywords:
  - subaccounts
  - dfareporting
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
<tr><td><b>Name</b></td><td><code>subaccounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.subaccounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this subaccount. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this subaccount. This is a required field. Must be less than 128 characters long and be unique among subaccounts of the same account. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#subaccount". |
| `accountId` | `string` | ID of the account that contains this subaccount. This is a read-only field that can be left blank. |
| `availablePermissionIds` | `array` | IDs of the available user role permissions for this subaccount. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one subaccount by ID. |
| `list` | `SELECT` | `profileId` | Gets a list of subaccounts, possibly filtered. This method supports paging. |
| `insert` | `INSERT` | `profileId` | Inserts a new subaccount. |
| `patch` | `EXEC` | `id, profileId` | Updates an existing subaccount. This method supports patch semantics. |
| `update` | `EXEC` | `profileId` | Updates an existing subaccount. |
