---
title: certs
hide_title: false
hide_table_of_contents: false
keywords:
  - certs
  - certs
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
<tr><td><b>Name</b></td><td><code>certs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.certs.certs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `autoRenew` | `boolean` |
| `cns` | `array` |
| `createdAt` | `number` |
| `expiresAt` | `number` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_cert_by_id` | `SELECT` | `id, teamId` | Get cert by id |
| `remove_cert` | `DELETE` | `id, teamId` | Remove cert |
| `issue_cert` | `EXEC` | `teamId` | Issue a new cert |
| `upload_cert` | `EXEC` | `teamId, data__ca, data__cert, data__key` | Upload a cert |
