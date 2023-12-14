---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - deployments
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.deployments.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `__created` | `number` |
| `__payload` | `object` |
| `__type` | `string` |
| `_created` | `number` |
| `_payload` | `object` |
| `_type` | `string` |
| `created` | `number` |
| `payload` | `object` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_deployment_events` | `SELECT` | `idOrUrl, teamId` |
