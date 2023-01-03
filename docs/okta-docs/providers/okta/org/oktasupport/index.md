---
title: oktasupport
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
<tr><td><b>Name</b></td><td><code>oktasupport</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.oktasupport</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `_links` | `object` |
| `expiration` | `string` |
| `support` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Gets Okta Support Settings of your organization. |
| `extend` | `EXEC` |  | Extends the length of time that Okta Support can access your org by 24 hours. This means that 24 hours are added to the remaining access time. |
| `grant` | `EXEC` |  | Enables you to temporarily allow Okta Support to access your org as an administrator for eight hours. |
| `revoke` | `EXEC` |  | Revokes Okta Support access to your organization. |
