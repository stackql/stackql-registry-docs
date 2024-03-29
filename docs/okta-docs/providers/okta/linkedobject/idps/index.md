---
title: idps
hide_title: false
hide_table_of_contents: false
keywords:
  - idps
  - linkedobject
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
<tr><td><b>Name</b></td><td><code>idps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.linkedobject.idps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `_links` | `object` |
| `associated` | `object` |
| `primary` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `linkedObjectName, subdomain` |
| `list` | `SELECT` | `subdomain` |
| `insert` | `INSERT` | `subdomain` |
| `delete` | `DELETE` | `linkedObjectName, subdomain` |
