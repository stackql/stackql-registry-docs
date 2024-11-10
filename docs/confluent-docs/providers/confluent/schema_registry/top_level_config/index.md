---
title: top_level_config
hide_title: false
hide_table_of_contents: false
keywords:
  - top_level_config
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

Creates, updates, deletes, gets or lists a <code>top_level_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>top_level_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.top_level_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alias" /> | `string` | If alias is specified, then this subject is an alias for the subject named by the alias. That means that any reference to this subject will be replaced by the alias. |
| <CopyableCode code="compatibilityGroup" /> | `string` | Only schemas that belong to the same compatibility group will be checked for compatibility. |
| <CopyableCode code="compatibilityLevel" /> | `string` | Compatibility Level |
| <CopyableCode code="defaultMetadata" /> | `object` | Default value for the metadata to be used during schema registration. |
| <CopyableCode code="defaultRuleSet" /> | `object` | Default value for the ruleSet to be used during schema registration. |
| <CopyableCode code="normalize" /> | `boolean` | If true, then schemas are automatically normalized when registered or when passed during lookups. This means that clients do not have to pass the "normalize" query parameter to have normalization occur. |
| <CopyableCode code="overrideMetadata" /> | `object` | Override value for the metadata to be used during schema registration. |
| <CopyableCode code="overrideRuleSet" /> | `object` | Override value for the ruleSet to be used during schema registration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_top_level_config" /> | `SELECT` | <CopyableCode code="" /> | Retrieves the global compatibility level, compatibility group, normalization, default metadata, and rule set. |
| <CopyableCode code="delete_top_level_config" /> | `DELETE` | <CopyableCode code="" /> | Deletes the global compatibility level config and reverts to the default. |
| <CopyableCode code="update_top_level_config" /> | `EXEC` | <CopyableCode code="" /> | Updates the global compatibility level, compatibility group, schema normalization, default metadata, and rule set. On success, echoes the original request back to the client. |

## `SELECT` examples

Retrieves the global compatibility level, compatibility group, normalization, default metadata, and rule set.


```sql
SELECT
alias,
compatibilityGroup,
compatibilityLevel,
defaultMetadata,
defaultRuleSet,
normalize,
overrideMetadata,
overrideRuleSet
FROM confluent.schema_registry.top_level_config
;
```
## `DELETE` example

Deletes the specified <code>top_level_config</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.schema_registry.top_level_config
WHERE  = '{{  }}';
```
