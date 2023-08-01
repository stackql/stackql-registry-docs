---
title: default
hide_title: false
hide_table_of_contents: false
keywords:
  - default
  - groupschema
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
<tr><td><b>Name</b></td><td><code>default</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.groupschema.default</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `lastUpdated` | `string` |
| `_links` | `object` |
| `title` | `string` |
| `created` | `string` |
| `type` | `string` |
| `properties` | `object` |
| `definitions` | `object` |
| `$schema` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `subdomain` | Fetches the group schema |
| `update` | `EXEC` | `subdomain` | Updates, adds ore removes one or more custom Group Profile properties in the schema |
