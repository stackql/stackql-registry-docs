---
title: domain_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_aliases
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.domain_aliases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `verified` | `boolean` | Indicates the verification state of a domain alias. (Read-only) |
| `creationTime` | `string` | The creation time of the domain alias. (Read-only). |
| `domainAliasName` | `string` | The domain alias name. |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | Kind of resource this is. |
| `parentDomainName` | `string` | The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customer, domainAliasName` | Retrieves a domain alias of the customer. |
| `list` | `SELECT` | `customer, parentDomainName` | Lists the domain aliases of the customer. |
| `insert` | `INSERT` | `customer` | Inserts a domain alias of the customer. |
| `delete` | `DELETE` | `customer, domainAliasName` | Deletes a domain Alias of the customer. |
| `_list` | `EXEC` | `customer, parentDomainName` | Lists the domain aliases of the customer. |
