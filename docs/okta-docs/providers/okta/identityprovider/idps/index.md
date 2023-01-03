---
title: idps
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `_links` | `object` |
| `type` | `string` |
| `created` | `string` |
| `issuerMode` | `string` |
| `policy` | `object` |
| `lastUpdated` | `string` |
| `protocol` | `object` |
| `status` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `idpId` | Fetches an IdP by `id`. |
| `list` | `SELECT` |  | Enumerates IdPs in your organization with pagination. A subset of IdPs can be returned that match a supported filter expression or query. |
| `insert` | `INSERT` |  | Adds a new IdP to your organization. |
| `delete` | `DELETE` | `idpId` | Removes an IdP from your organization. |
| `activate` | `EXEC` | `idpId` | Activates an inactive IdP. |
| `deactivate` | `EXEC` | `idpId` | Activates an inactive IdP. |
| `update` | `EXEC` | `idpId` | Updates the configuration for an IdP. |
