---
title: models_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - models_list_only
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

Lists <code>models</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/models/"><code>models</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::Model</code> resource updates data model for a WebSocket API. For more information, see &#91;Model Selection Expressions&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.models_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="model_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The API identifier.</td></tr>
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
Lists all <code>models</code> in a region.
```sql
SELECT
region,
api_id,
model_id
FROM aws.apigatewayv2.models_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>models_list_only</code> resource, see <a href="/providers/aws/apigatewayv2/models/#permissions"><code>models</code></a>

