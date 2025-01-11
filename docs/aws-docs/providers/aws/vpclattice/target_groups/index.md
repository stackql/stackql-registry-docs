---
title: target_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - target_groups
  - vpclattice
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

Creates, updates, deletes or gets a <code>target_group</code> resource or lists <code>target_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.target_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-targetgroup.html"><code>AWS::VpcLattice::TargetGroup</code></a>.

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
    <td><CopyableCode code="Type, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>target_groups</code> in a region.
```sql
SELECT
region,
arn,
config,
created_at,
id,
last_updated_at,
name,
status,
type,
targets,
tags
FROM aws.vpclattice.target_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>target_group</code>.
```sql
SELECT
region,
arn,
config,
created_at,
id,
last_updated_at,
name,
status,
type,
targets,
tags
FROM aws.vpclattice.target_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

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
/*+ create */
INSERT INTO aws.vpclattice.target_groups (
 Type,
 region
)
SELECT 
'{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.vpclattice.target_groups (
 Config,
 Name,
 Type,
 Targets,
 Tags,
 region
)
SELECT 
 '{{ Config }}',
 '{{ Name }}',
 '{{ Type }}',
 '{{ Targets }}',
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
      - name: Config
        value:
          Port: '{{ Port }}'
          Protocol: '{{ Protocol }}'
          ProtocolVersion: '{{ ProtocolVersion }}'
          IpAddressType: '{{ IpAddressType }}'
          LambdaEventStructureVersion: '{{ LambdaEventStructureVersion }}'
          VpcIdentifier: '{{ VpcIdentifier }}'
          HealthCheck:
            Enabled: '{{ Enabled }}'
            Protocol: '{{ Protocol }}'
            ProtocolVersion: '{{ ProtocolVersion }}'
            Port: '{{ Port }}'
            Path: '{{ Path }}'
            HealthCheckIntervalSeconds: '{{ HealthCheckIntervalSeconds }}'
            HealthCheckTimeoutSeconds: '{{ HealthCheckTimeoutSeconds }}'
            HealthyThresholdCount: '{{ HealthyThresholdCount }}'
            UnhealthyThresholdCount: '{{ UnhealthyThresholdCount }}'
            Matcher:
              HttpCode: '{{ HttpCode }}'
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
      - name: Targets
        value:
          - Id: '{{ Id }}'
            Port: '{{ Port }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.vpclattice.target_groups
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>target_groups</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateTargetGroup,
vpc-lattice:GetTargetGroup,
vpc-lattice:RegisterTargets,
vpc-lattice:ListTargets,
vpc-lattice:ListTagsForResource,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
ec2:DescribeVpcs,
ec2:DescribeInstances,
ec2:DescribeSubnets,
ec2:DescribeAvailabilityZoneMappings,
lambda:Invoke,
lambda:AddPermission,
elasticloadbalancing:DescribeLoadBalancers,
iam:CreateServiceLinkedRole
```

### Read
```json
vpc-lattice:GetTargetGroup,
vpc-lattice:ListTargets,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:UpdateTargetGroup,
vpc-lattice:GetTargetGroup,
vpc-lattice:ListTargets,
vpc-lattice:RegisterTargets,
vpc-lattice:DeregisterTargets,
ec2:DescribeVpcs,
ec2:DescribeInstances,
ec2:DescribeSubnets,
ec2:DescribeAvailabilityZoneMappings,
elasticloadbalancing:DescribeLoadBalancers,
lambda:Invoke,
lambda:RemovePermission,
lambda:AddPermission,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteTargetGroup,
vpc-lattice:GetTargetGroup,
vpc-lattice:DeregisterTargets,
vpc-lattice:ListTargets,
lambda:RemovePermission
```

### List
```json
vpc-lattice:ListTargetGroups
```
