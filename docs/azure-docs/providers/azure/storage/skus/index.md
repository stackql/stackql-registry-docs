---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - storage
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
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The SKU name. Required for account creation; optional for update. Note that in older versions, SKU name was called accountType. |
| `kind` | `string` | Indicates the type of storage account. |
| `locations` | `array` | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). |
| `resourceType` | `string` | The type of the resource, usually it is 'storageAccounts'. |
| `restrictions` | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| `tier` | `string` | The SKU tier. This is based on the SKU name. |
| `capabilities` | `array` | The capability information in the specified SKU, including file encryption, network ACLs, change notification, etc. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Skus_List` | `SELECT` | `subscriptionId` |
