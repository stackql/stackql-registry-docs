---
title: domain_name_v2_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name_v2_tags
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

Expands all tag keys and values for <code>domain_name_v2s</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name_v2_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApiGateway::DomainNameV2.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.domain_name_v2_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_configuration" /></td><td><code>object</code></td><td>The <code>EndpointConfiguration</code> property type specifies the endpoint types of a REST API.<br /><code>EndpointConfiguration</code> is a property of the &#91;AWS::ApiGateway::RestApi&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html) resource.</td></tr>
<tr><td><CopyableCode code="security_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name_arn" /></td><td><code>string</code></td><td>The amazon resource name (ARN) of the domain name resource.</td></tr>
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
Expands tags for all <code>domain_name_v2s</code> in a region.
```sql
SELECT
region,
certificate_arn,
domain_name,
endpoint_configuration,
security_policy,
policy,
domain_name_id,
domain_name_arn,
tag_key,
tag_value
FROM aws.apigateway.domain_name_v2_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>domain_name_v2_tags</code> resource, see <a href="/providers/aws/apigateway/domain_name_v2s/#permissions"><code>domain_name_v2s</code></a>

