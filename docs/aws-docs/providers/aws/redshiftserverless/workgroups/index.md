---
title: workgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - workgroups
  - redshiftserverless
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

Creates, updates, deletes or gets a <code>workgroup</code> resource or lists <code>workgroups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RedshiftServerless::Workgroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshiftserverless.workgroups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workgroup_name" /></td><td><code>string</code></td><td>The name of the workgroup.</td></tr>
<tr><td><CopyableCode code="namespace_name" /></td><td><code>string</code></td><td>The namespace the workgroup is associated with.</td></tr>
<tr><td><CopyableCode code="base_capacity" /></td><td><code>integer</code></td><td>The base compute capacity of the workgroup in Redshift Processing Units (RPUs).</td></tr>
<tr><td><CopyableCode code="max_capacity" /></td><td><code>integer</code></td><td>The max compute capacity of the workgroup in Redshift Processing Units (RPUs).</td></tr>
<tr><td><CopyableCode code="enhanced_vpc_routing" /></td><td><code>boolean</code></td><td>The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.</td></tr>
<tr><td><CopyableCode code="config_parameters" /></td><td><code>array</code></td><td>A list of parameters to set for finer control over a database. Available options are datestyle, enable_user_activity_logging, query_group, search_path, max_query_execution_time, and require_ssl.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>A list of security group IDs to associate with the workgroup.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>A list of subnet IDs the workgroup is associated with.</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>A value that specifies whether the workgroup can be accessible from a public network.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</td></tr>
<tr><td><CopyableCode code="price_performance_target" /></td><td><code>object</code></td><td>A property that represents the price performance target settings for the workgroup.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The map of the key-value pairs used to tag the workgroup.</td></tr>
<tr><td><CopyableCode code="workgroup" /></td><td><code>object</code></td><td>Definition for workgroup resource</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html"><code>AWS::RedshiftServerless::Workgroup</code></a>.

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
    <td><CopyableCode code="WorkgroupName, region" /></td>
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
Gets all <code>workgroups</code> in a region.
```sql
SELECT
region,
workgroup_name,
namespace_name,
base_capacity,
max_capacity,
enhanced_vpc_routing,
config_parameters,
security_group_ids,
subnet_ids,
publicly_accessible,
port,
price_performance_target,
tags,
workgroup
FROM aws.redshiftserverless.workgroups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>workgroup</code>.
```sql
SELECT
region,
workgroup_name,
namespace_name,
base_capacity,
max_capacity,
enhanced_vpc_routing,
config_parameters,
security_group_ids,
subnet_ids,
publicly_accessible,
port,
price_performance_target,
tags,
workgroup
FROM aws.redshiftserverless.workgroups
WHERE region = 'us-east-1' AND data__Identifier = '<WorkgroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workgroup</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.redshiftserverless.workgroups (
 WorkgroupName,
 region
)
SELECT 
'{{ WorkgroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.redshiftserverless.workgroups (
 WorkgroupName,
 NamespaceName,
 BaseCapacity,
 MaxCapacity,
 EnhancedVpcRouting,
 ConfigParameters,
 SecurityGroupIds,
 SubnetIds,
 PubliclyAccessible,
 Port,
 PricePerformanceTarget,
 Tags,
 region
)
SELECT 
 '{{ WorkgroupName }}',
 '{{ NamespaceName }}',
 '{{ BaseCapacity }}',
 '{{ MaxCapacity }}',
 '{{ EnhancedVpcRouting }}',
 '{{ ConfigParameters }}',
 '{{ SecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ PubliclyAccessible }}',
 '{{ Port }}',
 '{{ PricePerformanceTarget }}',
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
  - name: workgroup
    props:
      - name: WorkgroupName
        value: '{{ WorkgroupName }}'
      - name: NamespaceName
        value: '{{ NamespaceName }}'
      - name: BaseCapacity
        value: '{{ BaseCapacity }}'
      - name: MaxCapacity
        value: '{{ MaxCapacity }}'
      - name: EnhancedVpcRouting
        value: '{{ EnhancedVpcRouting }}'
      - name: ConfigParameters
        value:
          - ParameterKey: '{{ ParameterKey }}'
            ParameterValue: '{{ ParameterValue }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: Port
        value: '{{ Port }}'
      - name: PricePerformanceTarget
        value:
          Status: '{{ Status }}'
          Level: '{{ Level }}'
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
DELETE FROM aws.redshiftserverless.workgroups
WHERE data__Identifier = '<WorkgroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>workgroups</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:CreateNamespace,
redshift-serverless:CreateWorkgroup,
redshift-serverless:GetWorkgroup,
redshift-serverless:GetNamespace,
redshift-serverless:ListTagsForResource,
redshift-serverless:TagResource
```

### Read
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:GetWorkgroup,
redshift-serverless:ListTagsForResource
```

### Update
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:ListTagsForResource,
redshift-serverless:TagResource,
redshift-serverless:UntagResource,
redshift-serverless:GetWorkgroup,
redshift-serverless:UpdateWorkgroup,
redshift-serverless:ListTagsForResource,
redshift-serverless:TagResource,
redshift-serverless:UntagResource
```

### Delete
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:GetWorkgroup,
redshift-serverless:GetNamespace,
redshift-serverless:DeleteWorkgroup,
redshift-serverless:ListTagsForResource,
redshift-serverless:UntagResource
```

### List
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:ListWorkgroups,
redshift-serverless:ListTagsForResource
```
