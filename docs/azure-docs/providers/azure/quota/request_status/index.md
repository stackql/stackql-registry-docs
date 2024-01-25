---
title: request_status
hide_title: false
hide_table_of_contents: false
keywords:
  - request_status
  - quota
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>request_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.quota.request_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Quota request ID. |
| `name` | `string` | Quota request name. |
| `properties` | `object` | Quota request properties. |
| `type` | `string` | Resource type. "Microsoft.Quota/quotas". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, scope` | Get the quota request details and status by quota request ID for the resources of the resource provider at a specific location. The quota request ID **id** is returned in the response of the PUT operation. |
| `list` | `SELECT` | `scope` | For the specified scope, get the current quota requests for a one year period ending at the time is made. Use the **oData** filter to select quota requests. |
| `_list` | `EXEC` | `scope` | For the specified scope, get the current quota requests for a one year period ending at the time is made. Use the **oData** filter to select quota requests. |
