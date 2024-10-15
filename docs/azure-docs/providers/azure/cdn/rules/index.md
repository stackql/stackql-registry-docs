---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - cdn
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

Creates, updates, deletes, gets or lists a <code>rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rules', value: 'view', },
        { label: 'rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="conditions" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="match_processing_behavior" /> | `text` | field from the `properties` object |
| <CopyableCode code="order" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_set_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties of the Rules to create. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, ruleName, ruleSetName, subscriptionId" /> | Gets an existing delivery rule within a rule set. |
| <CopyableCode code="list_by_rule_set" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, ruleSetName, subscriptionId" /> | Lists all of the existing delivery rules within a rule set. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="profileName, resourceGroupName, ruleName, ruleSetName, subscriptionId" /> | Creates a new delivery rule within the specified rule set. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="profileName, resourceGroupName, ruleName, ruleSetName, subscriptionId" /> | Deletes an existing delivery rule within a rule set. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="profileName, resourceGroupName, ruleName, ruleSetName, subscriptionId" /> | Updates an existing delivery rule within a rule set. |

## `SELECT` examples

Lists all of the existing delivery rules within a rule set.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rules', value: 'view', },
        { label: 'rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
actions,
conditions,
deployment_status,
match_processing_behavior,
order,
profileName,
provisioning_state,
resourceGroupName,
ruleName,
ruleSetName,
rule_set_name,
subscriptionId
FROM azure.cdn.vw_rules
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleSetName = '{{ ruleSetName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.rules
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleSetName = '{{ ruleSetName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rules</code> resource.

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
INSERT INTO azure.cdn.rules (
profileName,
resourceGroupName,
ruleName,
ruleSetName,
subscriptionId,
properties
)
SELECT 
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ ruleName }}',
'{{ ruleSetName }}',
'{{ subscriptionId }}',
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
        - name: ruleSetName
          value: string
        - name: order
          value: integer
        - name: conditions
          value:
            - - name: name
                value: string
        - name: actions
          value:
            - - name: name
                value: string
        - name: matchProcessingBehavior
          value: string
        - name: provisioningState
          value: string
        - name: deploymentStatus
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>rules</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.rules
SET 
properties = '{{ properties }}'
WHERE 
profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND ruleSetName = '{{ ruleSetName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.rules
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND ruleSetName = '{{ ruleSetName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
