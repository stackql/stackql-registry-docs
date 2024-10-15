---
title: prometheus_rule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - prometheus_rule_groups
  - alerts_management
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

Creates, updates, deletes, gets or lists a <code>prometheus_rule_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prometheus_rule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.prometheus_rule_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_prometheus_rule_groups', value: 'view', },
        { label: 'prometheus_rule_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="interval" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | An Azure Prometheus rule group. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleGroupName, subscriptionId" /> | Retrieve a Prometheus rule group definition. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve Prometheus rule group definitions in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve Prometheus all rule group definitions in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, ruleGroupName, subscriptionId, data__properties" /> | Create or update a Prometheus rule group definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, ruleGroupName, subscriptionId" /> | Delete a Prometheus rule group definition. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, ruleGroupName, subscriptionId" /> | Update an Prometheus rule group definition. |

## `SELECT` examples

Retrieve Prometheus all rule group definitions in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_prometheus_rule_groups', value: 'view', },
        { label: 'prometheus_rule_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
cluster_name,
enabled,
interval,
location,
resourceGroupName,
ruleGroupName,
rules,
scopes,
subscriptionId,
tags
FROM azure.alerts_management.vw_prometheus_rule_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.alerts_management.prometheus_rule_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>prometheus_rule_groups</code> resource.

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
INSERT INTO azure.alerts_management.prometheus_rule_groups (
resourceGroupName,
ruleGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ ruleGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: description
          value: string
        - name: enabled
          value: boolean
        - name: clusterName
          value: string
        - name: scopes
          value:
            - string
        - name: interval
          value: string
        - name: rules
          value:
            - - name: record
                value: string
              - name: alert
                value: string
              - name: enabled
                value: boolean
              - name: expression
                value: string
              - name: labels
                value: object
              - name: severity
                value: integer
              - name: for
                value: string
              - name: annotations
                value: object
              - name: actions
                value: []
              - name: resolveConfiguration
                value:
                  - name: autoResolved
                    value: boolean
                  - name: timeToResolve
                    value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>prometheus_rule_groups</code> resource.

```sql
/*+ update */
UPDATE azure.alerts_management.prometheus_rule_groups
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND ruleGroupName = '{{ ruleGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>prometheus_rule_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.alerts_management.prometheus_rule_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND ruleGroupName = '{{ ruleGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
