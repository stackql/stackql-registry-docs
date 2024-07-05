---
title: api_key_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - api_key_tags
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

Expands all tag keys and values for <code>api_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_key_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::ApiKey</code> resource creates a unique key that you can distribute to clients who are executing API Gateway <code>Method</code> resources that require an API key. To specify which API key clients must use, map the API key with the <code>RestApi</code> and <code>Stage</code> resources that include the methods that require a key.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.api_key_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_id" /></td><td><code>string</code></td><td>An MKT customer identifier, when integrating with the AWS SaaS Marketplace.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the ApiKey.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>Specifies whether the ApiKey can be used by callers.</td></tr>
<tr><td><CopyableCode code="generate_distinct_id" /></td><td><code>boolean</code></td><td>Specifies whether (<code>true</code>) or not (<code>false</code>) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the API key. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the API key name. For more information, see &#91;Name Type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="stage_keys" /></td><td><code>array</code></td><td>DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.</td></tr>
<tr><td><CopyableCode code="value" /></td><td><code>string</code></td><td>Specifies a value of the API key.</td></tr>
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
Expands tags for all <code>api_keys</code> in a region.
```sql
SELECT
region,
api_key_id,
customer_id,
description,
enabled,
generate_distinct_id,
name,
stage_keys,
value,
tag_key,
tag_value
FROM aws.apigateway.api_key_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>api_key_tags</code> resource, see <a href="/providers/aws/apigateway/api_keys/#permissions"><code>api_keys</code></a>


