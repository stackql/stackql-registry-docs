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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adc_catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_catalog.adc_catalogs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the data catalog. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | The Get Azure Data Catalog Service operation retrieves a json representation of the data catalog. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | The Create Azure Data Catalog service operation creates a new data catalog service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | The Delete Azure Data Catalog Service operation deletes an existing data catalog. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | The Update Azure Data Catalog Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body. |
