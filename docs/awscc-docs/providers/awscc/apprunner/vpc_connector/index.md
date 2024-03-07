---
title: vpc_connector
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connector
  - apprunner
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_connector</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_connector</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apprunner.vpc_connector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpc_connector_name</code></td><td><code>string</code></td><td>A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.</td></tr>
<tr><td><code>vpc_connector_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this VPC connector.</td></tr>
<tr><td><code>vpc_connector_revision</code></td><td><code>integer</code></td><td>The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name.</td></tr>
<tr><td><code>subnets</code></td><td><code>array</code></td><td>A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.</td></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td>A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
vpc_connector_name,
vpc_connector_arn,
vpc_connector_revision,
subnets,
security_groups,
tags
FROM awscc.apprunner.vpc_connector
WHERE region = 'us-east-1'
AND data__Identifier = '{VpcConnectorArn}';
```

## Permissions

To operate on the <code>vpc_connector</code> resource, the following permissions are required:

### Read
```json
apprunner:DescribeVpcConnector
```

### Delete
```json
apprunner:DeleteVpcConnector
```

