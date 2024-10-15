---
title: alert_processing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_processing_rules
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

Creates, updates, deletes, gets or lists a <code>alert_processing_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_processing_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alert_processing_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_processing_rules', value: 'view', },
        { label: 'alert_processing_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="alertProcessingRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="conditions" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Alert processing rule properties defining scopes, conditions and scheduling logic for alert processing rule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_name" /> | `SELECT` | <CopyableCode code="alertProcessingRuleName, resourceGroupName, subscriptionId" /> | Get an alert processing rule by name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all alert processing rules in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all alert processing rules in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="alertProcessingRuleName, resourceGroupName, subscriptionId" /> | Create or update an alert processing rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="alertProcessingRuleName, resourceGroupName, subscriptionId" /> | Delete an alert processing rule. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="alertProcessingRuleName, resourceGroupName, subscriptionId" /> | Enable, disable, or update tags for an alert processing rule. |

## `SELECT` examples

List all alert processing rules in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_processing_rules', value: 'view', },
        { label: 'alert_processing_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
actions,
alertProcessingRuleName,
conditions,
enabled,
location,
resourceGroupName,
schedule,
scopes,
subscriptionId,
system_data,
tags
FROM azure.alerts_management.vw_alert_processing_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.alerts_management.alert_processing_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>alert_processing_rules</code> resource.

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
INSERT INTO azure.alerts_management.alert_processing_rules (
alertProcessingRuleName,
resourceGroupName,
subscriptionId,
location,
tags,
properties,
systemData
)
SELECT 
'{{ alertProcessingRuleName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: scopes
          value: []
        - name: conditions
          value: []
        - name: schedule
          value:
            - name: effectiveFrom
              value: string
            - name: effectiveUntil
              value: string
            - name: timeZone
              value: string
            - name: recurrences
              value:
                - - name: recurrenceType
                    value: string
                  - name: startTime
                    value: string
                  - name: endTime
                    value: string
        - name: actions
          value:
            - - name: actionType
                value: string
        - name: description
          value: string
        - name: enabled
          value: boolean
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>alert_processing_rules</code> resource.

```sql
/*+ update */
UPDATE azure.alerts_management.alert_processing_rules
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
alertProcessingRuleName = '{{ alertProcessingRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>alert_processing_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.alerts_management.alert_processing_rules
WHERE alertProcessingRuleName = '{{ alertProcessingRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
