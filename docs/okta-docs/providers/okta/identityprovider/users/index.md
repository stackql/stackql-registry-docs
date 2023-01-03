---
title: users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.identityprovider.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `_embedded` | `object` |
| `_links` | `object` |
| `created` | `string` |
| `externalId` | `string` |
| `lastUpdated` | `string` |
| `profile` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `idpId, userId` | Fetches a linked IdP user by ID |
| `list` | `SELECT` | `idpId` | Find all the users linked to an identity provider |
| `insert` | `INSERT` | `idpId, userId` | Links an Okta user to an existing Social Identity Provider. This does not support the SAML2 Identity Provider Type |
| `delete` | `DELETE` | `idpId, userId` | Removes the link between the Okta user and the IdP user. |
