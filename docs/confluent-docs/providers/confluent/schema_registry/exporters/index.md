---
title: exporters
hide_title: false
hide_table_of_contents: false
keywords:
  - exporters
  - schema_registry
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>exporters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exporters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.exporters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the exporter |
| <CopyableCode code="config" /> | `object` | The map containing exporter’s configurations |
| <CopyableCode code="context" /> | `string` | Customized context of the exporter if contextType equals CUSTOM. |
| <CopyableCode code="contextType" /> | `string` | Context type of the exporter. One of CUSTOM, NONE or AUTO (default) |
| <CopyableCode code="subjectRenameFormat" /> | `string` | Format string for the subject name in the destination cluster, which may contain ${subject} as a placeholder for the originating subject name. For example, dc_${subject} for the subject orders will map to the destination subject name dc_orders. |
| <CopyableCode code="subjects" /> | `array` | Name of each exporter subject |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_exporter_info_by_name" /> | `SELECT` | <CopyableCode code="name" /> | Retrieves the information of the schema exporter. |
| <CopyableCode code="delete_exporter" /> | `DELETE` | <CopyableCode code="name" /> | Deletes the schema exporter. |
| <CopyableCode code="list_exporters" /> | `EXEC` | <CopyableCode code="" /> | Retrieves a list of schema exporters that have been created. |
| <CopyableCode code="pause_exporter_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Pauses the state of the schema exporter. |
| <CopyableCode code="register_exporter" /> | `EXEC` | <CopyableCode code="" /> | Creates a new schema exporter. All attributes in request body are optional except config. |
| <CopyableCode code="reset_exporter_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Reset the state of the schema exporter. |
| <CopyableCode code="resume_exporter_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Resume running of the schema exporter. |
| <CopyableCode code="update_exporter_info" /> | `EXEC` | <CopyableCode code="name" /> | Updates the information or configurations of the schema exporter. All attributes in request body are optional. |

## `SELECT` examples

Retrieves the information of the schema exporter.


```sql
SELECT
name,
config,
context,
contextType,
subjectRenameFormat,
subjects
FROM confluent.schema_registry.exporters
WHERE name = '{{ name }}';
```
## `DELETE` example

Deletes the specified <code>exporters</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.schema_registry.exporters
WHERE name = '{{ name }}';
```
