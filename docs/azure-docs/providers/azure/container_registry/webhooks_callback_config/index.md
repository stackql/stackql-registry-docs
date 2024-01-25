---
title: webhooks_callback_config
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks_callback_config
  - container_registry
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
<tr><td><b>Name</b></td><td><code>webhooks_callback_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.webhooks_callback_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `customHeaders` | `object` | Custom headers that will be added to the webhook notifications. |
| `serviceUri` | `string` | The service URI for the webhook to post notifications. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `registryName, resourceGroupName, subscriptionId, webhookName` |
