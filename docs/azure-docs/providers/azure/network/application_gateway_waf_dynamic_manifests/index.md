---
title: application_gateway_waf_dynamic_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateway_waf_dynamic_manifests
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
<tr><td><b>Name</b></td><td><code>application_gateway_waf_dynamic_manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.application_gateway_waf_dynamic_manifests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `value` | `array` | The list of application gateway waf manifest. |
| `nextLink` | `string` | URL to get the next set of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ApplicationGatewayWafDynamicManifests_Get` | `SELECT` | `location, subscriptionId` |
