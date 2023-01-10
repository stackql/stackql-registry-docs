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
| `created` | `string` |
| `properties` | `object` |
| `_links` | `object` |
| `$schema` | `string` |
| `lastUpdated` | `string` |
| `title` | `string` |
| `type` | `string` |
| `definitions` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Fetches the group schema |
| `update` | `EXEC` |  | Updates, adds ore removes one or more custom Group Profile properties in the schema |
