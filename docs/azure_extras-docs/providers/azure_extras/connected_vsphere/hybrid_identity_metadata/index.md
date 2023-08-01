---
title: hybrid_identity_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_identity_metadata
  - connected_vsphere
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
<tr><td><b>Name</b></td><td><code>hybrid_identity_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.hybrid_identity_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Defines the resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HybridIdentityMetadata_Get` | `SELECT` | `api-version, metadataName, resourceGroupName, subscriptionId, virtualMachineName` | Implements HybridIdentityMetadata GET method. |
| `HybridIdentityMetadata_ListByVm` | `SELECT` | `api-version, resourceGroupName, subscriptionId, virtualMachineName` | Returns the list of HybridIdentityMetadata of the given vm. |
| `HybridIdentityMetadata_Create` | `INSERT` | `api-version, metadataName, resourceGroupName, subscriptionId, virtualMachineName, data__properties` | Create Or Update HybridIdentityMetadata. |
| `HybridIdentityMetadata_Delete` | `DELETE` | `api-version, metadataName, resourceGroupName, subscriptionId, virtualMachineName` | Implements HybridIdentityMetadata DELETE method. |
