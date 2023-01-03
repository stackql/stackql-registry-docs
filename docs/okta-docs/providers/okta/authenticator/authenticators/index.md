---
title: authenticators
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
<tr><td><b>Name</b></td><td><code>authenticators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.authenticator.authenticators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `settings` | `object` |
| `type` | `string` |
| `key` | `string` |
| `_links` | `object` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `authenticatorId` |
| `list` | `SELECT` |  |
| `activate` | `EXEC` | `authenticatorId` |
| `deactivate` | `EXEC` | `authenticatorId` |
