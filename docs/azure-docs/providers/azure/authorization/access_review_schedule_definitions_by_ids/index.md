---
title: access_review_schedule_definitions_by_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions_by_ids
  - authorization
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

Creates, updates, deletes, gets or lists a <code>access_review_schedule_definitions_by_ids</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_review_schedule_definitions_by_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_schedule_definitions_by_ids" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Create or Update access review schedule definition. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_review_schedule_definitions_by_ids</code> resource.

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
INSERT INTO azure.authorization.access_review_schedule_definitions_by_ids (
scheduleDefinitionId,
subscriptionId,
displayName,
descriptionForAdmins,
descriptionForReviewers,
settings,
reviewers,
backupReviewers,
instances
)
SELECT 
'{{ scheduleDefinitionId }}',
'{{ subscriptionId }}',
'{{ displayName }}',
'{{ descriptionForAdmins }}',
'{{ descriptionForReviewers }}',
'{{ settings }}',
'{{ reviewers }}',
'{{ backupReviewers }}',
'{{ instances }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: string
    - name: status
      value: string
    - name: descriptionForAdmins
      value: string
    - name: descriptionForReviewers
      value: string
    - name: createdBy
      value:
        - name: principalId
          value: string
        - name: principalType
          value: string
        - name: principalName
          value: string
        - name: userPrincipalName
          value: string
    - name: settings
      value:
        - name: mailNotificationsEnabled
          value: boolean
        - name: reminderNotificationsEnabled
          value: boolean
        - name: defaultDecisionEnabled
          value: boolean
        - name: justificationRequiredOnApproval
          value: boolean
        - name: defaultDecision
          value: string
        - name: autoApplyDecisionsEnabled
          value: boolean
        - name: recommendationsEnabled
          value: boolean
        - name: recommendationLookBackDuration
          value: string
        - name: instanceDurationInDays
          value: integer
        - name: recurrence
          value:
            - name: pattern
              value:
                - name: type
                  value: string
                - name: interval
                  value: integer
            - name: range
              value:
                - name: type
                  value: string
                - name: numberOfOccurrences
                  value: integer
                - name: startDate
                  value: string
                - name: endDate
                  value: string
    - name: scope
      value:
        - name: resourceId
          value: string
        - name: roleDefinitionId
          value: string
        - name: principalType
          value: string
        - name: assignmentState
          value: string
        - name: inactiveDuration
          value: string
        - name: expandNestedMemberships
          value: boolean
        - name: includeInheritedAccess
          value: boolean
        - name: includeAccessBelowResource
          value: boolean
        - name: excludeResourceId
          value: string
        - name: excludeRoleDefinitionId
          value: string
    - name: reviewers
      value:
        - - name: principalId
            value: string
          - name: principalType
            value: string
    - name: backupReviewers
      value:
        - - name: principalId
            value: string
          - name: principalType
            value: string
    - name: reviewersType
      value: string
    - name: instances
      value:
        - - name: id
            value: string
          - name: name
            value: string
          - name: type
            value: string
          - name: properties
            value:
              - name: status
                value: string
              - name: startDateTime
                value: string
              - name: endDateTime
                value: string
              - name: reviewers
                value:
                  - - name: principalId
                      value: string
                    - name: principalType
                      value: string
              - name: backupReviewers
                value:
                  - - name: principalId
                      value: string
                    - name: principalType
                      value: string
              - name: reviewersType
                value: string

```
</TabItem>
</Tabs>
