---
title: rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_sets
  - contentwarehouse
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>rule_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.rule_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the rule set. Managed internally. Format: projects/{project_number}/locations/{location}/ruleSet/{rule_set_id}. The name is ignored when creating a rule set. |
| <CopyableCode code="description" /> | `string` | Short description of the rule-set. |
| <CopyableCode code="rules" /> | `array` | List of rules given by the customer. |
| <CopyableCode code="source" /> | `string` | Source of the rules i.e., customer name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, ruleSetsId" /> | Gets a ruleset. Returns NOT_FOUND if the ruleset does not exist. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists rulesets. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a ruleset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, ruleSetsId" /> | Deletes a ruleset. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, ruleSetsId" /> | Updates a ruleset. Returns INVALID_ARGUMENT if the name of the ruleset is non-empty and does not equal the existing name. |

## `SELECT` examples

Lists rulesets.

```sql
SELECT
name,
description,
rules,
source
FROM google.contentwarehouse.rule_sets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rule_sets</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.contentwarehouse.rule_sets (
locationsId,
projectsId,
source,
description,
name,
rules
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ source }}',
'{{ description }}',
'{{ name }}',
'{{ rules }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
source: string
description: string
name: string
rules:
  - description: string
    ruleId: string
    triggerType: string
    condition: string
    actions:
      - actionId: string
        publishToPubSub:
          messages:
            - type: string
          topicId: string
        accessControl:
          policy:
            etag: string
            bindings:
              - members:
                  - type: string
                role: string
                condition:
                  location: string
                  expression: string
                  title: string
                  description: string
            auditConfigs:
              - service: string
                auditLogConfigs:
                  - exemptedMembers:
                      - type: string
                    logType: string
            version: integer
          operationType: string
        deleteDocumentAction:
          enableHardDelete: boolean
        removeFromFolderAction:
          condition: string
          folder: string
        dataValidation:
          conditions: object
        dataUpdate:
          entries: object
        addToFolder:
          folders:
            - type: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>rule_sets</code> resource.

```sql
/*+ update */
UPDATE google.contentwarehouse.rule_sets
SET 
ruleSet = '{{ ruleSet }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND ruleSetsId = '{{ ruleSetsId }}';
```

## `DELETE` example

Deletes the specified <code>rule_sets</code> resource.

```sql
/*+ delete */
DELETE FROM google.contentwarehouse.rule_sets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND ruleSetsId = '{{ ruleSetsId }}';
```
