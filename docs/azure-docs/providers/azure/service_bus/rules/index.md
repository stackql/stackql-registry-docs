---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - service_bus
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_bus.rules" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="action" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation_filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="filter_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="topicName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Description of Rule Resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, ruleName, subscriptionId, subscriptionName, topicName" /> | Retrieves the description for the specified rule. |
| <CopyableCode code="list_by_subscriptions" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName" /> | List all the rules within given topic-subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, resourceGroupName, ruleName, subscriptionId, subscriptionName, topicName" /> | Creates a new rule and updates an existing rule |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, resourceGroupName, ruleName, subscriptionId, subscriptionName, topicName" /> | Deletes an existing rule. |

## `SELECT` examples

List all the rules within given topic-subscription

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
id,
name,
action,
correlation_filter,
filter_type,
location,
namespaceName,
resourceGroupName,
ruleName,
sql_filter,
subscriptionId,
subscriptionName,
system_data,
topicName,
type
FROM azure.service_bus.vw_rules
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND subscriptionName = '{{ subscriptionName }}'
AND topicName = '{{ topicName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.service_bus.rules
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND subscriptionName = '{{ subscriptionName }}'
AND topicName = '{{ topicName }}';
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
INSERT INTO azure.service_bus.rules (
namespaceName,
resourceGroupName,
ruleName,
subscriptionId,
subscriptionName,
topicName,
properties
)
SELECT 
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ ruleName }}',
'{{ subscriptionId }}',
'{{ subscriptionName }}',
'{{ topicName }}',
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
        - name: action
          value:
            - name: sqlExpression
              value: string
            - name: compatibilityLevel
              value: integer
            - name: requiresPreprocessing
              value: boolean
        - name: filterType
          value: []
        - name: sqlFilter
          value:
            - name: sqlExpression
              value: string
            - name: compatibilityLevel
              value: integer
            - name: requiresPreprocessing
              value: boolean
        - name: correlationFilter
          value:
            - name: properties
              value: object
            - name: correlationId
              value: string
            - name: messageId
              value: string
            - name: to
              value: string
            - name: replyTo
              value: string
            - name: label
              value: string
            - name: sessionId
              value: string
            - name: replyToSessionId
              value: string
            - name: contentType
              value: string
            - name: requiresPreprocessing
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_bus.rules
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND subscriptionName = '{{ subscriptionName }}'
AND topicName = '{{ topicName }}';
```
