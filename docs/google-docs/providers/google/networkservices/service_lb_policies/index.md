---
title: service_lb_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - service_lb_policies
  - networkservices
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

Creates, updates, deletes, gets or lists a <code>service_lb_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_lb_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.service_lb_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the ServiceLbPolicy resource. It matches pattern `projects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy_name}`. |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="autoCapacityDrain" /> | `object` | Option to specify if an unhealthy IG/NEG should be considered for global load balancing and traffic routing. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when this resource was created. |
| <CopyableCode code="failoverConfig" /> | `object` | Option to specify health based failover behavior. This is not related to Network load balancer FailoverPolicy. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the ServiceLbPolicy resource. |
| <CopyableCode code="loadBalancingAlgorithm" /> | `string` | Optional. The type of load balancing algorithm to be used. The default behavior is WATERFALL_BY_REGION. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when this resource was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, serviceLbPoliciesId" /> | Gets details of a single ServiceLbPolicy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ServiceLbPolicies in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ServiceLbPolicy in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, serviceLbPoliciesId" /> | Deletes a single ServiceLbPolicy. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, serviceLbPoliciesId" /> | Updates the parameters of a single ServiceLbPolicy. |

## `SELECT` examples

Lists ServiceLbPolicies in a given project and location.

```sql
SELECT
name,
description,
autoCapacityDrain,
createTime,
failoverConfig,
labels,
loadBalancingAlgorithm,
updateTime
FROM google.networkservices.service_lb_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_lb_policies</code> resource.

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
INSERT INTO google.networkservices.service_lb_policies (
locationsId,
projectsId,
name,
labels,
description,
loadBalancingAlgorithm,
autoCapacityDrain,
failoverConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ description }}',
'{{ loadBalancingAlgorithm }}',
'{{ autoCapacityDrain }}',
'{{ failoverConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
labels: object
description: string
loadBalancingAlgorithm: string
autoCapacityDrain:
  enable: boolean
failoverConfig:
  failoverHealthThreshold: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>service_lb_policies</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.service_lb_policies
SET 
name = '{{ name }}',
labels = '{{ labels }}',
description = '{{ description }}',
loadBalancingAlgorithm = '{{ loadBalancingAlgorithm }}',
autoCapacityDrain = '{{ autoCapacityDrain }}',
failoverConfig = '{{ failoverConfig }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceLbPoliciesId = '{{ serviceLbPoliciesId }}';
```

## `DELETE` example

Deletes the specified <code>service_lb_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.service_lb_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceLbPoliciesId = '{{ serviceLbPoliciesId }}';
```
