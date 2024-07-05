---
title: vpc_link_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_link_tags
  - apigateway
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

Expands all tag keys and values for <code>vpc_links</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_link_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::VpcLink</code> resource creates an API Gateway VPC link for a REST API to access resources in an Amazon Virtual Private Cloud (VPC). For more information, see &#91;vpclink:create&#93;(https://docs.aws.amazon.com/apigateway/latest/api/API_CreateVpcLink.html) in the <code>Amazon API Gateway REST API Reference</code>.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.vpc_link_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name used to label and identify the VPC link.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the VPC link.</td></tr>
<tr><td><CopyableCode code="target_arns" /></td><td><code>array</code></td><td>The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS-account of the API owner.</td></tr>
<tr><td><CopyableCode code="vpc_link_id" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>vpc_links</code> in a region.
```sql
SELECT
region,
name,
description,
target_arns,
vpc_link_id,
tag_key,
tag_value
FROM aws.apigateway.vpc_link_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_link_tags</code> resource, see <a href="/providers/aws/apigateway/vpc_links/#permissions"><code>vpc_links</code></a>


