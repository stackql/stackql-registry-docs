---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - cost_management
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
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.settings" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | List all cost management settings in the requested scope. |
| <CopyableCode code="delete_by_scope" /> | `DELETE` | <CopyableCode code="scope, type" /> | Delete a setting within the given scope. |
| <CopyableCode code="create_or_update_by_scope" /> | `EXEC` | <CopyableCode code="scope, type, data__kind" /> | Create or update a setting within the given scope. |
| <CopyableCode code="get_by_scope" /> | `EXEC` | <CopyableCode code="scope, type" /> | Get the setting from the given scope by name. |
