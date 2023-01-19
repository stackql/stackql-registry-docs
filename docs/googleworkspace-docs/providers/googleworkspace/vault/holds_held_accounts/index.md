---
title: holds_held_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - holds_held_accounts
  - vault
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>holds_held_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.vault.holds_held_accounts</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `matters_holds_addHeldAccounts` | `EXEC` | `holdId, matterId` | Adds accounts to a hold. Returns a list of accounts that have been successfully added. Accounts can be added only to an existing account-based hold. |
| `matters_holds_removeHeldAccounts` | `EXEC` | `holdId, matterId` | Removes the specified accounts from a hold. Returns a list of statuses in the same order as the request. |
