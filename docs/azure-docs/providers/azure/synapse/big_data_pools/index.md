---
title: big_data_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - big_data_pools
  - synapse
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

Creates, updates, deletes, gets or lists a <code>big_data_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>big_data_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.big_data_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_big_data_pools', value: 'view', },
        { label: 'big_data_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_pause" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_scale" /> | `text` | field from the `properties` object |
| <CopyableCode code="bigDataPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cache_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_libraries" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_spark_log_folder" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_executor_allocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_autotune_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_compute_isolation_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_succeeded_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="library_requirements" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_size_family" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_level_packages_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="spark_config_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="spark_events_folder" /> | `text` | field from the `properties` object |
| <CopyableCode code="spark_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a Big Data pool powered by Apache Spark |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bigDataPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Get a Big Data pool. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List Big Data pools in a workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bigDataPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Create a new Big Data pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bigDataPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Delete a Big Data pool from the workspace. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="bigDataPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Patch a Big Data pool. |

## `SELECT` examples

List Big Data pools in a workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_big_data_pools', value: 'view', },
        { label: 'big_data_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_pause,
auto_scale,
bigDataPoolName,
cache_size,
creation_date,
custom_libraries,
default_spark_log_folder,
dynamic_executor_allocation,
is_autotune_enabled,
is_compute_isolation_enabled,
last_succeeded_timestamp,
library_requirements,
location,
node_count,
node_size,
node_size_family,
provisioning_state,
resourceGroupName,
session_level_packages_enabled,
spark_config_properties,
spark_events_folder,
spark_version,
subscriptionId,
tags,
workspaceName
FROM azure.synapse.vw_big_data_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.synapse.big_data_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>big_data_pools</code> resource.

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
INSERT INTO azure.synapse.big_data_pools (
bigDataPoolName,
resourceGroupName,
subscriptionId,
workspaceName,
tags,
location,
properties
)
SELECT 
'{{ bigDataPoolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
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
        - name: provisioningState
          value: string
        - name: autoScale
          value:
            - name: minNodeCount
              value: integer
            - name: enabled
              value: boolean
            - name: maxNodeCount
              value: integer
        - name: creationDate
          value: string
        - name: autoPause
          value:
            - name: delayInMinutes
              value: integer
            - name: enabled
              value: boolean
        - name: isComputeIsolationEnabled
          value: boolean
        - name: isAutotuneEnabled
          value: boolean
        - name: sessionLevelPackagesEnabled
          value: boolean
        - name: cacheSize
          value: integer
        - name: dynamicExecutorAllocation
          value:
            - name: enabled
              value: boolean
            - name: minExecutors
              value: integer
            - name: maxExecutors
              value: integer
        - name: sparkEventsFolder
          value: string
        - name: nodeCount
          value: integer
        - name: libraryRequirements
          value:
            - name: time
              value: string
            - name: content
              value: string
            - name: filename
              value: string
        - name: customLibraries
          value:
            - - name: name
                value: string
              - name: path
                value: string
              - name: containerName
                value: string
              - name: uploadedTimestamp
                value: string
              - name: type
                value: string
              - name: provisioningStatus
                value: string
              - name: creatorId
                value: string
        - name: sparkConfigProperties
          value:
            - name: time
              value: string
            - name: content
              value: string
            - name: filename
              value: string
            - name: configurationType
              value: string
        - name: sparkVersion
          value: string
        - name: defaultSparkLogFolder
          value: string
        - name: nodeSize
          value: string
        - name: nodeSizeFamily
          value: string
        - name: lastSucceededTimestamp
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>big_data_pools</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.big_data_pools
SET 
tags = '{{ tags }}'
WHERE 
bigDataPoolName = '{{ bigDataPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>big_data_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.big_data_pools
WHERE bigDataPoolName = '{{ bigDataPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
