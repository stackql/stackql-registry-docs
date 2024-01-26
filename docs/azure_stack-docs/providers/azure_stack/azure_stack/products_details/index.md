---
title: products_details
hide_title: false
hide_table_of_contents: false
keywords:
  - products_details
  - azure_stack
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>products_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack.products_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `galleryPackageBlobSasUri` | `string` | The URI to the .azpkg file that provides information required for showing product in the gallery. |
| `productKind` | `string` | Specifies the kind of the product (virtualMachine or virtualMachineExtension). |
| `properties` | `object` | Product information. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `productName, registrationName, resourceGroup, subscriptionId` |
