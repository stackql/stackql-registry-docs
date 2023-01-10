---
title: wordpress_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - wordpress_instances
  - workloads
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>wordpress_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.workloads.wordpress_instances</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WordpressInstances_List` | `SELECT` | `phpWorkloadName, resourceGroupName, subscriptionId` | Lists WordPress instance resources under a phpWorkload resource. |
| `WordpressInstances_CreateOrUpdate` | `INSERT` | `phpWorkloadName, resourceGroupName, subscriptionId` | Create or updated WordPress instance resource. |
| `WordpressInstances_Delete` | `DELETE` | `phpWorkloadName, resourceGroupName, subscriptionId` | Delete WordPress instance resource. |
| `WordpressInstances_Get` | `EXEC` | `phpWorkloadName, resourceGroupName, subscriptionId` | Gets the WordPress instance resource. |
