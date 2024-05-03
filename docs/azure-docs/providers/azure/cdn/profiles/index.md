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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `string` | Kind of the profile. Used by portal to differentiate traditional CDN profile and new AFD profile. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create a profile. |
| <CopyableCode code="sku" /> | `object` | Standard_Verizon = The SKU name for a Standard Verizon CDN profile.<br />Premium_Verizon = The SKU name for a Premium Verizon CDN profile.<br />Custom_Verizon = The SKU name for a Custom Verizon CDN profile.<br />Standard_Akamai = The SKU name for an Akamai CDN profile.<br />Standard_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using GB based billing model.<br />Standard_Microsoft = The SKU name for a Standard Microsoft CDN profile.<br />Standard_AzureFrontDoor =  The SKU name for an Azure Front Door Standard profile.<br />Premium_AzureFrontDoor = The SKU name for an Azure Front Door Premium profile.<br />Standard_955BandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using 95-5 peak bandwidth billing model.<br />Standard_AvgBandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using monthly average peak bandwidth billing model.<br />StandardPlus_ChinaCdn = The SKU name for a China CDN profile for live-streaming using GB based billing model.<br />StandardPlus_955BandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using 95-5 peak bandwidth billing model.<br />StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model.<br /> |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Gets an Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within an Azure subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId, data__sku" /> | Creates a new Azure Front Door Standard or Azure Front Door Premium or CDN profile with a profile name under the specified subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Deletes an existing  Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified parameters. Deleting a profile will result in the deletion of all of the sub-resources including endpoints, origins and custom domains. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within an Azure subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within a resource group. |
| <CopyableCode code="can_migrate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, data__classicResourceReference" /> | Checks if CDN profile can be migrated to Azure Frontdoor(Standard/Premium) profile. |
| <CopyableCode code="generate_sso_uri" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Generates a dynamic SSO URI used to sign in to the CDN supplemental portal. Supplemental portal is used to configure advanced feature capabilities that are not yet available in the Azure portal, such as core reports in a standard profile; rules engine, advanced HTTP reports, and real-time stats and alerts in a premium profile. The SSO URI changes approximately every 10 minutes. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, data__classicResourceReference, data__profileName, data__sku" /> | Migrate the CDN profile to Azure Frontdoor(Standard/Premium) profile. The change need to be committed after this. |
| <CopyableCode code="migration_commit" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Commit the migrated Azure Frontdoor(Standard/Premium) profile. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Updates an existing Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group. |
