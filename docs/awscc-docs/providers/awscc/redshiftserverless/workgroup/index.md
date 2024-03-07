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
Gets an individual <code>workgroup</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workgroup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workgroup</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshiftserverless.workgroup</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workgroup_name</code></td><td><code>string</code></td><td>The name of the workgroup.</td></tr>
<tr><td><code>namespace_name</code></td><td><code>string</code></td><td>The namespace the workgroup is associated with.</td></tr>
<tr><td><code>base_capacity</code></td><td><code>integer</code></td><td>The base compute capacity of the workgroup in Redshift Processing Units (RPUs).</td></tr>
<tr><td><code>max_capacity</code></td><td><code>integer</code></td><td>The max compute capacity of the workgroup in Redshift Processing Units (RPUs).</td></tr>
<tr><td><code>enhanced_vpc_routing</code></td><td><code>boolean</code></td><td>The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.</td></tr>
<tr><td><code>config_parameters</code></td><td><code>array</code></td><td>A list of parameters to set for finer control over a database. Available options are datestyle, enable_user_activity_logging, query_group, search_path, max_query_execution_time, and require_ssl.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>A list of security group IDs to associate with the workgroup.</td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td>A list of subnet IDs the workgroup is associated with.</td></tr>
<tr><td><code>publicly_accessible</code></td><td><code>boolean</code></td><td>A value that specifies whether the workgroup can be accessible from a public network.</td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The map of the key-value pairs used to tag the workgroup.</td></tr>
<tr><td><code>workgroup</code></td><td><code>object</code></td><td>Definition for workgroup resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
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
FROM awscc.redshiftserverless.workgroup
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;WorkgroupName&gt;'
```
