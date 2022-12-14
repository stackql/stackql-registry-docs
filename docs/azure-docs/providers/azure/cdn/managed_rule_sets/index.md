---
title: managed_rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_rule_sets
  - cdn
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
<tr><td><b>Name</b></td><td><code>managed_rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.managed_rule_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `systemData` | `object` | Read only system data |
| `type` | `string` | Resource type. |
| `properties` | `object` | Properties for a managed rule set definition. |
| `sku` | `object` | Standard_Verizon = The SKU name for a Standard Verizon CDN profile.<br />Premium_Verizon = The SKU name for a Premium Verizon CDN profile.<br />Custom_Verizon = The SKU name for a Custom Verizon CDN profile.<br />Standard_Akamai = The SKU name for an Akamai CDN profile.<br />Standard_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using GB based billing model.<br />Standard_Microsoft = The SKU name for a Standard Microsoft CDN profile.<br />Standard_AzureFrontDoor =  The SKU name for an Azure Front Door Standard profile.<br />Premium_AzureFrontDoor = The SKU name for an Azure Front Door Premium profile.<br />Standard_955BandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using 95-5 peak bandwidth billing model.<br />Standard_AvgBandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using monthly average peak bandwidth billing model.<br />StandardPlus_ChinaCdn = The SKU name for a China CDN profile for live-streaming using GB based billing model.<br />StandardPlus_955BandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using 95-5 peak bandwidth billing model.<br />StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ManagedRuleSets_List` | `SELECT` | `subscriptionId` |
