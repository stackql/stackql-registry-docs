---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - vpcaccess
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

Creates, updates, deletes, gets or lists a <code>connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vpcaccess.connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name in the format `projects/*/locations/*/connectors/*`. |
| <CopyableCode code="connectedProjects" /> | `array` | Output only. List of projects using the connector. |
| <CopyableCode code="ipCidrRange" /> | `string` | Optional. The range of internal addresses that follows RFC 4632 notation. Example: `10.132.0.0/28`. |
| <CopyableCode code="machineType" /> | `string` | Machine type of VM Instance underlying connector. Default is e2-micro |
| <CopyableCode code="maxInstances" /> | `integer` | Maximum value of instances in autoscaling group underlying the connector. |
| <CopyableCode code="maxThroughput" /> | `integer` | Maximum throughput of the connector in Mbps. Refers to the expected throughput when using an `e2-micro` machine type. Value must be a multiple of 100 from 300 through 1000. Must be higher than the value specified by --min-throughput. If both max-throughput and max-instances are provided, max-instances takes precedence over max-throughput. The use of `max-throughput` is discouraged in favor of `max-instances`. |
| <CopyableCode code="minInstances" /> | `integer` | Minimum value of instances in autoscaling group underlying the connector. |
| <CopyableCode code="minThroughput" /> | `integer` | Minimum throughput of the connector in Mbps. Refers to the expected throughput when using an `e2-micro` machine type. Value must be a multiple of 100 from 200 through 900. Must be lower than the value specified by --max-throughput. If both min-throughput and min-instances are provided, min-instances takes precedence over min-throughput. The use of `min-throughput` is discouraged in favor of `min-instances`. |
| <CopyableCode code="network" /> | `string` | Optional. Name of a VPC network. |
| <CopyableCode code="state" /> | `string` | Output only. State of the VPC access connector. |
| <CopyableCode code="subnet" /> | `object` | The subnet in which to house the connector |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectorsId, locationsId, projectsId" /> | Gets a Serverless VPC Access connector. Returns NOT_FOUND if the resource does not exist. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Serverless VPC Access connectors. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Serverless VPC Access connector, returns an operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectorsId, locationsId, projectsId" /> | Deletes a Serverless VPC Access connector. Returns NOT_FOUND if the resource does not exist. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="connectorsId, locationsId, projectsId" /> | Updates a Serverless VPC Access connector, returns an operation. |

## `SELECT` examples

Lists Serverless VPC Access connectors.

```sql
SELECT
name,
connectedProjects,
ipCidrRange,
machineType,
maxInstances,
maxThroughput,
minInstances,
minThroughput,
network,
state,
subnet
FROM google.vpcaccess.connectors
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connectors</code> resource.

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
INSERT INTO google.vpcaccess.connectors (
locationsId,
projectsId,
name,
network,
ipCidrRange,
state,
minThroughput,
maxThroughput,
connectedProjects,
subnet,
machineType,
minInstances,
maxInstances
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ network }}',
'{{ ipCidrRange }}',
'{{ state }}',
'{{ minThroughput }}',
'{{ maxThroughput }}',
'{{ connectedProjects }}',
'{{ subnet }}',
'{{ machineType }}',
'{{ minInstances }}',
'{{ maxInstances }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: network
      value: '{{ network }}'
    - name: ipCidrRange
      value: '{{ ipCidrRange }}'
    - name: state
      value: '{{ state }}'
    - name: minThroughput
      value: '{{ minThroughput }}'
    - name: maxThroughput
      value: '{{ maxThroughput }}'
    - name: connectedProjects
      value: '{{ connectedProjects }}'
    - name: subnet
      value: '{{ subnet }}'
    - name: machineType
      value: '{{ machineType }}'
    - name: minInstances
      value: '{{ minInstances }}'
    - name: maxInstances
      value: '{{ maxInstances }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connectors</code> resource.

```sql
/*+ update */
UPDATE google.vpcaccess.connectors
SET 
name = '{{ name }}',
network = '{{ network }}',
ipCidrRange = '{{ ipCidrRange }}',
state = '{{ state }}',
minThroughput = '{{ minThroughput }}',
maxThroughput = '{{ maxThroughput }}',
connectedProjects = '{{ connectedProjects }}',
subnet = '{{ subnet }}',
machineType = '{{ machineType }}',
minInstances = '{{ minInstances }}',
maxInstances = '{{ maxInstances }}'
WHERE 
connectorsId = '{{ connectorsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>connectors</code> resource.

```sql
/*+ delete */
DELETE FROM google.vpcaccess.connectors
WHERE connectorsId = '{{ connectorsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
