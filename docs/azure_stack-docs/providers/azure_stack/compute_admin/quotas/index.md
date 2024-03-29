---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - compute_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.compute_admin.quotas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties for a Compute Quota |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, quotaName, subscriptionId` | Get an existing Compute Quota. |
| `list` | `SELECT` | `location, subscriptionId` | Get a list of existing Compute quotas. |
| `create_or_update` | `INSERT` | `location, quotaName, subscriptionId` | Creates or Updates a Compute Quota with the provided quota parameters. |
| `delete` | `DELETE` | `location, quotaName, subscriptionId` | Delete an existing Compute quota. |
| `_list` | `EXEC` | `location, subscriptionId` | Get a list of existing Compute quotas. |
