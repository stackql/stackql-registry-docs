---
title: default
hide_title: false
hide_table_of_contents: false
keywords:
  - default
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
<tr><td><b>Name</b></td><td><code>default</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.userschema.default</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `properties` | `object` |
| `_links` | `object` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `title` | `string` |
| `type` | `string` |
| `definitions` | `object` |
| `$schema` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `appInstanceId, subdomain` | Fetches the Schema for an App User |
| `insert` | `INSERT` | `appInstanceId, subdomain` | Partial updates on the User Profile properties of the Application User Schema. |
