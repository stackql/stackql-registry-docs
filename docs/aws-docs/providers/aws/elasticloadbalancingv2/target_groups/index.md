---
title: target_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - target_groups
  - elasticloadbalancingv2
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


Used to retrieve a list of <code>target_groups</code> in a region or to create or delete a <code>target_groups</code> resource, use <code>target_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticLoadBalancingV2::TargetGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.target_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="target_group_arn" /></td><td><code>string</code></td><td>The ARN of the Target Group</td></tr>
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
target_group_arn
FROM aws.elasticloadbalancingv2.target_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>target_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- target_group.iql (required properties only)
INSERT INTO aws.elasticloadbalancingv2.target_groups (
 IpAddressType,
 HealthCheckIntervalSeconds,
 Matcher,
 HealthCheckPath,
 Port,
 Targets,
 HealthCheckEnabled,
 ProtocolVersion,
 UnhealthyThresholdCount,
 HealthCheckTimeoutSeconds,
 Name,
 VpcId,
 HealthyThresholdCount,
 HealthCheckProtocol,
 TargetGroupAttributes,
 TargetType,
 HealthCheckPort,
 Protocol,
 Tags,
 region
)
SELECT 
'{{ IpAddressType }}',
 '{{ HealthCheckIntervalSeconds }}',
 '{{ Matcher }}',
 '{{ HealthCheckPath }}',
 '{{ Port }}',
 '{{ Targets }}',
 '{{ HealthCheckEnabled }}',
 '{{ ProtocolVersion }}',
 '{{ UnhealthyThresholdCount }}',
 '{{ HealthCheckTimeoutSeconds }}',
 '{{ Name }}',
 '{{ VpcId }}',
 '{{ HealthyThresholdCount }}',
 '{{ HealthCheckProtocol }}',
 '{{ TargetGroupAttributes }}',
 '{{ TargetType }}',
 '{{ HealthCheckPort }}',
 '{{ Protocol }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- target_group.iql (all properties)
INSERT INTO aws.elasticloadbalancingv2.target_groups (
 IpAddressType,
 HealthCheckIntervalSeconds,
 Matcher,
 HealthCheckPath,
 Port,
 Targets,
 HealthCheckEnabled,
 ProtocolVersion,
 UnhealthyThresholdCount,
 HealthCheckTimeoutSeconds,
 Name,
 VpcId,
 HealthyThresholdCount,
 HealthCheckProtocol,
 TargetGroupAttributes,
 TargetType,
 HealthCheckPort,
 Protocol,
 Tags,
 region
)
SELECT 
 '{{ IpAddressType }}',
 '{{ HealthCheckIntervalSeconds }}',
 '{{ Matcher }}',
 '{{ HealthCheckPath }}',
 '{{ Port }}',
 '{{ Targets }}',
 '{{ HealthCheckEnabled }}',
 '{{ ProtocolVersion }}',
 '{{ UnhealthyThresholdCount }}',
 '{{ HealthCheckTimeoutSeconds }}',
 '{{ Name }}',
 '{{ VpcId }}',
 '{{ HealthyThresholdCount }}',
 '{{ HealthCheckProtocol }}',
 '{{ TargetGroupAttributes }}',
 '{{ TargetType }}',
 '{{ HealthCheckPort }}',
 '{{ Protocol }}',
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
  - name: target_group
    props:
      - name: IpAddressType
        value: '{{ IpAddressType }}'
      - name: HealthCheckIntervalSeconds
        value: '{{ HealthCheckIntervalSeconds }}'
      - name: Matcher
        value:
          GrpcCode: '{{ GrpcCode }}'
          HttpCode: '{{ HttpCode }}'
      - name: HealthCheckPath
        value: '{{ HealthCheckPath }}'
      - name: Port
        value: '{{ Port }}'
      - name: Targets
        value:
          - AvailabilityZone: '{{ AvailabilityZone }}'
            Id: '{{ Id }}'
            Port: '{{ Port }}'
      - name: HealthCheckEnabled
        value: '{{ HealthCheckEnabled }}'
      - name: ProtocolVersion
        value: '{{ ProtocolVersion }}'
      - name: UnhealthyThresholdCount
        value: '{{ UnhealthyThresholdCount }}'
      - name: HealthCheckTimeoutSeconds
        value: '{{ HealthCheckTimeoutSeconds }}'
      - name: Name
        value: '{{ Name }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: HealthyThresholdCount
        value: '{{ HealthyThresholdCount }}'
      - name: HealthCheckProtocol
        value: '{{ HealthCheckProtocol }}'
      - name: TargetGroupAttributes
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: TargetType
        value: '{{ TargetType }}'
      - name: HealthCheckPort
        value: '{{ HealthCheckPort }}'
      - name: Protocol
        value: '{{ Protocol }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.elasticloadbalancingv2.target_groups
WHERE data__Identifier = '<TargetGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>target_groups</code> resource, the following permissions are required:

### Create
```json
elasticloadbalancing:CreateTargetGroup,
elasticloadbalancing:DescribeTargetGroups,
elasticloadbalancing:RegisterTargets,
elasticloadbalancing:ModifyTargetGroupAttributes,
elasticloadbalancing:DescribeTargetHealth,
elasticloadbalancing:AddTags
```

### Delete
```json
elasticloadbalancing:DeleteTargetGroup,
elasticloadbalancing:DescribeTargetGroups
```

### List
```json
elasticloadbalancing:DescribeTargetGroups
```

