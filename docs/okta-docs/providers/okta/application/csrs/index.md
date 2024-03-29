---
title: csrs
hide_title: false
hide_table_of_contents: false
keywords:
  - csrs
  - application
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
<tr><td><b>Name</b></td><td><code>csrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.csrs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `kty` | `string` |
| `created` | `string` |
| `csr` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, csrId, subdomain` |  |
| `list` | `SELECT` | `appId, subdomain` | Enumerates Certificate Signing Requests for an application |
| `insert` | `INSERT` | `appId, subdomain` | Generates a new key pair and returns the Certificate Signing Request for it. |
| `delete` | `DELETE` | `appId, csrId, subdomain` |  |
