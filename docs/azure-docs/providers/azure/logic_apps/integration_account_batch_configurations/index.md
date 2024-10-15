---
title: integration_account_batch_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_batch_configurations
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_account_batch_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_account_batch_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_account_batch_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_batch_configurations', value: 'view', },
        { label: 'integration_account_batch_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="batchConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="batch_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_criteria" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The batch configuration properties definition. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId" /> | Get a batch configuration for an integration account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | List the batch configurations for an integration account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a batch configuration for an integration account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId" /> | Delete a batch configuration for an integration account. |

## `SELECT` examples

List the batch configurations for an integration account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_batch_configurations', value: 'view', },
        { label: 'integration_account_batch_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
batchConfigurationName,
batch_group_name,
changed_time,
created_time,
integrationAccountName,
location,
metadata,
release_criteria,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.logic_apps.vw_integration_account_batch_configurations
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.logic_apps.integration_account_batch_configurations
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_account_batch_configurations</code> resource.

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
INSERT INTO azure.logic_apps.integration_account_batch_configurations (
batchConfigurationName,
integrationAccountName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
location,
tags
)
SELECT 
'{{ batchConfigurationName }}',
'{{ integrationAccountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: batchGroupName
          value: string
        - name: releaseCriteria
          value:
            - name: messageCount
              value: integer
            - name: batchSize
              value: integer
            - name: recurrence
              value:
                - name: frequency
                  value: []
                - name: interval
                  value: integer
                - name: startTime
                  value: string
                - name: endTime
                  value: string
                - name: timeZone
                  value: string
                - name: schedule
                  value:
                    - name: minutes
                      value:
                        - integer
                    - name: hours
                      value:
                        - integer
                    - name: weekDays
                      value:
                        - string
                    - name: monthDays
                      value:
                        - integer
                    - name: monthlyOccurrences
                      value:
                        - - name: day
                            value: []
                          - name: occurrence
                            value: integer
        - name: createdTime
          value: string
        - name: changedTime
          value: string
        - name: metadata
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>integration_account_batch_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_account_batch_configurations
WHERE batchConfigurationName = '{{ batchConfigurationName }}'
AND integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
