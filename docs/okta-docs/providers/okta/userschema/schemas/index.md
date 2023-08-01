---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
  - userschema
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
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.userschema.schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `created` | `string` |
| `$schema` | `string` |
| `type` | `string` |
| `lastUpdated` | `string` |
| `properties` | `object` |
| `title` | `string` |
| `definitions` | `object` |
| `_links` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `schemaId, subdomain` | Fetches the schema for a Schema Id. |
| `partialUpdate` | `EXEC` | `schemaId, subdomain` | Partial updates on the User Profile properties of the user schema. |
