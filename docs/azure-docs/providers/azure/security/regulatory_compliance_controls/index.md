---
title: regulatory_compliance_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - regulatory_compliance_controls
  - security
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
<tr><td><b>Name</b></td><td><code>regulatory_compliance_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.regulatory_compliance_controls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Regulatory compliance control data |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegulatoryComplianceControls_Get` | `SELECT` | `api-version, regulatoryComplianceControlName, regulatoryComplianceStandardName, subscriptionId` | Selected regulatory compliance control details and state |
| `RegulatoryComplianceControls_List` | `SELECT` | `api-version, regulatoryComplianceStandardName, subscriptionId` | All supported regulatory compliance controls details and state for selected standard |
