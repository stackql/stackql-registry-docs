---
title: metadata_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_schemas
  - api_center
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
<tr><td><b>Name</b></td><td><code>metadata_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.metadata_schemas" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="metadataSchemaName, resourceGroupName, serviceName, subscriptionId" /> | Returns details of the metadata schema. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Returns a collection of metadata schemas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="metadataSchemaName, resourceGroupName, serviceName, subscriptionId" /> | Creates new or updates existing metadata schema. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="metadataSchemaName, resourceGroupName, serviceName, subscriptionId" /> | Deletes specified metadata schema. |
