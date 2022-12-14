---
title: available_endpoint_services
hide_title: false
hide_table_of_contents: false
keywords:
  - available_endpoint_services
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
<tr><td><b>Name</b></td><td><code>available_endpoint_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.available_endpoint_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the endpoint service. |
| `type` | `string` | Type of the endpoint service. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AvailableEndpointServices_List` | `SELECT` | `location, subscriptionId` |
