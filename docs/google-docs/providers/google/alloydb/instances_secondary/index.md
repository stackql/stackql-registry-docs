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
displayName,
labels,
instanceType,
machineConfig,
availabilityType,
gceZone,
databaseFlags,
queryInsightsConfig,
readPoolConfig,
etag,
annotations,
clientConnectionConfig,
pscInstanceConfig,
networkConfig
)
SELECT 
'{{ clustersId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ labels }}',
'{{ instanceType }}',
'{{ machineConfig }}',
'{{ availabilityType }}',
'{{ gceZone }}',
'{{ databaseFlags }}',
'{{ queryInsightsConfig }}',
'{{ readPoolConfig }}',
'{{ etag }}',
'{{ annotations }}',
'{{ clientConnectionConfig }}',
'{{ pscInstanceConfig }}',
'{{ networkConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
displayName: string
uid: string
createTime: string
updateTime: string
deleteTime: string
labels: object
state: string
instanceType: string
machineConfig:
  cpuCount: integer
availabilityType: string
gceZone: string
databaseFlags: object
writableNode:
  zoneId: string
  id: string
  ip: string
  state: string
nodes:
  - zoneId: string
    id: string
    ip: string
    state: string
queryInsightsConfig:
  recordApplicationTags: boolean
  recordClientAddress: boolean
  queryStringLength: integer
  queryPlansPerMinute: integer
readPoolConfig:
  nodeCount: integer
ipAddress: string
publicIpAddress: string
reconciling: boolean
etag: string
annotations: object
clientConnectionConfig:
  requireConnectors: boolean
  sslConfig:
    sslMode: string
    caSource: string
satisfiesPzs: boolean
pscInstanceConfig:
  serviceAttachmentLink: string
  allowedConsumerProjects:
    - type: string
  pscDnsName: string
networkConfig:
  authorizedExternalNetworks:
    - cidrRange: string
  enablePublicIp: boolean
  enableOutboundPublicIp: boolean
outboundPublicIpAddresses:
  - type: string

```
</TabItem>
</Tabs>
