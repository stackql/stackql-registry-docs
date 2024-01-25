---
title: appliances_upgrade_graph
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances_upgrade_graph
  - resource_connector
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
<tr><td><b>Name</b></td><td><code>appliances_upgrade_graph</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_connector.appliances_upgrade_graph</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The appliance resource path |
| `name` | `string` | The release train name. |
| `properties` | `object` | The Upgrade Graph Properties for appliance. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId, upgradeGraph` |
