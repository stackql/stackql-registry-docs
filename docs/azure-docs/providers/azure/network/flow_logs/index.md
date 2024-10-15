---
title: flow_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_logs
  - network
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

Creates, updates, deletes, gets or lists a <code>flow_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.flow_logs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_flow_logs', value: 'view', },
        { label: 'flow_logs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_filtering_criteria" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="flowLogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="flow_analytics_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="format" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="networkWatcherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="target_resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Parameters that define the configuration of flow log. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="flowLogName, networkWatcherName, resourceGroupName, subscriptionId" /> | Gets a flow log resource by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Lists all flow log resources for the specified Network Watcher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="flowLogName, networkWatcherName, resourceGroupName, subscriptionId" /> | Create or update a flow log for the specified network security group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="flowLogName, networkWatcherName, resourceGroupName, subscriptionId" /> | Deletes the specified flow log resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="flowLogName, networkWatcherName, resourceGroupName, subscriptionId" /> | Update tags of the specified flow log. |

## `SELECT` examples

Lists all flow log resources for the specified Network Watcher.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_flow_logs', value: 'view', },
        { label: 'flow_logs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
enabled,
enabled_filtering_criteria,
etag,
flowLogName,
flow_analytics_configuration,
format,
identity,
location,
networkWatcherName,
provisioning_state,
resourceGroupName,
retention_policy,
storage_id,
subscriptionId,
tags,
target_resource_guid,
target_resource_id,
type
FROM azure.network.vw_flow_logs
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
location,
properties,
tags,
type
FROM azure.network.flow_logs
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow_logs</code> resource.

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
INSERT INTO azure.network.flow_logs (
flowLogName,
networkWatcherName,
resourceGroupName,
subscriptionId,
properties,
identity,
id,
location,
tags
)
SELECT 
'{{ flowLogName }}',
'{{ networkWatcherName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ id }}',
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
        - name: targetResourceId
          value: string
        - name: targetResourceGuid
          value: string
        - name: storageId
          value: string
        - name: enabledFilteringCriteria
          value: string
        - name: enabled
          value: boolean
        - name: retentionPolicy
          value:
            - name: days
              value: integer
            - name: enabled
              value: boolean
        - name: format
          value:
            - name: type
              value: string
            - name: version
              value: integer
        - name: flowAnalyticsConfiguration
          value:
            - name: networkWatcherFlowAnalyticsConfiguration
              value:
                - name: enabled
                  value: boolean
                - name: workspaceId
                  value: string
                - name: workspaceRegion
                  value: string
                - name: workspaceResourceId
                  value: string
                - name: trafficAnalyticsInterval
                  value: integer
        - name: provisioningState
          value: []
    - name: etag
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
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

Deletes the specified <code>flow_logs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.flow_logs
WHERE flowLogName = '{{ flowLogName }}'
AND networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
