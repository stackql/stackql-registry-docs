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
    - name: displayName
      value: '{{ displayName }}'
    - name: labels
      value: '{{ labels }}'
    - name: instanceType
      value: '{{ instanceType }}'
    - name: machineConfig
      value:
        - name: cpuCount
          value: '{{ cpuCount }}'
    - name: availabilityType
      value: '{{ availabilityType }}'
    - name: gceZone
      value: '{{ gceZone }}'
    - name: databaseFlags
      value: '{{ databaseFlags }}'
    - name: queryInsightsConfig
      value:
        - name: recordApplicationTags
          value: '{{ recordApplicationTags }}'
        - name: recordClientAddress
          value: '{{ recordClientAddress }}'
        - name: queryStringLength
          value: '{{ queryStringLength }}'
        - name: queryPlansPerMinute
          value: '{{ queryPlansPerMinute }}'
    - name: readPoolConfig
      value:
        - name: nodeCount
          value: '{{ nodeCount }}'
    - name: etag
      value: '{{ etag }}'
    - name: annotations
      value: '{{ annotations }}'
    - name: clientConnectionConfig
      value:
        - name: requireConnectors
          value: '{{ requireConnectors }}'
        - name: sslConfig
          value:
            - name: sslMode
              value: '{{ sslMode }}'
            - name: caSource
              value: '{{ caSource }}'
    - name: pscInstanceConfig
      value:
        - name: allowedConsumerProjects
          value:
            - name: type
              value: '{{ type }}'
    - name: networkConfig
      value:
        - name: authorizedExternalNetworks
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: enablePublicIp
          value: '{{ enablePublicIp }}'
        - name: enableOutboundPublicIp
          value: '{{ enableOutboundPublicIp }}'

```
</TabItem>
</Tabs>
