---
title: idps
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `type` | `string` |
| `version` | `string` |
| `status` | `string` |
| `_links` | `object` |
| `channel` | `object` |
| `lastUpdated` | `string` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `inlineHookId` | Gets an inline hook by ID |
| `list` | `SELECT` |  | Success |
| `insert` | `INSERT` |  | Success |
| `delete` | `DELETE` | `inlineHookId` | Deletes the Inline Hook matching the provided id. Once deleted, the Inline Hook is unrecoverable. As a safety precaution, only Inline Hooks with a status of INACTIVE are eligible for deletion. |
| `activate` | `EXEC` | `inlineHookId` | Activates the Inline Hook matching the provided id |
| `deactivate` | `EXEC` | `inlineHookId` | Deactivates the Inline Hook matching the provided id |
| `execute` | `EXEC` | `inlineHookId` | Executes the Inline Hook matching the provided inlineHookId using the request body as the input. This will send the provided data through the Channel and return a response if it matches the correct data contract. This execution endpoint should only be used for testing purposes. |
| `update` | `EXEC` | `inlineHookId` | Updates an inline hook by ID |
