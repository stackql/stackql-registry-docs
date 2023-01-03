---
title: org
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
<tr><td><b>Name</b></td><td><code>org</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.org</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `created` | `string` |
| `endUserSupportHelpURL` | `string` |
| `address2` | `string` |
| `lastUpdated` | `string` |
| `expiresAt` | `string` |
| `supportPhoneNumber` | `string` |
| `companyName` | `string` |
| `state` | `string` |
| `city` | `string` |
| `phoneNumber` | `string` |
| `postalCode` | `string` |
| `_links` | `object` |
| `website` | `string` |
| `country` | `string` |
| `address1` | `string` |
| `subdomain` | `string` |
| `status` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Get settings of your organization. |
| `partialUpdate` | `EXEC` |  | Partial update settings of your organization. |
| `update` | `EXEC` |  | Update settings of your organization. |
