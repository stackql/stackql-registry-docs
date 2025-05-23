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
- name: your_resource_model_name
  props:
    - name: source
      value: string
    - name: description
      value: string
    - name: name
      value: string
    - name: rules
      value:
        - - name: description
            value: string
          - name: ruleId
            value: string
          - name: triggerType
            value: string
          - name: condition
            value: string
          - name: actions
            value:
              - - name: actionId
                  value: string
                - name: publishToPubSub
                  value:
                    - name: messages
                      value:
                        - string
                    - name: topicId
                      value: string
                - name: accessControl
                  value:
                    - name: policy
                      value:
                        - name: etag
                          value: string
                        - name: bindings
                          value:
                            - - name: members
                                value:
                                  - string
                              - name: role
                                value: string
                              - name: condition
                                value:
                                  - name: location
                                    value: string
                                  - name: expression
                                    value: string
                                  - name: title
                                    value: string
                                  - name: description
                                    value: string
                        - name: auditConfigs
                          value:
                            - - name: service
                                value: string
                              - name: auditLogConfigs
                                value:
                                  - - name: exemptedMembers
                                      value:
                                        - string
                                    - name: logType
                                      value: string
                        - name: version
                          value: integer
                    - name: operationType
                      value: string
                - name: deleteDocumentAction
                  value:
                    - name: enableHardDelete
                      value: boolean
                - name: removeFromFolderAction
                  value:
                    - name: condition
                      value: string
                    - name: folder
                      value: string
                - name: dataValidation
                  value:
                    - name: conditions
                      value: object
                - name: dataUpdate
                  value:
                    - name: entries
                      value: object
                - name: addToFolder
                  value:
                    - name: folders
                      value:
                        - string

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
