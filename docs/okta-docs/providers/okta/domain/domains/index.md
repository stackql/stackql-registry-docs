---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domain
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.domain.domains</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainId, subdomain` | Fetches a Domain by `id`. |
| `list` | `SELECT` | `subdomain` | List all verified custom Domains for the org. |
| `insert` | `INSERT` | `subdomain` | Creates your domain. |
| `delete` | `DELETE` | `domainId, subdomain` | Deletes a Domain by `id`. |
| `verify` | `EXEC` | `domainId, subdomain` | Verifies the Domain by `id`. |
