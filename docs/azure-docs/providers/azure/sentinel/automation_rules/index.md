---
title: automation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - automation_rules
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>automation_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>automation_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.automation_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_automation_rules', value: 'view', },
        { label: 'automation_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationRuleId" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="order" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="triggering_logic" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Automation rule properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationRuleId, resourceGroupName, subscriptionId, workspaceName" /> | Gets the automation rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all automation rules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationRuleId, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Creates or updates the automation rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationRuleId, resourceGroupName, subscriptionId, workspaceName" /> | Delete the automation rule. |

## `SELECT` examples

Gets all automation rules.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_automation_rules', value: 'view', },
        { label: 'automation_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
actions,
automationRuleId,
created_by,
created_time_utc,
display_name,
etag,
last_modified_by,
last_modified_time_utc,
order,
resourceGroupName,
subscriptionId,
triggering_logic,
workspaceName
FROM azure.sentinel.vw_automation_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.automation_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>automation_rules</code> resource.

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
INSERT INTO azure.sentinel.automation_rules (
automationRuleId,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
etag,
properties
)
SELECT 
'{{ automationRuleId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: displayName
          value: string
        - name: order
          value: integer
        - name: triggeringLogic
          value:
            - name: isEnabled
              value: boolean
            - name: expirationTimeUtc
              value: string
            - name: triggersOn
              value: []
            - name: triggersWhen
              value: []
            - name: conditions
              value:
                - - name: conditionType
                    value: []
        - name: actions
          value:
            - - name: order
                value: integer
              - name: actionType
                value: []
        - name: lastModifiedTimeUtc
          value: string
        - name: createdTimeUtc
          value: string
        - name: lastModifiedBy
          value:
            - name: email
              value: string
            - name: name
              value: string
            - name: objectId
              value: string
            - name: userPrincipalName
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>automation_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.automation_rules
WHERE automationRuleId = '{{ automationRuleId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
