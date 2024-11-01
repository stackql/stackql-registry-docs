---
title: modes
hide_title: false
hide_table_of_contents: false
keywords:
  - modes
  - schema_registry
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>modes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.modes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_mode" /> | `SELECT` | <CopyableCode code="subject" /> | Retrieves the subject mode. |
| <CopyableCode code="get_top_level_mode" /> | `SELECT` |  | Retrieves global mode. |
| <CopyableCode code="delete_subject_mode" /> | `DELETE` | <CopyableCode code="subject" /> | Deletes the specified subject-level mode and reverts to the global default. |
| <CopyableCode code="update_mode" /> | `EXEC` | <CopyableCode code="subject" /> | Update mode for the specified subject. On success, echoes the original request back to the client. |
| <CopyableCode code="update_top_level_mode" /> | `EXEC` |  | Update global mode. On success, echoes the original request back to the client. |
