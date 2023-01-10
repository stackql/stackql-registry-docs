---
title: hcx_enterprise_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - hcx_enterprise_sites
  - vmware
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>hcx_enterprise_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware.hcx_enterprise_sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | The properties of an HCX Enterprise Site |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `HcxEnterpriseSites_Get` | `SELECT` | `hcxEnterpriseSiteName, privateCloudName, resourceGroupName, subscriptionId` |
| `HcxEnterpriseSites_List` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |
| `HcxEnterpriseSites_CreateOrUpdate` | `INSERT` | `hcxEnterpriseSiteName, privateCloudName, resourceGroupName, subscriptionId` |
| `HcxEnterpriseSites_Delete` | `DELETE` | `hcxEnterpriseSiteName, privateCloudName, resourceGroupName, subscriptionId` |
