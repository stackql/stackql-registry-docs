---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - memcache
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

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.memcache.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` Note: Memcached instances are managed and addressed at the regional level so `location_id` here refers to a Google Cloud region; however, users may choose which zones Memcached nodes should be provisioned in within an instance. Refer to zones field for more details. |
| <CopyableCode code="authorizedNetwork" /> | `string` | The full name of the Google Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. If left unspecified, the `default` network will be used. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the instance was created. |
| <CopyableCode code="discoveryEndpoint" /> | `string` | Output only. Endpoint for the Discovery API. |
| <CopyableCode code="displayName" /> | `string` | User provided name for the instance, which is only used for display purposes. Cannot be more than 80 characters. |
| <CopyableCode code="instanceMessages" /> | `array` | List of messages that describe the current state of the Memcached instance. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| <CopyableCode code="maintenancePolicy" /> | `object` | Maintenance policy per instance. |
| <CopyableCode code="maintenanceSchedule" /> | `object` | Upcoming maintenance schedule. |
| <CopyableCode code="memcacheFullVersion" /> | `string` | Output only. The full version of memcached server running on this instance. System automatically determines the full memcached version for an instance based on the input MemcacheVersion. The full version format will be "memcached-1.5.16". |
| <CopyableCode code="memcacheNodes" /> | `array` | Output only. List of Memcached nodes. Refer to Node message for more details. |
| <CopyableCode code="memcacheVersion" /> | `string` | The major version of Memcached software. If not provided, latest supported version will be used. Currently the latest supported major version is `MEMCACHE_1_5`. The minor version will be automatically determined by our system based on the latest supported minor version. |
| <CopyableCode code="nodeConfig" /> | `object` | Configuration for a Memcached Node. |
| <CopyableCode code="nodeCount" /> | `integer` | Required. Number of nodes in the Memcached instance. |
| <CopyableCode code="parameters" /> | `object` |  |
| <CopyableCode code="reservedIpRangeId" /> | `array` | Optional. Contains the id of allocated IP address ranges associated with the private service access connection for example, "test-default" associated with IP range 10.0.0.0/29. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Optional. Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Optional. Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The state of this Memcached instance. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the instance was updated. |
| <CopyableCode code="zones" /> | `array` | Zones in which Memcached nodes should be provisioned. Memcached nodes will be equally distributed across these zones. If not provided, the service will by default create nodes in all zones in the region for the instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Gets details of a single Instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Instances in a given location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Instance in a given location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Deletes a single Instance. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Updates an existing Instance in a given project and location. |
| <CopyableCode code="apply_parameters" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | `ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance. |
| <CopyableCode code="reschedule_maintenance" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Reschedules upcoming maintenance event. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Upgrades the Memcache instance to a newer memcached engine version specified in the request. |

## `SELECT` examples

Lists Instances in a given location.

```sql
SELECT
name,
authorizedNetwork,
createTime,
discoveryEndpoint,
displayName,
instanceMessages,
labels,
maintenancePolicy,
maintenanceSchedule,
memcacheFullVersion,
memcacheNodes,
memcacheVersion,
nodeConfig,
nodeCount,
parameters,
reservedIpRangeId,
satisfiesPzi,
satisfiesPzs,
state,
updateTime,
zones
FROM google.memcache.instances
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

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
INSERT INTO google.memcache.instances (
locationsId,
projectsId,
name,
displayName,
labels,
authorizedNetwork,
zones,
nodeCount,
nodeConfig,
memcacheVersion,
parameters,
instanceMessages,
maintenancePolicy,
reservedIpRangeId
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ labels }}',
'{{ authorizedNetwork }}',
'{{ zones }}',
'{{ nodeCount }}',
'{{ nodeConfig }}',
'{{ memcacheVersion }}',
'{{ parameters }}',
'{{ instanceMessages }}',
'{{ maintenancePolicy }}',
'{{ reservedIpRangeId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: labels
      value: object
    - name: authorizedNetwork
      value: string
    - name: zones
      value:
        - string
    - name: nodeCount
      value: integer
    - name: nodeConfig
      value:
        - name: cpuCount
          value: integer
        - name: memorySizeMb
          value: integer
    - name: memcacheVersion
      value: string
    - name: parameters
      value:
        - name: id
          value: string
        - name: params
          value: object
    - name: memcacheNodes
      value:
        - - name: nodeId
            value: string
          - name: zone
            value: string
          - name: state
            value: string
          - name: host
            value: string
          - name: port
            value: integer
          - name: memcacheVersion
            value: string
          - name: memcacheFullVersion
            value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: state
      value: string
    - name: memcacheFullVersion
      value: string
    - name: instanceMessages
      value:
        - - name: code
            value: string
          - name: message
            value: string
    - name: discoveryEndpoint
      value: string
    - name: maintenancePolicy
      value:
        - name: createTime
          value: string
        - name: updateTime
          value: string
        - name: description
          value: string
        - name: weeklyMaintenanceWindow
          value:
            - - name: day
                value: string
              - name: startTime
                value:
                  - name: hours
                    value: integer
                  - name: minutes
                    value: integer
                  - name: seconds
                    value: integer
                  - name: nanos
                    value: integer
              - name: duration
                value: string
    - name: maintenanceSchedule
      value:
        - name: startTime
          value: string
        - name: endTime
          value: string
        - name: scheduleDeadlineTime
          value: string
    - name: reservedIpRangeId
      value:
        - string
    - name: satisfiesPzs
      value: boolean
    - name: satisfiesPzi
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instances</code> resource.

```sql
/*+ update */
UPDATE google.memcache.instances
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
authorizedNetwork = '{{ authorizedNetwork }}',
zones = '{{ zones }}',
nodeCount = '{{ nodeCount }}',
nodeConfig = '{{ nodeConfig }}',
memcacheVersion = '{{ memcacheVersion }}',
parameters = '{{ parameters }}',
instanceMessages = '{{ instanceMessages }}',
maintenancePolicy = '{{ maintenancePolicy }}',
reservedIpRangeId = '{{ reservedIpRangeId }}'
WHERE 
instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.memcache.instances
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
