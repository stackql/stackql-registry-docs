---
title: exporters
hide_title: false
hide_table_of_contents: false
keywords:
  - exporters
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
<tr><td><b>Name</b></td><td><code>exporters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.exporters" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_exporter" /> | `DELETE` | <CopyableCode code="name" /> | Deletes the schema exporter. |
| <CopyableCode code="get_exporter_config_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Retrieves the config of the schema exporter. |
| <CopyableCode code="get_exporter_info_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Retrieves the information of the schema exporter. |
| <CopyableCode code="get_exporter_status_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Retrieves the status of the schema exporter. |
| <CopyableCode code="list_exporters" /> | `EXEC` |  | Retrieves a list of schema exporters that have been created. |
| <CopyableCode code="pause_exporter_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Pauses the state of the schema exporter. |
| <CopyableCode code="register_exporter" /> | `EXEC` |  | Creates a new schema exporter. All attributes in request body are optional except config. |
| <CopyableCode code="reset_exporter_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Reset the state of the schema exporter. |
| <CopyableCode code="resume_exporter_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Resume running of the schema exporter. |
| <CopyableCode code="update_exporter_config_by_name" /> | `EXEC` | <CopyableCode code="name" /> | Retrieves the config of the schema exporter. |
| <CopyableCode code="update_exporter_info" /> | `EXEC` | <CopyableCode code="name" /> | Updates the information or configurations of the schema exporter. All attributes in request body are optional. |
