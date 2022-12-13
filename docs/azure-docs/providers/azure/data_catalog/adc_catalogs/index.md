---
title: adc_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - adc_catalogs
  - data_catalog
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
<tr><td><b>Name</b></td><td><code>adc_catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_catalog.adc_catalogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `properties` | `object` | Properties of the data catalog. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `etag` | `string` | Resource etag |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ADCCatalogs_Get` | `SELECT` | `catalogName, resourceGroupName, subscriptionId` | The Get Azure Data Catalog Service operation retrieves a json representation of the data catalog. |
| `ADCCatalogs_CreateOrUpdate` | `INSERT` | `catalogName, resourceGroupName, subscriptionId` | The Create Azure Data Catalog service operation creates a new data catalog service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged. |
| `ADCCatalogs_Delete` | `DELETE` | `catalogName, resourceGroupName, subscriptionId` | The Delete Azure Data Catalog Service operation deletes an existing data catalog. |
| `ADCCatalogs_ListtByResourceGroup` | `EXEC` | `resourceGroupName, subscriptionId` | The List catalogs in Resource Group operation lists all the Azure Data Catalogs available under the given resource group. |
| `ADCCatalogs_Update` | `EXEC` | `catalogName, resourceGroupName, subscriptionId` | The Update Azure Data Catalog Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body. |
