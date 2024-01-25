---
title: alias
hide_title: false
hide_table_of_contents: false
keywords:
  - alias
  - subscription
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
<tr><td><b>Name</b></td><td><code>alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscription.alias</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID for the alias resource. |
| `name` | `string` | Alias ID. |
| `properties` | `object` | Put subscription creation result properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type, Microsoft.Subscription/aliases. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `aliasName` | Get Alias Subscription. |
| `list` | `SELECT` |  | List Alias Subscription. |
| `create` | `INSERT` | `aliasName` | Create Alias Subscription. |
| `delete` | `DELETE` | `aliasName` | Delete Alias. |
| `_list` | `EXEC` |  | List Alias Subscription. |
