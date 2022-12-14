---
title: scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - scopes
  - authorizationserver
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
<tr><td><b>Name</b></td><td><code>scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authorizationserver.scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `displayName` | `string` |
| `metadataPublish` | `string` |
| `system` | `boolean` |
| `consent` | `string` |
| `default` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authServerId, scopeId` |
| `list` | `SELECT` | `authServerId` |
| `insert` | `INSERT` | `authServerId` |
| `delete` | `DELETE` | `authServerId, scopeId` |
| `update` | `EXEC` | `authServerId, scopeId` |
