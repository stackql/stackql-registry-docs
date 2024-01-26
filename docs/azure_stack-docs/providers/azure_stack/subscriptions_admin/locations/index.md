---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - subscriptions_admin
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Location identifier. |
| `name` | `string` | Location name. |
| `displayName` | `string` | Display name of the location. |
| `latitude` | `string` | Latitude of the location. |
| `longitude` | `string` | Longitude of the location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, subscriptionId` | Get the specified location. |
| `list` | `SELECT` | `subscriptionId` | Get a list of all AzureStack location. |
| `create_or_update` | `INSERT` | `location, subscriptionId` | Updates the specified location. |
| `_list` | `EXEC` | `subscriptionId` | Get a list of all AzureStack location. |
