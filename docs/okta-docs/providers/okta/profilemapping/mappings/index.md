---
title: mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - mappings
  - profilemapping
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
<tr><td><b>Name</b></td><td><code>mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.profilemapping.mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `_links` | `object` |
| `properties` | `object` |
| `source` | `object` |
| `target` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mappingId, subdomain` | Fetches a single Profile Mapping referenced by its ID. |
| `list` | `SELECT` | `subdomain` | Enumerates Profile Mappings in your organization with pagination. |
| `insert` | `INSERT` | `mappingId, subdomain` | Updates an existing Profile Mapping by adding, updating, or removing one or many Property Mappings. |
