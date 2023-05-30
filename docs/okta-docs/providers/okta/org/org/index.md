---
title: org
hide_title: false
hide_table_of_contents: false
keywords:
  - org
  - org
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
<tr><td><b>Name</b></td><td><code>org</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.org</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `status` | `string` |
| `country` | `string` |
| `city` | `string` |
| `address2` | `string` |
| `companyName` | `string` |
| `postalCode` | `string` |
| `created` | `string` |
| `phoneNumber` | `string` |
| `address1` | `string` |
| `state` | `string` |
| `endUserSupportHelpURL` | `string` |
| `supportPhoneNumber` | `string` |
| `subdomain` | `string` |
| `lastUpdated` | `string` |
| `website` | `string` |
| `expiresAt` | `string` |
| `_links` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `subdomain` | Get settings of your organization. |
| `partialUpdate` | `EXEC` | `subdomain` | Partial update settings of your organization. |
| `update` | `EXEC` | `subdomain` | Update settings of your organization. |
