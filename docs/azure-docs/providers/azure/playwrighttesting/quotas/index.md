---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - playwrighttesting
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.playwrighttesting.quotas</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, name, subscriptionId` | Get quota by name. |
| `list_by_subscription` | `SELECT` | `location, subscriptionId` | List quotas for a given subscription Id. |
| `_list_by_subscription` | `EXEC` | `location, subscriptionId` | List quotas for a given subscription Id. |
