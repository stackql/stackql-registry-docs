---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `kind` | `string` | Kind of the profile. Used by portal to differentiate traditional CDN profile and new AFD profile. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The JSON object that contains the properties required to create a profile. |
| `sku` | `object` | Standard_Verizon = The SKU name for a Standard Verizon CDN profile.<br />Premium_Verizon = The SKU name for a Premium Verizon CDN profile.<br />Custom_Verizon = The SKU name for a Custom Verizon CDN profile.<br />Standard_Akamai = The SKU name for an Akamai CDN profile.<br />Standard_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using GB based billing model.<br />Standard_Microsoft = The SKU name for a Standard Microsoft CDN profile.<br />Standard_AzureFrontDoor =  The SKU name for an Azure Front Door Standard profile.<br />Premium_AzureFrontDoor = The SKU name for an Azure Front Door Premium profile.<br />Standard_955BandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using 95-5 peak bandwidth billing model.<br />Standard_AvgBandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using monthly average peak bandwidth billing model.<br />StandardPlus_ChinaCdn = The SKU name for a China CDN profile for live-streaming using GB based billing model.<br />StandardPlus_955BandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using 95-5 peak bandwidth billing model.<br />StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model.<br /> |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Gets an Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group. |
| `list` | `SELECT` | `subscriptionId` | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within an Azure subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within a resource group. |
| `create` | `INSERT` | `profileName, resourceGroupName, subscriptionId, data__sku` | Creates a new Azure Front Door Standard or Azure Front Door Premium or CDN profile with a profile name under the specified subscription and resource group. |
| `delete` | `DELETE` | `profileName, resourceGroupName, subscriptionId` | Deletes an existing  Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified parameters. Deleting a profile will result in the deletion of all of the sub-resources including endpoints, origins and custom domains. |
| `_list` | `EXEC` | `subscriptionId` | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within an Azure subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within a resource group. |
| `can_migrate` | `EXEC` | `resourceGroupName, subscriptionId, data__classicResourceReference` | Checks if CDN profile can be migrated to Azure Frontdoor(Standard/Premium) profile. |
| `generate_sso_uri` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Generates a dynamic SSO URI used to sign in to the CDN supplemental portal. Supplemental portal is used to configure advanced feature capabilities that are not yet available in the Azure portal, such as core reports in a standard profile; rules engine, advanced HTTP reports, and real-time stats and alerts in a premium profile. The SSO URI changes approximately every 10 minutes. |
| `migrate` | `EXEC` | `resourceGroupName, subscriptionId, data__classicResourceReference, data__profileName, data__sku` | Migrate the CDN profile to Azure Frontdoor(Standard/Premium) profile. The change need to be committed after this. |
| `migration_commit` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Commit the migrated Azure Frontdoor(Standard/Premium) profile. |
| `update` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Updates an existing Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group. |
