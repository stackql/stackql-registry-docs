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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>vpc_connector</code> resource, use <code>vpc_connectors</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.vpc_connector" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="vpc_connector_name" /></td><td><code>string</code></td><td>A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.</td></tr>
<tr><td><CopyableCode code="vpc_connector_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this VPC connector.</td></tr>
<tr><td><CopyableCode code="vpc_connector_revision" /></td><td><code>integer</code></td><td>The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name.</td></tr>
<tr><td><CopyableCode code="subnets" /></td><td><code>array</code></td><td>A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
vpc_connector_name,
vpc_connector_arn,
vpc_connector_revision,
subnets,
security_groups,
tags
FROM aws.apprunner.vpc_connector
WHERE region = 'us-east-1' AND data__Identifier = '<VpcConnectorArn>';
```


## Permissions

To operate on the <code>vpc_connector</code> resource, the following permissions are required:

### Read
```json
apprunner:DescribeVpcConnector
```

