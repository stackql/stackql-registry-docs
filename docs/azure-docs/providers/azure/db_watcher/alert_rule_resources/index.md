---
title: alert_rule_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rule_resources
  - db_watcher
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

Creates, updates, deletes, gets or lists a <code>alert_rule_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_rule_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.db_watcher.alert_rule_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_rule_resources', value: 'view', },
        { label: 'alert_rule_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alertRuleResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_rule_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_rule_template_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_rule_template_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_with_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="watcherName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The generic properties of the alert rule proxy resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertRuleResourceName, resourceGroupName, subscriptionId, watcherName" /> | Get a AlertRuleResource |
| <CopyableCode code="list_by_parent" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | List AlertRuleResource resources by Watcher |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="alertRuleResourceName, resourceGroupName, subscriptionId, watcherName" /> | Create a AlertRuleResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="alertRuleResourceName, resourceGroupName, subscriptionId, watcherName" /> | Delete a AlertRuleResource |

## `SELECT` examples

List AlertRuleResource resources by Watcher

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_rule_resources', value: 'view', },
        { label: 'alert_rule_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
alertRuleResourceName,
alert_rule_resource_id,
alert_rule_template_id,
alert_rule_template_version,
created_with_properties,
creation_time,
provisioning_state,
resourceGroupName,
subscriptionId,
watcherName
FROM azure.db_watcher.vw_alert_rule_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.db_watcher.alert_rule_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>alert_rule_resources</code> resource.

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
INSERT INTO azure.db_watcher.alert_rule_resources (
alertRuleResourceName,
resourceGroupName,
subscriptionId,
watcherName,
properties
)
SELECT 
'{{ alertRuleResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ watcherName }}',
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
        - name: alertRuleResourceId
          value: string
        - name: createdWithProperties
          value: []
        - name: creationTime
          value: string
        - name: provisioningState
          value: []
        - name: alertRuleTemplateId
          value: string
        - name: alertRuleTemplateVersion
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>alert_rule_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.db_watcher.alert_rule_resources
WHERE alertRuleResourceName = '{{ alertRuleResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
