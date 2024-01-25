---
title: subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription
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
<tr><td><b>Name</b></td><td><code>subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscription.subscription</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accept_ownership` | `EXEC` | `subscriptionId` | Accept subscription ownership. |
| `accept_ownership_status` | `EXEC` | `subscriptionId` | Accept subscription ownership status. |
| `cancel` | `EXEC` | `subscriptionId` | The operation to cancel a subscription |
| `enable` | `EXEC` | `subscriptionId` | The operation to enable a subscription |
| `rename` | `EXEC` | `subscriptionId` | The operation to rename a subscription |
