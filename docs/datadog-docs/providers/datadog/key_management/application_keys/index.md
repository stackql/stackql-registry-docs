---
title: application_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - application_keys
  - key_management
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.key_management.application_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the application key. |
| <CopyableCode code="attributes" /> | `object` | Attributes of a full application key. |
| <CopyableCode code="relationships" /> | `object` | Resources related to the application key. |
| <CopyableCode code="type" /> | `string` | Application Keys resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_application_key" /> | `SELECT` | <CopyableCode code="app_key_id, dd_site" /> | Get an application key for your org. |
| <CopyableCode code="list_application_keys" /> | `SELECT` | <CopyableCode code="dd_site" /> | List all application keys available for your org |
| <CopyableCode code="delete_application_key" /> | `DELETE` | <CopyableCode code="app_key_id, dd_site" /> | Delete an application key |
| <CopyableCode code="_get_application_key" /> | `EXEC` | <CopyableCode code="app_key_id, dd_site" /> | Get an application key for your org. |
| <CopyableCode code="_list_application_keys" /> | `EXEC` | <CopyableCode code="dd_site" /> | List all application keys available for your org |
| <CopyableCode code="update_application_key" /> | `EXEC` | <CopyableCode code="app_key_id, data__data, dd_site" /> | Edit an application key |
