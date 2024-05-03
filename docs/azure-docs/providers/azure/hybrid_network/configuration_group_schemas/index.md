---
title: configuration_group_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_group_schemas
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>configuration_group_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.configuration_group_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Configuration group schema properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about the specified configuration group schema. |
| <CopyableCode code="list_by_publisher" /> | `SELECT` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the configuration group schemas under a publisher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a configuration group schema. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Deletes a specified configuration group schema. |
| <CopyableCode code="_list_by_publisher" /> | `EXEC` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the configuration group schemas under a publisher. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId" /> | Updates a configuration group schema resource. |
