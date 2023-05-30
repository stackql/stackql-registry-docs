---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - group
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
<tr><td><b>Id</b></td><td><code>okta.group.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `visibility` | `object` |
| `settings` | `object` |
| `label` | `string` |
| `_embedded` | `object` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `features` | `array` |
| `accessibility` | `object` |
| `signOnMode` | `string` |
| `_links` | `object` |
| `profile` | `object` |
| `licensing` | `object` |
| `credentials` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `groupId, subdomain` |
