---
title: scanning_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - scanning_groups
  - sensitive_data_scanner
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
<tr><td><b>Name</b></td><td><code>scanning_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.sensitive_data_scanner.scanning_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the configuration. |
| <CopyableCode code="attributes" /> | `object` | Attributes of the Sensitive Data configuration. |
| <CopyableCode code="relationships" /> | `object` | Relationships of the configuration. |
| <CopyableCode code="type" /> | `string` | Sensitive Data Scanner configuration type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_scanning_groups" /> | `SELECT` | <CopyableCode code="dd_site" /> | List all the Scanning groups in your organization. |
| <CopyableCode code="create_scanning_group" /> | `INSERT` | <CopyableCode code="dd_site" /> | Create a scanning group.<br />The request MAY include a configuration relationship.<br />A rules relationship can be omitted entirely, but if it is included it MUST be<br />null or an empty array (rules cannot be created at the same time).<br />The new group will be ordered last within the configuration. |
| <CopyableCode code="delete_scanning_group" /> | `DELETE` | <CopyableCode code="group_id, data__meta, dd_site" /> | Delete a given group. |
| <CopyableCode code="_list_scanning_groups" /> | `EXEC` | <CopyableCode code="dd_site" /> | List all the Scanning groups in your organization. |
| <CopyableCode code="reorder_scanning_groups" /> | `EXEC` | <CopyableCode code="data__data, data__meta, dd_site" /> | Reorder the list of groups. |
| <CopyableCode code="update_scanning_group" /> | `EXEC` | <CopyableCode code="group_id, data__data, data__meta, dd_site" /> | Update a group, including the order of the rules.<br />Rules within the group are reordered by including a rules relationship. If the rules<br />relationship is present, its data section MUST contain linkages for all of the rules<br />currently in the group, and MUST NOT contain any others. |
