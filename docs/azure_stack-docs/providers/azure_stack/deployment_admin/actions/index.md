---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - deployment_admin
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.deployment_admin.actions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `product_bootstrap_action` | `EXEC` | `productId, subscriptionId` | Invokes bootstrap action on the product deployment |
| `product_deploy_action` | `EXEC` | `productId, subscriptionId` | Invokes deploy action on the product |
| `product_execute_runner_action` | `EXEC` | `productId, subscriptionId` | Invokes execute runner action on the product deployment |
| `product_remove_action` | `EXEC` | `productId, subscriptionId` | Invokes remove action on the product deployment |
| `product_rotate_secrets_action` | `EXEC` | `productId, subscriptionId` | Invokes rotate secrets action on the product deployment |
