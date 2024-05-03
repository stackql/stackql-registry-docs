---
title: product
hide_title: false
hide_table_of_contents: false
keywords:
  - product
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.product" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="etag" /> | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="properties" /> | `object` | Properties portion of the product resource. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="productName, registrationName, resourceGroup, subscriptionId" /> |
