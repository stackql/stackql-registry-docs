---
title: governance_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - governance_assignments
  - security
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

Creates, updates, deletes, gets or lists a <code>governance_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>governance_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.governance_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_governance_assignments', value: 'view', },
        { label: 'governance_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="additional_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignmentKey" /> | `text` | field from the `properties` object |
| <CopyableCode code="governance_email_notification" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_grace_period" /> | `text` | field from the `properties` object |
| <CopyableCode code="owner" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_due_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_eta" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of an governance assignment |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assessmentName, assignmentKey, scope" /> | Get a specific governanceAssignment for the requested scope by AssignmentKey |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="assessmentName, scope" /> | Get governance assignments on all of your resources inside a scope |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="assessmentName, assignmentKey, scope" /> | Creates or updates a governance assignment on the given subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assessmentName, assignmentKey, scope" /> | Delete a GovernanceAssignment over a given scope |

## `SELECT` examples

Get governance assignments on all of your resources inside a scope

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_governance_assignments', value: 'view', },
        { label: 'governance_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_data,
assessmentName,
assignmentKey,
governance_email_notification,
is_grace_period,
owner,
remediation_due_date,
remediation_eta,
scope,
type
FROM azure.security.vw_governance_assignments
WHERE assessmentName = '{{ assessmentName }}'
AND scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.governance_assignments
WHERE assessmentName = '{{ assessmentName }}'
AND scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>governance_assignments</code> resource.

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
INSERT INTO azure.security.governance_assignments (
assessmentName,
assignmentKey,
scope,
properties
)
SELECT 
'{{ assessmentName }}',
'{{ assignmentKey }}',
'{{ scope }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: owner
          value: string
        - name: remediationDueDate
          value: string
        - name: remediationEta
          value:
            - name: eta
              value: string
            - name: justification
              value: string
        - name: isGracePeriod
          value: boolean
        - name: governanceEmailNotification
          value:
            - name: disableManagerEmailNotification
              value: boolean
            - name: disableOwnerEmailNotification
              value: boolean
        - name: additionalData
          value:
            - name: ticketNumber
              value: integer
            - name: ticketLink
              value: string
            - name: ticketStatus
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>governance_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.governance_assignments
WHERE assessmentName = '{{ assessmentName }}'
AND assignmentKey = '{{ assignmentKey }}'
AND scope = '{{ scope }}';
```
