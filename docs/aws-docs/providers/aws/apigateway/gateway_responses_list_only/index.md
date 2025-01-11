---
title: gateway_responses_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_responses_list_only
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

Lists <code>gateway_responses</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/gateway_responses/"><code>gateway_responses</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_responses_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::GatewayResponse</code> resource creates a gateway response for your API. For more information, see &#91;API Gateway Responses&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html#api-gateway-gatewayResponse-definition) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.gateway_responses_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>gateway_responses</code> in a region.
```sql
SELECT
region,
id
FROM aws.apigateway.gateway_responses_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>gateway_responses_list_only</code> resource, see <a href="/providers/aws/apigateway/gateway_responses/#permissions"><code>gateway_responses</code></a>

