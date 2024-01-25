---
title: buildpack_binding_for_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - buildpack_binding_for_cluster
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>buildpack_binding_for_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.buildpack_binding_for_cluster</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` |
