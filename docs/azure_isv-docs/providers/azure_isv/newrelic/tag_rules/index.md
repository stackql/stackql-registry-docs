---
title: tag_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_rules
  - newrelic
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

Creates, updates, deletes, gets or lists a <code>tag_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.newrelic.tag_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tag_rules', value: 'view', },
        { label: 'tag_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="log_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="metric_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The resource-specific properties for this resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subscriptionId" /> | Get a TagRule |
| <CopyableCode code="list_by_new_relic_monitor_resource" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | List TagRule resources by NewRelicMonitorResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subscriptionId, data__properties" /> | Create a TagRule |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subscriptionId" /> | Delete a TagRule |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subscriptionId" /> | Update a TagRule |

## `SELECT` examples

List TagRule resources by NewRelicMonitorResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tag_rules', value: 'view', },
        { label: 'tag_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
log_rules,
metric_rules,
monitorName,
provisioning_state,
resourceGroupName,
ruleSetName,
subscriptionId
FROM azure_isv.newrelic.vw_tag_rules
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.newrelic.tag_rules
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tag_rules</code> resource.

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
INSERT INTO azure_isv.newrelic.tag_rules (
monitorName,
resourceGroupName,
ruleSetName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ monitorName }}',
'{{ resourceGroupName }}',
'{{ ruleSetName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: provisioningState
          value: []
        - name: logRules
          value:
            - name: sendAadLogs
              value: []
            - name: sendSubscriptionLogs
              value: []
            - name: sendActivityLogs
              value: []
            - name: filteringTags
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
                  - name: action
                    value: []
        - name: metricRules
          value:
            - name: sendMetrics
              value: []
            - name: filteringTags
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
            - name: userEmail
              value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tag_rules</code> resource.

```sql
/*+ update */
UPDATE azure_isv.newrelic.tag_rules
SET 
properties = '{{ properties }}'
WHERE 
monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleSetName = '{{ ruleSetName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>tag_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.newrelic.tag_rules
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleSetName = '{{ ruleSetName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
