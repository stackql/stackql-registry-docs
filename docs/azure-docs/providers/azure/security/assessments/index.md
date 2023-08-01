---
title: assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments
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
<tr><td><b>Name</b></td><td><code>assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.assessments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Describes properties of an assessment. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Assessments_Get` | `SELECT` | `api-version, assessmentName, resourceId` | Get a security assessment on your scanned resource |
| `Assessments_List` | `SELECT` | `api-version, scope` | Get security assessments on all your scanned resources inside a scope |
| `Assessments_CreateOrUpdate` | `INSERT` | `api-version, assessmentName, resourceId` | Create a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result |
| `Assessments_Delete` | `DELETE` | `api-version, assessmentName, resourceId` | Delete a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result |
