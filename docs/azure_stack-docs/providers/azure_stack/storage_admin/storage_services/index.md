---
title: storage_services
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_services
  - storage_admin
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
<tr><td><b>Name</b></td><td><code>storage_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.storage_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | The properties for service name. |
| <CopyableCode code="type" /> | `string` | Resource Type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroup, serviceName, subscriptionId" /> | Returns the specified storage service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroup, serviceName, subscriptionId" /> | Create the specified storage resource. |
