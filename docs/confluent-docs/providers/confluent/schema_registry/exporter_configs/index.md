---
title: exporter_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - exporter_configs
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
<tr><td><b>Name</b></td><td><code>exporter_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.exporter_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="basic.auth.credentials.source" /> | `string` | Config SR Auth |
| <CopyableCode code="basic.auth.user.info" /> | `string` | Config SR User Info |
| <CopyableCode code="schema.registry.url" /> | `string` | Config SR URL |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_exporter_config_by_name" /> | `SELECT` | <CopyableCode code="name" /> |
| <CopyableCode code="update_exporter_config_by_name" /> | `EXEC` | <CopyableCode code="name" /> |
