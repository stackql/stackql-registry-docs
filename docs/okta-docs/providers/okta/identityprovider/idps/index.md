---
title: idps
hide_title: false
hide_table_of_contents: false
keywords:
  - idps
  - identityprovider
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
<tr><td><b>Id</b></td><td><code>okta.identityprovider.idps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `type` | `string` |
| `_links` | `object` |
| `issuerMode` | `string` |
| `lastUpdated` | `string` |
| `protocol` | `object` |
| `status` | `string` |
| `policy` | `object` |
| `created` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `idpId, subdomain` | Fetches an IdP by `id`. |
| `list` | `SELECT` | `subdomain` | Enumerates IdPs in your organization with pagination. A subset of IdPs can be returned that match a supported filter expression or query. |
| `insert` | `INSERT` | `subdomain` | Adds a new IdP to your organization. |
| `delete` | `DELETE` | `idpId, subdomain` | Removes an IdP from your organization. |
| `activate` | `EXEC` | `idpId, subdomain` | Activates an inactive IdP. |
| `deactivate` | `EXEC` | `idpId, subdomain` | Activates an inactive IdP. |
| `update` | `EXEC` | `idpId, subdomain` | Updates the configuration for an IdP. |
