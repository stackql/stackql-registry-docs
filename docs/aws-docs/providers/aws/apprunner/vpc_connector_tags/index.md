---
title: vpc_connector_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connector_tags
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

Expands all tag keys and values for <code>vpc_connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connector_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.vpc_connector_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vpc_connector_name" /></td><td><code>string</code></td><td>A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.</td></tr>
<tr><td><CopyableCode code="vpc_connector_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this VPC connector.</td></tr>
<tr><td><CopyableCode code="vpc_connector_revision" /></td><td><code>integer</code></td><td>The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name.</td></tr>
<tr><td><CopyableCode code="subnets" /></td><td><code>array</code></td><td>A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>vpc_connectors</code> in a region.
```sql
SELECT
region,
vpc_connector_name,
vpc_connector_arn,
vpc_connector_revision,
subnets,
security_groups,
tag_key,
tag_value
FROM aws.apprunner.vpc_connector_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_connector_tags</code> resource, see <a href="/providers/aws/apprunner/vpc_connectors/#permissions"><code>vpc_connectors</code></a>


