---
title: subject_level_config
hide_title: false
hide_table_of_contents: false
keywords:
  - subject_level_config
  - schema_registry
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>subject_level_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subject_level_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.subject_level_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alias" /> | `string` | If alias is specified, then this subject is an alias for the subject
named by the alias. That means that any reference to this subject
will be replaced by the alias. |
| <CopyableCode code="compatibilityGroup" /> | `string` | Only schemas that belong to the same compatibility group will be
checked for compatibility. |
| <CopyableCode code="compatibilityLevel" /> | `string` | Compatibility Level |
| <CopyableCode code="defaultMetadata" /> | `object` | Default value for the metadata to be used during schema registration. |
| <CopyableCode code="defaultRuleSet" /> | `object` | Default value for the ruleSet to be used during schema registration. |
| <CopyableCode code="normalize" /> | `boolean` | If true, then schemas are automatically normalized when registered or
when passed during lookups. This means that clients do not have to
pass the "normalize" query parameter to have normalization occur. |
| <CopyableCode code="overrideMetadata" /> | `object` | Override value for the metadata to be used during schema registration. |
| <CopyableCode code="overrideRuleSet" /> | `object` | Override value for the ruleSet to be used during schema registration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_subject_level_config" /> | `SELECT` | <CopyableCode code="subject" /> | Retrieves compatibility level, compatibility group, normalization,
default metadata, and rule set for a subject. |
| <CopyableCode code="delete_subject_config" /> | `DELETE` | <CopyableCode code="subject" /> | Deletes the specified subject-level compatibility level config and reverts to the global default. |
| <CopyableCode code="update_subject_level_config" /> | `EXEC` | <CopyableCode code="subject" /> | Update compatibility level, compatibility group, normalization,
default metadata, and rule set for the specified subject. On success,
echoes the original request back to the client. |

## `SELECT` examples

Retrieves compatibility level, compatibility group, normalization,
default metadata, and rule set for a subject.


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
FROM confluent.schema_registry.subject_level_config
WHERE subject = '{{ subject }}';
```
## `DELETE` example

Deletes the specified <code>subject_level_config</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.schema_registry.subject_level_config
WHERE subject = '{{ subject }}';
```
