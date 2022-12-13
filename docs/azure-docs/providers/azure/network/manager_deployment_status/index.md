---
title: manager_deployment_status
hide_title: false
hide_table_of_contents: false
keywords:
  - manager_deployment_status
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
<tr><td><b>Name</b></td><td><code>manager_deployment_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.manager_deployment_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `skipToken` | `string` | When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data. |
| `value` | `array` | Gets a page of Network Manager Deployment Status |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `NetworkManagerDeploymentStatus_List` | `SELECT` |  |
