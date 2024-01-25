---
title: private_link_services_auto_approved_private_link_services_by_resource_group
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_auto_approved_private_link_services_by_resource_group
  - network
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
<tr><td><b>Name</b></td><td><code>private_link_services_auto_approved_private_link_services_by_resource_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.private_link_services_auto_approved_private_link_services_by_resource_group</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` |
