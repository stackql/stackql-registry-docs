---
title: application_gateway_waf_dynamic_manifests_default
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateway_waf_dynamic_manifests_default
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
<tr><td><b>Name</b></td><td><code>application_gateway_waf_dynamic_manifests_default</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.application_gateway_waf_dynamic_manifests_default</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `properties` | `object` | Properties of ApplicationGatewayWafDynamicManifest. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ApplicationGatewayWafDynamicManifestsDefault_Get` | `SELECT` | `location, subscriptionId` |
