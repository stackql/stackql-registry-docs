---
title: vpc_links_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_links_list_only
  - apigatewayv2
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

Lists <code>vpc_links</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/vpc_links/"><code>vpc_links</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_links_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::VpcLink</code> resource creates a VPC link. Supported only for HTTP APIs. The VPC link status must transition from <code>PENDING</code> to <code>AVAILABLE</code> to successfully create a VPC link, which can take up to 10 minutes. To learn more, see &#91;Working with VPC Links for HTTP APIs&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.vpc_links_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vpc_link_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>A list of subnet IDs to include in the VPC link.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>A list of security group IDs for the VPC link.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the VPC link.</td></tr>
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
Lists all <code>vpc_links</code> in a region.
```sql
SELECT
region,
vpc_link_id
FROM aws.apigatewayv2.vpc_links_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_links_list_only</code> resource, see <a href="/providers/aws/apigatewayv2/vpc_links/#permissions"><code>vpc_links</code></a>


