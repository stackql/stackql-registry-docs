---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `isPrimary` | `boolean` | Indicates if the domain is a primary domain (Read-only). |
| `kind` | `string` | Kind of resource this is. |
| `verified` | `boolean` | Indicates the verification state of a domain. (Read-only). |
| `creationTime` | `string` | Creation time of the domain. Expressed in [Unix time](https://en.wikipedia.org/wiki/Epoch_time) format. (Read-only). |
| `domainAliases` | `array` | A list of domain alias objects. (Read-only) |
| `domainName` | `string` | The domain name of the customer. |
| `etag` | `string` | ETag of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customer, domainName` | Retrieves a domain of the customer. |
| `list` | `SELECT` | `customer` | Lists the domains of the customer. |
| `insert` | `INSERT` | `customer` | Inserts a domain of the customer. |
| `delete` | `DELETE` | `customer, domainName` | Deletes a domain of the customer. |
| `_list` | `EXEC` | `customer` | Lists the domains of the customer. |
