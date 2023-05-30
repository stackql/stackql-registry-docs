---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - application
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `lastUpdated` | `string` |
| `profile` | `object` |
| `licensing` | `object` |
| `status` | `string` |
| `signOnMode` | `string` |
| `accessibility` | `object` |
| `credentials` | `object` |
| `settings` | `object` |
| `_links` | `object` |
| `visibility` | `object` |
| `created` | `string` |
| `_embedded` | `object` |
| `label` | `string` |
| `features` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, subdomain` | Fetches an application from your Okta organization by `id`. |
| `list` | `SELECT` | `subdomain` | Enumerates apps added to your organization with pagination. A subset of apps can be returned that match a supported filter expression or query. |
| `insert` | `INSERT` | `subdomain` | Adds a new application to your Okta organization. |
| `delete` | `DELETE` | `appId, subdomain` | Removes an inactive application. |
| `activate` | `EXEC` | `appId, subdomain` | Activates an inactive application. |
| `deactivate` | `EXEC` | `appId, subdomain` | Deactivates an active application. |
| `deleteall` | `EXEC` | `appId, subdomain` | Revokes all tokens for the specified application |
| `update` | `EXEC` | `appId, subdomain` | Updates an application in your organization. |
