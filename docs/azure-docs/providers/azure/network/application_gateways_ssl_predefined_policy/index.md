---
title: application_gateways_ssl_predefined_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways_ssl_predefined_policy
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
<tr><td><b>Name</b></td><td><code>application_gateways_ssl_predefined_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.application_gateways_ssl_predefined_policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the Ssl predefined policy. |
| `properties` | `object` | Properties of ApplicationGatewaySslPredefinedPolicy. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `predefinedPolicyName, subscriptionId` |
