---
title: data_exports
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exports
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

Creates, updates, deletes, gets or lists a <code>data_exports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.data_exports" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_exports', value: 'view', },
        { label: 'data_exports', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataExportName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_export_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Data Export properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataExportName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a data export instance. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists the data export instances within a workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataExportName, resourceGroupName, subscriptionId, workspaceName" /> | Create or update a data export. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataExportName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the specified data export in a given workspace.. |

## `SELECT` examples

Lists the data export instances within a workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_exports', value: 'view', },
        { label: 'data_exports', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_date,
dataExportName,
data_export_id,
destination,
enable,
last_modified_date,
resourceGroupName,
subscriptionId,
table_names,
workspaceName
FROM azure.log_analytics.vw_data_exports
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.log_analytics.data_exports
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_exports</code> resource.

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
INSERT INTO azure.log_analytics.data_exports (
dataExportName,
resourceGroupName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ dataExportName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: dataExportId
          value: string
        - name: tableNames
          value:
            - string
        - name: destination
          value:
            - name: resourceId
              value: string
            - name: type
              value: string
            - name: metaData
              value:
                - name: eventHubName
                  value: string
        - name: enable
          value: boolean
        - name: createdDate
          value: string
        - name: lastModifiedDate
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_exports</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.data_exports
WHERE dataExportName = '{{ dataExportName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
