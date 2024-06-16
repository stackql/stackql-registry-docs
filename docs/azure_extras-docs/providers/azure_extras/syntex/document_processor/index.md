---
title: document_processor
hide_title: false
hide_table_of_contents: false
keywords:
  - document_processor
  - syntex
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>document_processor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.syntex.document_processor" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Document processor properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="processorName, resourceGroupName, subscriptionId" /> | Returns a document processor for a given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns document processors in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns document processors in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="processorName, resourceGroupName, subscriptionId" /> | Creates a document processor resource for a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="processorName, resourceGroupName, subscriptionId" /> | Deletes document processor resource for a given name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="processorName, resourceGroupName, subscriptionId" /> | Updates a document processor resource for a given name. |
