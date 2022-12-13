---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Defines CDN web application firewall policy properties. |
| `sku` | `object` | Standard_Verizon = The SKU name for a Standard Verizon CDN profile.<br />Premium_Verizon = The SKU name for a Premium Verizon CDN profile.<br />Custom_Verizon = The SKU name for a Custom Verizon CDN profile.<br />Standard_Akamai = The SKU name for an Akamai CDN profile.<br />Standard_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using GB based billing model.<br />Standard_Microsoft = The SKU name for a Standard Microsoft CDN profile.<br />Standard_AzureFrontDoor =  The SKU name for an Azure Front Door Standard profile.<br />Premium_AzureFrontDoor = The SKU name for an Azure Front Door Premium profile.<br />Standard_955BandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using 95-5 peak bandwidth billing model.<br />Standard_AvgBandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using monthly average peak bandwidth billing model.<br />StandardPlus_ChinaCdn = The SKU name for a China CDN profile for live-streaming using GB based billing model.<br />StandardPlus_955BandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using 95-5 peak bandwidth billing model.<br />StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model.<br /> |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Gets a unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Policies_Get` | `SELECT` | `policyName, resourceGroupName, subscriptionId` | Retrieve protection policy with specified name within a resource group. |
| `Policies_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the protection policies within a resource group. |
| `Policies_CreateOrUpdate` | `INSERT` | `policyName, resourceGroupName, subscriptionId, data__sku` | Create or update policy with specified rule set name within a resource group. |
| `Policies_Delete` | `DELETE` | `policyName, resourceGroupName, subscriptionId` | Deletes Policy |
| `Policies_Update` | `EXEC` | `policyName, resourceGroupName, subscriptionId` | Update an existing CdnWebApplicationFirewallPolicy with the specified policy name under the specified subscription and resource group |
