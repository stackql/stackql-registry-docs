---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.tables" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tables', value: 'view', },
        { label: 'tables', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="archive_retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_plan_modified_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restored_logs" /> | `text` | field from the `properties` object |
| <CopyableCode code="result_statistics" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_in_days_as_default" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="search_results" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_retention_in_days_as_default" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Table properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, tableName, workspaceName" /> | Gets a Log Analytics workspace table. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all the tables for the specified Log Analytics workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, tableName, workspaceName" /> | Update or Create a Log Analytics workspace table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, tableName, workspaceName" /> | Delete a Log Analytics workspace table. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, tableName, workspaceName" /> | Update a Log Analytics workspace table. |
| <CopyableCode code="cancel_search" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, tableName, workspaceName" /> | Cancel a log analytics workspace search results table query run. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, tableName, workspaceName" /> | Migrate a Log Analytics table from support of the Data Collector API and Custom Fields features to support of Data Collection Rule-based Custom Logs. |

## `SELECT` examples

Gets all the tables for the specified Log Analytics workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tables', value: 'view', },
        { label: 'tables', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
archive_retention_in_days,
last_plan_modified_date,
plan,
provisioning_state,
resourceGroupName,
restored_logs,
result_statistics,
retention_in_days,
retention_in_days_as_default,
schema,
search_results,
subscriptionId,
system_data,
tableName,
total_retention_in_days,
total_retention_in_days_as_default,
workspaceName
FROM azure.log_analytics.vw_tables
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.log_analytics.tables
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tables</code> resource.

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
INSERT INTO azure.log_analytics.tables (
resourceGroupName,
subscriptionId,
tableName,
workspaceName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tableName }}',
'{{ workspaceName }}',
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
        - name: retentionInDays
          value: integer
        - name: totalRetentionInDays
          value: integer
        - name: archiveRetentionInDays
          value: integer
        - name: searchResults
          value:
            - name: query
              value: string
            - name: description
              value: string
            - name: limit
              value: integer
            - name: startSearchTime
              value: string
            - name: endSearchTime
              value: string
            - name: sourceTable
              value: string
            - name: azureAsyncOperationId
              value: string
        - name: restoredLogs
          value:
            - name: startRestoreTime
              value: string
            - name: endRestoreTime
              value: string
            - name: sourceTable
              value: string
            - name: azureAsyncOperationId
              value: string
        - name: resultStatistics
          value:
            - name: progress
              value: number
            - name: ingestedRecords
              value: integer
            - name: scannedGb
              value: number
        - name: plan
          value: string
        - name: lastPlanModifiedDate
          value: string
        - name: schema
          value:
            - name: name
              value: string
            - name: displayName
              value: string
            - name: description
              value: string
            - name: columns
              value:
                - - name: name
                    value: string
                  - name: type
                    value: string
                  - name: dataTypeHint
                    value: string
                  - name: displayName
                    value: string
                  - name: description
                    value: string
                  - name: isDefaultDisplay
                    value: boolean
                  - name: isHidden
                    value: boolean
            - name: standardColumns
              value:
                - - name: name
                    value: string
                  - name: type
                    value: string
                  - name: dataTypeHint
                    value: string
                  - name: displayName
                    value: string
                  - name: description
                    value: string
                  - name: isDefaultDisplay
                    value: boolean
                  - name: isHidden
                    value: boolean
            - name: categories
              value:
                - string
            - name: labels
              value:
                - string
            - name: source
              value: string
            - name: tableType
              value: string
            - name: tableSubType
              value: string
            - name: solutions
              value:
                - string
        - name: provisioningState
          value: string
        - name: retentionInDaysAsDefault
          value: boolean
        - name: totalRetentionInDaysAsDefault
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

Updates a <code>tables</code> resource.

```sql
/*+ update */
UPDATE azure.log_analytics.tables
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>tables</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.tables
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tableName = '{{ tableName }}'
AND workspaceName = '{{ workspaceName }}';
```
