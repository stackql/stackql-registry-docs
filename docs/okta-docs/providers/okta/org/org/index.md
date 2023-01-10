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
| `country` | `string` |
| `address2` | `string` |
| `endUserSupportHelpURL` | `string` |
| `address1` | `string` |
| `companyName` | `string` |
| `created` | `string` |
| `status` | `string` |
| `expiresAt` | `string` |
| `supportPhoneNumber` | `string` |
| `subdomain` | `string` |
| `state` | `string` |
| `_links` | `object` |
| `phoneNumber` | `string` |
| `postalCode` | `string` |
| `website` | `string` |
| `lastUpdated` | `string` |
| `city` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Get settings of your organization. |
| `partialUpdate` | `EXEC` |  | Partial update settings of your organization. |
| `update` | `EXEC` |  | Update settings of your organization. |
