---
title: sub_account_tag_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_account_tag_rules
  - logz
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

Creates, updates, deletes, gets or lists a <code>sub_account_tag_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sub_account_tag_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.logz.sub_account_tag_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sub_account_tag_rules', value: 'view', },
        { label: 'sub_account_tag_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The id of the rule set. |
| <CopyableCode code="name" /> | `text` | Name of the rule set. |
| <CopyableCode code="log_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the rule set. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the rule set. |
| <CopyableCode code="name" /> | `string` | Name of the rule set. |
| <CopyableCode code="properties" /> | `object` | Definition of the properties for a TagRules resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the rule set. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subAccountName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subAccountName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subAccountName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sub_account_tag_rules', value: 'view', },
        { label: 'sub_account_tag_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
log_rules,
monitorName,
provisioning_state,
resourceGroupName,
ruleSetName,
subAccountName,
subscriptionId,
system_data,
type
FROM azure_isv.logz.vw_sub_account_tag_rules
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subAccountName = '{{ subAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure_isv.logz.sub_account_tag_rules
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subAccountName = '{{ subAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sub_account_tag_rules</code> resource.

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
INSERT INTO azure_isv.logz.sub_account_tag_rules (
monitorName,
resourceGroupName,
ruleSetName,
subAccountName,
subscriptionId,
properties
)
SELECT 
'{{ monitorName }}',
'{{ resourceGroupName }}',
'{{ ruleSetName }}',
'{{ subAccountName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: logRules
          value:
            - name: sendAadLogs
              value: boolean
            - name: sendSubscriptionLogs
              value: boolean
            - name: sendActivityLogs
              value: boolean
            - name: filteringTags
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
                  - name: action
                    value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sub_account_tag_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.logz.sub_account_tag_rules
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleSetName = '{{ ruleSetName }}'
AND subAccountName = '{{ subAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
