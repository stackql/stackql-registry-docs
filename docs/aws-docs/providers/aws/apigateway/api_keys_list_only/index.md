---
title: api_keys_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys_list_only
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

Lists <code>api_keys</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/api_keys/"><code>api_keys</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::ApiKey</code> resource creates a unique key that you can distribute to clients who are executing API Gateway <code>Method</code> resources that require an API key. To specify which API key clients must use, map the API key with the <code>RestApi</code> and <code>Stage</code> resources that include the methods that require a key.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.api_keys_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_key_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>api_keys</code> in a region.
```sql
SELECT
region,
api_key_id
FROM aws.apigateway.api_keys_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>api_keys_list_only</code> resource, see <a href="/providers/aws/apigateway/api_keys/#permissions"><code>api_keys</code></a>

