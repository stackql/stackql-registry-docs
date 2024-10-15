---
title: governance_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - governance_rules
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

Creates, updates, deletes, gets or lists a <code>governance_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>governance_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.governance_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_governance_rules', value: 'view', },
        { label: 'governance_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="condition_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="excluded_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="governance_email_notification" /> | `text` | field from the `properties` object |
| <CopyableCode code="include_member_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_disabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_grace_period" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="owner_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation_timeframe" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleId" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of an governance rule |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ruleId, scope" /> | Get a specific governance rule for the requested scope by ruleId |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of all relevant governance rules over a scope |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ruleId, scope" /> | Creates or updates a governance rule over a given scope |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ruleId, scope" /> | Delete a Governance rule over a given scope |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="ruleId, scope" /> | Execute a governance rule |
| <CopyableCode code="operation_results" /> | `EXEC` | <CopyableCode code="operationId, ruleId, scope" /> | Get governance rules long run operation result for the requested scope by ruleId and operationId |

## `SELECT` examples

Get a list of all relevant governance rules over a scope

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_governance_rules', value: 'view', },
        { label: 'governance_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
condition_sets,
display_name,
excluded_scopes,
governance_email_notification,
include_member_scopes,
is_disabled,
is_grace_period,
metadata,
owner_source,
remediation_timeframe,
ruleId,
rule_priority,
rule_type,
scope,
source_resource_type,
tenant_id,
type
FROM azure.security.vw_governance_rules
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.governance_rules
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>governance_rules</code> resource.

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
INSERT INTO azure.security.governance_rules (
ruleId,
scope,
properties
)
SELECT 
'{{ ruleId }}',
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
        - name: tenantId
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: remediationTimeframe
          value: string
        - name: isGracePeriod
          value: boolean
        - name: rulePriority
          value: integer
        - name: isDisabled
          value: boolean
        - name: ruleType
          value: string
        - name: sourceResourceType
          value: string
        - name: excludedScopes
          value:
            - string
        - name: conditionSets
          value:
            - []
        - name: includeMemberScopes
          value: boolean
        - name: ownerSource
          value:
            - name: type
              value: string
            - name: value
              value: string
        - name: governanceEmailNotification
          value:
            - name: disableManagerEmailNotification
              value: boolean
            - name: disableOwnerEmailNotification
              value: boolean
        - name: metadata
          value:
            - name: createdBy
              value: string
            - name: createdOn
              value: string
            - name: updatedBy
              value: string
            - name: updatedOn
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

Deletes the specified <code>governance_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.governance_rules
WHERE ruleId = '{{ ruleId }}'
AND scope = '{{ scope }}';
```
