---
title: top_level_config
hide_title: false
hide_table_of_contents: false
keywords:
  - top_level_config
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
<tr><td><b>Name</b></td><td><code>top_level_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.top_level_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alias" /> | `string` | If alias is specified, then this subject is an alias for the subject<br />named by the alias. That means that any reference to this subject<br />will be replaced by the alias. |
| <CopyableCode code="compatibilityGroup" /> | `string` | Only schemas that belong to the same compatibility group will be<br />checked for compatibility. |
| <CopyableCode code="compatibilityLevel" /> | `string` | Compatibility Level |
| <CopyableCode code="defaultMetadata" /> | `object` | Default value for the metadata to be used during schema registration. |
| <CopyableCode code="defaultRuleSet" /> | `object` | Default value for the ruleSet to be used during schema registration. |
| <CopyableCode code="normalize" /> | `boolean` | If true, then schemas are automatically normalized when registered or<br />when passed during lookups. This means that clients do not have to<br />pass the "normalize" query parameter to have normalization occur. |
| <CopyableCode code="overrideMetadata" /> | `object` | Override value for the metadata to be used during schema registration. |
| <CopyableCode code="overrideRuleSet" /> | `object` | Override value for the ruleSet to be used during schema registration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_top_level_config" /> | `SELECT` |  | Retrieves the global compatibility level, compatibility group,<br />normalization, default metadata, and rule set. |
| <CopyableCode code="delete_top_level_config" /> | `DELETE` |  | Deletes the global compatibility level config and reverts to the default. |
| <CopyableCode code="update_top_level_config" /> | `EXEC` |  | Updates the global compatibility level, compatibility group,<br />schema normalization, default metadata, and rule set. On success, echoes the<br />original request back to the client. |
