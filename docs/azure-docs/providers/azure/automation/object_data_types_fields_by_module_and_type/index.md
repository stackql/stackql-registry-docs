---
title: object_data_types_fields_by_module_and_type
hide_title: false
hide_table_of_contents: false
keywords:
  - object_data_types_fields_by_module_and_type
  - automation
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
<tr><td><b>Name</b></td><td><code>object_data_types_fields_by_module_and_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.object_data_types_fields_by_module_and_type" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the field. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the field. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId, typeName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId, typeName" /> |
