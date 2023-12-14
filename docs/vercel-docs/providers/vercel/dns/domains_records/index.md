---
title: domains_records
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_records
  - dns
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.dns.domains_records</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `created` | `number` |
| `createdAt` | `number` |
| `creator` | `string` |
| `mxPriority` | `number` |
| `priority` | `number` |
| `slug` | `string` |
| `type` | `string` |
| `updated` | `number` |
| `updatedAt` | `number` |
| `value` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_records` | `SELECT` | `domain, teamId` | Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options. |
| `create_record` | `INSERT` | `domain, teamId, data__type` | Creates a DNS record for a domain. |
| `remove_record` | `DELETE` | `domain, recordId, teamId` | Removes an existing DNS record from a domain name. |
| `_get_records` | `EXEC` | `domain, teamId` | Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options. |
| `update_record` | `EXEC` | `recordId, teamId` | Updates an existing DNS record for a domain name. |
