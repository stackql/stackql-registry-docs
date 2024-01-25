---
title: provider_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_registrations
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>provider_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.provider_hub.provider_registrations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `providerNamespace, subscriptionId` | Gets the provider registration details. |
| `list` | `SELECT` | `subscriptionId` | Gets the list of the provider registrations in the subscription. |
| `create_or_update` | `INSERT` | `providerNamespace, subscriptionId` | Creates or updates the provider registration. |
| `delete` | `DELETE` | `providerNamespace, subscriptionId` | Deletes a provider registration. |
| `_list` | `EXEC` | `subscriptionId` | Gets the list of the provider registrations in the subscription. |
| `generate_operations` | `EXEC` | `providerNamespace, subscriptionId` | Generates the operations api for the given provider. |
