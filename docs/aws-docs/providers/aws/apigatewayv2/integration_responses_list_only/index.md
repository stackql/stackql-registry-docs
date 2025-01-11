---
title: integration_responses_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_responses_list_only
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

Lists <code>integration_responses</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/integration_responses/"><code>integration_responses</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_responses_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::IntegrationResponse</code> resource updates an integration response for an WebSocket API. For more information, see &#91;Set up WebSocket API Integration Responses in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-responses.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.integration_responses_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="integration_response_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="integration_id" /></td><td><code>string</code></td><td>The integration ID.</td></tr>
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
Lists all <code>integration_responses</code> in a region.
```sql
SELECT
region,
api_id,
integration_id,
integration_response_id
FROM aws.apigatewayv2.integration_responses_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>integration_responses_list_only</code> resource, see <a href="/providers/aws/apigatewayv2/integration_responses/#permissions"><code>integration_responses</code></a>

