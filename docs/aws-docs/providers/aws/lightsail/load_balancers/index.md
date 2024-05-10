---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - lightsail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>load_balancers</code> in a region or to create or delete a <code>load_balancers</code> resource, use <code>load_balancer</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::LoadBalancer</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.load_balancers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="load_balancer_name" /></td><td><code>string</code></td><td>The name of your load balancer.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
load_balancer_name
FROM aws.lightsail.load_balancers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>load_balancer</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- load_balancer.iql (required properties only)
INSERT INTO aws.lightsail.load_balancers (
 LoadBalancerName,
 InstancePort,
 region
)
SELECT 
'{{ LoadBalancerName }}',
 '{{ InstancePort }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- load_balancer.iql (all properties)
INSERT INTO aws.lightsail.load_balancers (
 LoadBalancerName,
 InstancePort,
 IpAddressType,
 AttachedInstances,
 HealthCheckPath,
 SessionStickinessEnabled,
 SessionStickinessLBCookieDurationSeconds,
 TlsPolicyName,
 Tags,
 region
)
SELECT 
 '{{ LoadBalancerName }}',
 '{{ InstancePort }}',
 '{{ IpAddressType }}',
 '{{ AttachedInstances }}',
 '{{ HealthCheckPath }}',
 '{{ SessionStickinessEnabled }}',
 '{{ SessionStickinessLBCookieDurationSeconds }}',
 '{{ TlsPolicyName }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: load_balancer
    props:
      - name: LoadBalancerName
        value: '{{ LoadBalancerName }}'
      - name: InstancePort
        value: '{{ InstancePort }}'
      - name: IpAddressType
        value: '{{ IpAddressType }}'
      - name: AttachedInstances
        value:
          - '{{ AttachedInstances[0] }}'
      - name: HealthCheckPath
        value: '{{ HealthCheckPath }}'
      - name: SessionStickinessEnabled
        value: '{{ SessionStickinessEnabled }}'
      - name: SessionStickinessLBCookieDurationSeconds
        value: '{{ SessionStickinessLBCookieDurationSeconds }}'
      - name: TlsPolicyName
        value: '{{ TlsPolicyName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lightsail.load_balancers
WHERE data__Identifier = '<LoadBalancerName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>load_balancers</code> resource, the following permissions are required:

### Create
```json
lightsail:CreateLoadBalancer,
lightsail:GetLoadBalancer,
lightsail:GetLoadBalancers,
lightsail:GetInstance,
lightsail:AttachInstancesToLoadBalancer,
lightsail:DetachInstancesFromLoadBalancer,
lightsail:UpdateLoadBalancerAttribute,
lightsail:TagResource,
lightsail:UntagResource
```

### Delete
```json
lightsail:DeleteLoadBalancer,
lightsail:GetLoadBalancer,
lightsail:GetLoadBalancers
```

### List
```json
lightsail:GetLoadBalancers
```

