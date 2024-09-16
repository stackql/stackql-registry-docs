---
title: target_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - target_pools
  - compute
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

Creates, updates, deletes, gets or lists a <code>target_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="backupPool" /> | `string` | The server-defined URL for the resource. This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool, and its failoverRatio field is properly set to a value between [0, 1]. backupPool and failoverRatio together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below failoverRatio, traffic arriving at the load-balanced IP will be directed to the backup pool. In case where failoverRatio and backupPool are not set, or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the "force" mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="failoverRatio" /> | `number` | This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool (i.e., not as a backup pool to some other target pool). The value of the field must be in [0, 1]. If set, backupPool must also be set. They together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below this number, traffic arriving at the load-balanced IP will be directed to the backup pool. In case where failoverRatio is not set or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the "force" mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy. |
| <CopyableCode code="healthChecks" /> | `array` | The URL of the HttpHealthCheck resource. A member instance in this pool is considered healthy if and only if the health checks pass. Only legacy HttpHealthChecks are supported. Only one health check may be specified. |
| <CopyableCode code="instances" /> | `array` | A list of resource URLs to the virtual machine instances serving this pool. They must live in zones contained in the same region as this pool. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#targetPool for target pools. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the target pool resides. |
| <CopyableCode code="securityPolicy" /> | `string` | [Output Only] The resource URL for the security policy associated with this target pool. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="sessionAffinity" /> | `string` | Session affinity option, must be one of the following values: NONE: Connections from the same client IP may go to any instance in the pool. CLIENT_IP: Connections from the same client IP will go to the same instance in the pool while that instance remains healthy. CLIENT_IP_PROTO: Connections from the same client IP with the same IP protocol will go to the same instance in the pool while that instance remains healthy. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of target pools. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, targetPool" /> | Returns the specified target pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of target pools available to the specified project and region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a target pool in the specified project and region using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, targetPool" /> | Deletes the specified target pool. |
| <CopyableCode code="set_backup" /> | `EXEC` | <CopyableCode code="project, region, targetPool" /> | Changes a backup target pool's configurations. |
| <CopyableCode code="set_security_policy" /> | `EXEC` | <CopyableCode code="project, region, targetPool" /> | Sets the Google Cloud Armor security policy for the specified target pool. For more information, see Google Cloud Armor Overview |

## `SELECT` examples

Retrieves an aggregated list of target pools. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
backupPool,
creationTimestamp,
failoverRatio,
healthChecks,
instances,
kind,
region,
securityPolicy,
selfLink,
sessionAffinity
FROM google.compute.target_pools
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_pools</code> resource.

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
INSERT INTO google.compute.target_pools (
project,
region,
kind,
id,
creationTimestamp,
name,
description,
region,
healthChecks,
instances,
sessionAffinity,
failoverRatio,
backupPool,
selfLink,
securityPolicy
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ healthChecks }}',
'{{ instances }}',
'{{ sessionAffinity }}',
number,
'{{ backupPool }}',
'{{ selfLink }}',
'{{ securityPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: '{{ kind }}'
    - name: id
      value: '{{ id }}'
    - name: creationTimestamp
      value: '{{ creationTimestamp }}'
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: region
      value: '{{ region }}'
    - name: healthChecks
      value: '{{ healthChecks }}'
    - name: instances
      value: '{{ instances }}'
    - name: sessionAffinity
      value: '{{ sessionAffinity }}'
    - name: failoverRatio
      value: '{{ failoverRatio }}'
    - name: backupPool
      value: '{{ backupPool }}'
    - name: selfLink
      value: '{{ selfLink }}'
    - name: securityPolicy
      value: '{{ securityPolicy }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>target_pools</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.target_pools
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND targetPool = '{{ targetPool }}';
```
