---
title: authenticators
hide_title: false
hide_table_of_contents: false
keywords:
  - authenticators
  - authenticator
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
<tr><td><b>Name</b></td><td><code>authenticators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authenticator.authenticators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `created` | `string` |
| `_links` | `object` |
| `key` | `string` |
| `status` | `string` |
| `type` | `string` |
| `lastUpdated` | `string` |
| `settings` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authenticatorId` |
| `list` | `SELECT` |  |
| `activate` | `EXEC` | `authenticatorId` |
| `deactivate` | `EXEC` | `authenticatorId` |
