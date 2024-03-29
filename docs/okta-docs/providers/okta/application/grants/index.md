---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.grants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `_embedded` | `object` |
| `clientId` | `string` |
| `createdBy` | `object` |
| `issuer` | `string` |
| `lastUpdated` | `string` |
| `source` | `string` |
| `status` | `string` |
| `userId` | `string` |
| `_links` | `object` |
| `scopeId` | `string` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, grantId, subdomain` | Fetches a single scope consent grant for the application |
| `list` | `SELECT` | `appId, subdomain` | Lists all scope consent grants for the application |
| `insert` | `INSERT` | `appId, subdomain` | Grants consent for the application to request an OAuth 2.0 Okta scope |
| `delete` | `DELETE` | `appId, grantId, subdomain` | Revokes permission for the application to request the given scope |
