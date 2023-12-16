---
title: records
hide_title: false
hide_table_of_contents: false
keywords:
  - records
  - domains
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.domains.records</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `data` | `string` |  |
| `port` | `integer` | Service port (SRV only) |
| `priority` | `integer` | Record priority (MX and SRV only) |
| `protocol` | `string` | Service protocol (SRV only) |
| `service` | `string` | Service type (SRV only) |
| `ttl` | `integer` |  |
| `type` | `string` |  |
| `weight` | `integer` | Record weight (SRV only) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `record_get` | `SELECT` | `domain, type` | Retrieve DNS Records for the specified Domain, optionally with the specified Type and/or Name |
| `record_add` | `EXEC` | `domain` | Add the specified DNS Records to the specified Domain |
| `record_replace` | `EXEC` | `domain` | Replace all DNS Records for the specified Domain |
| `record_replace_type` | `EXEC` | `domain, type` | Replace all DNS Records for the specified Domain with the specified Type |
| `record_replace_type_name` | `EXEC` | `domain, name, type` | Replace all DNS Records for the specified Domain with the specified Type and Name |
