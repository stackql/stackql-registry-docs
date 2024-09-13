---
title: instances_secondary
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_secondary
  - alloydb
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

Creates, updates, deletes, gets or lists a <code>instances_secondary</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_secondary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.instances_secondary" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="createsecondary" /> | `INSERT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Creates a new SECONDARY Instance in a given project and location. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances_secondary</code> resource.

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
INSERT INTO google.alloydb.instances_secondary (
clustersId,
locationsId,
projectsId,
name,
displayName,
uid,
createTime,
updateTime,
deleteTime,
labels,
state,
instanceType,
machineConfig,
availabilityType,
gceZone,
databaseFlags,
writableNode,
nodes,
queryInsightsConfig,
readPoolConfig,
ipAddress,
publicIpAddress,
reconciling,
etag,
annotations,
clientConnectionConfig,
satisfiesPzs,
pscInstanceConfig,
networkConfig,
outboundPublicIpAddresses
)
SELECT 
'{{ clustersId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ labels }}',
'{{ state }}',
'{{ instanceType }}',
'{{ machineConfig }}',
'{{ availabilityType }}',
'{{ gceZone }}',
'{{ databaseFlags }}',
'{{ writableNode }}',
'{{ nodes }}',
'{{ queryInsightsConfig }}',
'{{ readPoolConfig }}',
'{{ ipAddress }}',
'{{ publicIpAddress }}',
true|false,
'{{ etag }}',
'{{ annotations }}',
'{{ clientConnectionConfig }}',
true|false,
'{{ pscInstanceConfig }}',
'{{ networkConfig }}',
'{{ outboundPublicIpAddresses }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: uid
        value: '{{ uid }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: state
        value: '{{ state }}'
      - name: instanceType
        value: '{{ instanceType }}'
      - name: machineConfig
        value: '{{ machineConfig }}'
      - name: availabilityType
        value: '{{ availabilityType }}'
      - name: gceZone
        value: '{{ gceZone }}'
      - name: databaseFlags
        value: '{{ databaseFlags }}'
      - name: writableNode
        value: '{{ writableNode }}'
      - name: nodes
        value: '{{ nodes }}'
      - name: queryInsightsConfig
        value: '{{ queryInsightsConfig }}'
      - name: readPoolConfig
        value: '{{ readPoolConfig }}'
      - name: ipAddress
        value: '{{ ipAddress }}'
      - name: publicIpAddress
        value: '{{ publicIpAddress }}'
      - name: reconciling
        value: '{{ reconciling }}'
      - name: etag
        value: '{{ etag }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: clientConnectionConfig
        value: '{{ clientConnectionConfig }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: pscInstanceConfig
        value: '{{ pscInstanceConfig }}'
      - name: networkConfig
        value: '{{ networkConfig }}'
      - name: outboundPublicIpAddresses
        value: '{{ outboundPublicIpAddresses }}'

```
</TabItem>
</Tabs>
