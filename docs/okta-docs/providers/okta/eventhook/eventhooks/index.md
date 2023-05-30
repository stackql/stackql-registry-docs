---
title: eventhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - eventhooks
  - eventhook
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
<tr><td><b>Name</b></td><td><code>eventhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.eventhook.eventhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `createdBy` | `string` |
| `lastUpdated` | `string` |
| `status` | `string` |
| `created` | `string` |
| `verificationStatus` | `string` |
| `channel` | `object` |
| `_links` | `object` |
| `events` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `eventHookId, subdomain` |
| `list` | `SELECT` | `subdomain` |
| `insert` | `INSERT` | `subdomain` |
| `delete` | `DELETE` | `eventHookId, subdomain` |
| `activate` | `EXEC` | `eventHookId, subdomain` |
| `deactivate` | `EXEC` | `eventHookId, subdomain` |
| `update` | `EXEC` | `eventHookId, subdomain` |
| `verify` | `EXEC` | `eventHookId, subdomain` |
