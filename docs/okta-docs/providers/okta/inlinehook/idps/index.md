---
title: idps
hide_title: false
hide_table_of_contents: false
keywords:
  - idps
  - inlinehook
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>idps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.inlinehook.idps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `version` | `string` |
| `channel` | `object` |
| `_links` | `object` |
| `status` | `string` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `inlineHookId, subdomain` | Gets an inline hook by ID |
| `list` | `SELECT` | `subdomain` | Success |
| `insert` | `INSERT` | `subdomain` | Success |
| `delete` | `DELETE` | `inlineHookId, subdomain` | Deletes the Inline Hook matching the provided id. Once deleted, the Inline Hook is unrecoverable. As a safety precaution, only Inline Hooks with a status of INACTIVE are eligible for deletion. |
| `activate` | `EXEC` | `inlineHookId, subdomain` | Activates the Inline Hook matching the provided id |
| `deactivate` | `EXEC` | `inlineHookId, subdomain` | Deactivates the Inline Hook matching the provided id |
| `execute` | `EXEC` | `inlineHookId, subdomain` | Executes the Inline Hook matching the provided inlineHookId using the request body as the input. This will send the provided data through the Channel and return a response if it matches the correct data contract. This execution endpoint should only be used for testing purposes. |
| `update` | `EXEC` | `inlineHookId, subdomain` | Updates an inline hook by ID |
