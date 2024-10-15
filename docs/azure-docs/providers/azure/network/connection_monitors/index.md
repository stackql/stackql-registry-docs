---
title: connection_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_monitors
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

Creates, updates, deletes, gets or lists a <code>connection_monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.connection_monitors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_monitors', value: 'view', },
        { label: 'connection_monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the connection monitor. |
| <CopyableCode code="name" /> | `text` | Name of the connection monitor. |
| <CopyableCode code="auto_start" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionMonitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_monitor_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Connection monitor location. |
| <CopyableCode code="monitoring_interval_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkWatcherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Connection monitor tags. |
| <CopyableCode code="test_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Connection monitor type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the connection monitor. |
| <CopyableCode code="name" /> | `string` | Name of the connection monitor. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Connection monitor location. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a connection monitor. |
| <CopyableCode code="tags" /> | `object` | Connection monitor tags. |
| <CopyableCode code="type" /> | `string` | Connection monitor type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Gets a connection monitor by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Lists all connection monitors for the specified Network Watcher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a connection monitor. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Deletes the specified connection monitor. |
| <CopyableCode code="query" /> | `EXEC` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Query a snapshot of the most recent connection states. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Starts the specified connection monitor. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Stops the specified connection monitor. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId" /> | Update tags of the specified connection monitor. |

## `SELECT` examples

Lists all connection monitors for the specified Network Watcher.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_monitors', value: 'view', },
        { label: 'connection_monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
auto_start,
connectionMonitorName,
connection_monitor_type,
destination,
endpoints,
etag,
location,
monitoring_interval_in_seconds,
monitoring_status,
networkWatcherName,
notes,
outputs,
provisioning_state,
resourceGroupName,
source,
start_time,
subscriptionId,
tags,
test_configurations,
test_groups,
type
FROM azure.network.vw_connection_monitors
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
location,
properties,
tags,
type
FROM azure.network.connection_monitors
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection_monitors</code> resource.

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
INSERT INTO azure.network.connection_monitors (
connectionMonitorName,
networkWatcherName,
resourceGroupName,
subscriptionId,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ connectionMonitorName }}',
'{{ networkWatcherName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
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
        - name: source
          value:
            - name: resourceId
              value: string
            - name: port
              value: integer
        - name: destination
          value:
            - name: resourceId
              value: string
            - name: address
              value: string
            - name: port
              value: integer
        - name: autoStart
          value: boolean
        - name: monitoringIntervalInSeconds
          value: integer
        - name: endpoints
          value:
            - - name: name
                value: string
              - name: type
                value: string
              - name: resourceId
                value: string
              - name: address
                value: string
              - name: filter
                value:
                  - name: type
                    value: string
                  - name: items
                    value:
                      - - name: type
                          value: string
                        - name: address
                          value: string
              - name: scope
                value:
                  - name: include
                    value:
                      - - name: address
                          value: string
                  - name: exclude
                    value:
                      - - name: address
                          value: string
              - name: coverageLevel
                value: string
              - name: locationDetails
                value:
                  - name: region
                    value: string
              - name: subscriptionId
                value: string
        - name: testConfigurations
          value:
            - - name: name
                value: string
              - name: testFrequencySec
                value: integer
              - name: protocol
                value: string
              - name: preferredIPVersion
                value: string
              - name: httpConfiguration
                value:
                  - name: port
                    value: integer
                  - name: method
                    value: string
                  - name: path
                    value: string
                  - name: requestHeaders
                    value:
                      - - name: name
                          value: string
                        - name: value
                          value: string
                  - name: validStatusCodeRanges
                    value:
                      - string
                  - name: preferHTTPS
                    value: boolean
              - name: tcpConfiguration
                value:
                  - name: port
                    value: integer
                  - name: disableTraceRoute
                    value: boolean
                  - name: destinationPortBehavior
                    value: string
              - name: icmpConfiguration
                value:
                  - name: disableTraceRoute
                    value: boolean
              - name: successThreshold
                value:
                  - name: checksFailedPercent
                    value: integer
                  - name: roundTripTimeMs
                    value: number
        - name: testGroups
          value:
            - - name: name
                value: string
              - name: disable
                value: boolean
              - name: testConfigurations
                value:
                  - string
              - name: sources
                value:
                  - string
              - name: destinations
                value:
                  - string
        - name: outputs
          value:
            - - name: type
                value: string
              - name: workspaceSettings
                value:
                  - name: workspaceResourceId
                    value: string
        - name: notes
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connection_monitors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.connection_monitors
WHERE connectionMonitorName = '{{ connectionMonitorName }}'
AND networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
