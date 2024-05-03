---
title: workgroup
hide_title: false
hide_table_of_contents: false
keywords:
  - workgroup
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

Gets or operates on an individual <code>workgroup</code> resource, use <code>workgroups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workgroup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RedshiftServerless::Workgroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshiftserverless.workgroup" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workgroup_name" /></td><td><code>string</code></td><td>The name of the workgroup.</td></tr>
<tr><td><CopyableCode code="namespace_name" /></td><td><code>string</code></td><td>The namespace the workgroup is associated with.</td></tr>
<tr><td><CopyableCode code="base_capacity" /></td><td><code>integer</code></td><td>The base compute capacity of the workgroup in Redshift Processing Units (RPUs).</td></tr>
<tr><td><CopyableCode code="max_capacity" /></td><td><code>integer</code></td><td>The max compute capacity of the workgroup in Redshift Processing Units (RPUs).</td></tr>
<tr><td><CopyableCode code="enhanced_vpc_routing" /></td><td><code>boolean</code></td><td>The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.</td></tr>
<tr><td><CopyableCode code="config_parameters" /></td><td><code>array</code></td><td>A list of parameters to set for finer control over a database. Available options are datestyle, enable_user_activity_logging, query_group, search_path, max_query_execution_time, and require_ssl.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>A list of security group IDs to associate with the workgroup.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>A list of subnet IDs the workgroup is associated with.</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>A value that specifies whether the workgroup can be accessible from a public network.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The map of the key-value pairs used to tag the workgroup.</td></tr>
<tr><td><CopyableCode code="workgroup" /></td><td><code>object</code></td><td>Definition for workgroup resource</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
tags,
workgroup
FROM aws.redshiftserverless.workgroup
WHERE data__Identifier = '<WorkgroupName>';
```

## Permissions

To operate on the <code>workgroup</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:GetWorkgroup
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
redshift-serverless:UpdateWorkgroup
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
redshift-serverless:DeleteWorkgroup
```

