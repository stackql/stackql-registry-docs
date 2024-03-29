---
title: subdomain
hide_title: false
hide_table_of_contents: false
keywords:
  - subdomain
  - account
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subdomain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.account.subdomain</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` | Login URL corresponding to the subdomain. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format.<br /> |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `subdomain` | `string` | The new subdomain. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getSubdomain` | `SELECT` | `region` | Get the configured subdomain. |
| `createSubdomain` | `INSERT` | `data__subdomain, region` | Create a subdomain. Only the Account Owner can create a subdomain. |
| `deleteSubdomain` | `DELETE` | `region` | Delete the configured subdomain. |
| `updateSubdomain` | `EXEC` | `data__subdomain, region` | Update a subdomain. Only the Account Owner can update the subdomain. |
