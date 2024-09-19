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
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: uid
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: deleteTime
      value: string
    - name: labels
      value: object
    - name: state
      value: string
    - name: instanceType
      value: string
    - name: machineConfig
      value:
        - name: cpuCount
          value: integer
    - name: availabilityType
      value: string
    - name: gceZone
      value: string
    - name: databaseFlags
      value: object
    - name: writableNode
      value:
        - name: zoneId
          value: string
        - name: id
          value: string
        - name: ip
          value: string
        - name: state
          value: string
    - name: nodes
      value:
        - - name: zoneId
            value: string
          - name: id
            value: string
          - name: ip
            value: string
          - name: state
            value: string
    - name: queryInsightsConfig
      value:
        - name: recordApplicationTags
          value: boolean
        - name: recordClientAddress
          value: boolean
        - name: queryStringLength
          value: integer
        - name: queryPlansPerMinute
          value: integer
    - name: readPoolConfig
      value:
        - name: nodeCount
          value: integer
    - name: ipAddress
      value: string
    - name: publicIpAddress
      value: string
    - name: reconciling
      value: boolean
    - name: etag
      value: string
    - name: annotations
      value: object
    - name: clientConnectionConfig
      value:
        - name: requireConnectors
          value: boolean
        - name: sslConfig
          value:
            - name: sslMode
              value: string
            - name: caSource
              value: string
    - name: satisfiesPzs
      value: boolean
    - name: pscInstanceConfig
      value:
        - name: serviceAttachmentLink
          value: string
        - name: allowedConsumerProjects
          value:
            - string
        - name: pscDnsName
          value: string
    - name: networkConfig
      value:
        - name: authorizedExternalNetworks
          value:
            - - name: cidrRange
                value: string
        - name: enablePublicIp
          value: boolean
        - name: enableOutboundPublicIp
          value: boolean
    - name: outboundPublicIpAddresses
      value:
        - string

```
</TabItem>
</Tabs>
