---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| <CopyableCode code="display" /> | `object` | The display information for a configuration store operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation is a data action |
| <CopyableCode code="origin" /> | `string` | Origin of the operation |
| <CopyableCode code="properties" /> | `object` | Extra Operation properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` |  | Lists the operations available from this provider. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks whether the configuration store name is available for use. |
| <CopyableCode code="regional_check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks whether the configuration store name is available for use. |
