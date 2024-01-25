---
title: private_link_hub_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_hub_private_link_resources
  - synapse
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
<tr><td><b>Name</b></td><td><code>private_link_hub_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.private_link_hub_private_link_resources</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateLinkHubName, privateLinkResourceName, resourceGroupName, subscriptionId` | Get private link resource in private link hub |
| `list` | `SELECT` | `privateLinkHubName, resourceGroupName, subscriptionId` | Get all private link resources for a private link hub |
| `_list` | `EXEC` | `privateLinkHubName, resourceGroupName, subscriptionId` | Get all private link resources for a private link hub |
