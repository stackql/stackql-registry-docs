---
title: request_validators
hide_title: false
hide_table_of_contents: false
keywords:
  - request_validators
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
Retrieves a list of <code>request_validators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>request_validators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::RequestValidator`` resource sets up basic validation rules for incoming requests to your API. For more information, see &#91;Enable Basic Request Validation for an API in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;api-gateway-method-request-validation.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.request_validators</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>request_validator_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
rest_api_id,
request_validator_id
FROM aws.apigateway.request_validators
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>request_validators</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET
```

### List
```json
apigateway:GET
```

