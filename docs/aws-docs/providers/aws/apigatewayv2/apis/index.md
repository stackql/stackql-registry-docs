---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
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


Used to retrieve a list of <code>apis</code> in a region or to create or delete a <code>apis</code> resource, use <code>api</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::Api`` resource creates an API. WebSocket APIs and HTTP APIs are supported. For more information about WebSocket APIs, see &#91;About WebSocket APIs in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;apigateway-websocket-api-overview.html) in the *API Gateway Developer Guide*. For more information about HTTP APIs, see &#91;HTTP APIs&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;http-api.html) in the *API Gateway Developer Guide.*</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.apis" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
api_id
FROM aws.apigatewayv2.apis
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "RouteSelectionExpression": "{{ RouteSelectionExpression }}",
 "BodyS3Location": {
  "Etag": "{{ Etag }}",
  "Bucket": "{{ Bucket }}",
  "Version": "{{ Version }}",
  "Key": "{{ Key }}"
 },
 "Description": "{{ Description }}",
 "BasePath": "{{ BasePath }}",
 "FailOnWarnings": "{{ FailOnWarnings }}",
 "DisableExecuteApiEndpoint": "{{ DisableExecuteApiEndpoint }}",
 "DisableSchemaValidation": "{{ DisableSchemaValidation }}",
 "Name": "{{ Name }}",
 "Target": "{{ Target }}",
 "CredentialsArn": "{{ CredentialsArn }}",
 "CorsConfiguration": {
  "AllowOrigins": [
   "{{ AllowOrigins[0] }}"
  ],
  "AllowCredentials": "{{ AllowCredentials }}",
  "ExposeHeaders": [
   "{{ ExposeHeaders[0] }}"
  ],
  "AllowHeaders": [
   "{{ AllowHeaders[0] }}"
  ],
  "MaxAge": "{{ MaxAge }}",
  "AllowMethods": [
   "{{ AllowMethods[0] }}"
  ]
 },
 "Version": "{{ Version }}",
 "ProtocolType": "{{ ProtocolType }}",
 "RouteKey": "{{ RouteKey }}",
 "Body": {},
 "Tags": {},
 "ApiKeySelectionExpression": "{{ ApiKeySelectionExpression }}"
}
>>>
--required properties only
INSERT INTO aws.apigatewayv2.apis (
 RouteSelectionExpression,
 BodyS3Location,
 Description,
 BasePath,
 FailOnWarnings,
 DisableExecuteApiEndpoint,
 DisableSchemaValidation,
 Name,
 Target,
 CredentialsArn,
 CorsConfiguration,
 Version,
 ProtocolType,
 RouteKey,
 Body,
 Tags,
 ApiKeySelectionExpression,
 region
)
SELECT 
{{ RouteSelectionExpression }},
 {{ BodyS3Location }},
 {{ Description }},
 {{ BasePath }},
 {{ FailOnWarnings }},
 {{ DisableExecuteApiEndpoint }},
 {{ DisableSchemaValidation }},
 {{ Name }},
 {{ Target }},
 {{ CredentialsArn }},
 {{ CorsConfiguration }},
 {{ Version }},
 {{ ProtocolType }},
 {{ RouteKey }},
 {{ Body }},
 {{ Tags }},
 {{ ApiKeySelectionExpression }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "RouteSelectionExpression": "{{ RouteSelectionExpression }}",
 "BodyS3Location": {
  "Etag": "{{ Etag }}",
  "Bucket": "{{ Bucket }}",
  "Version": "{{ Version }}",
  "Key": "{{ Key }}"
 },
 "Description": "{{ Description }}",
 "BasePath": "{{ BasePath }}",
 "FailOnWarnings": "{{ FailOnWarnings }}",
 "DisableExecuteApiEndpoint": "{{ DisableExecuteApiEndpoint }}",
 "DisableSchemaValidation": "{{ DisableSchemaValidation }}",
 "Name": "{{ Name }}",
 "Target": "{{ Target }}",
 "CredentialsArn": "{{ CredentialsArn }}",
 "CorsConfiguration": {
  "AllowOrigins": [
   "{{ AllowOrigins[0] }}"
  ],
  "AllowCredentials": "{{ AllowCredentials }}",
  "ExposeHeaders": [
   "{{ ExposeHeaders[0] }}"
  ],
  "AllowHeaders": [
   "{{ AllowHeaders[0] }}"
  ],
  "MaxAge": "{{ MaxAge }}",
  "AllowMethods": [
   "{{ AllowMethods[0] }}"
  ]
 },
 "Version": "{{ Version }}",
 "ProtocolType": "{{ ProtocolType }}",
 "RouteKey": "{{ RouteKey }}",
 "Body": {},
 "Tags": {},
 "ApiKeySelectionExpression": "{{ ApiKeySelectionExpression }}"
}
>>>
--all properties
INSERT INTO aws.apigatewayv2.apis (
 RouteSelectionExpression,
 BodyS3Location,
 Description,
 BasePath,
 FailOnWarnings,
 DisableExecuteApiEndpoint,
 DisableSchemaValidation,
 Name,
 Target,
 CredentialsArn,
 CorsConfiguration,
 Version,
 ProtocolType,
 RouteKey,
 Body,
 Tags,
 ApiKeySelectionExpression,
 region
)
SELECT 
 {{ RouteSelectionExpression }},
 {{ BodyS3Location }},
 {{ Description }},
 {{ BasePath }},
 {{ FailOnWarnings }},
 {{ DisableExecuteApiEndpoint }},
 {{ DisableSchemaValidation }},
 {{ Name }},
 {{ Target }},
 {{ CredentialsArn }},
 {{ CorsConfiguration }},
 {{ Version }},
 {{ ProtocolType }},
 {{ RouteKey }},
 {{ Body }},
 {{ Tags }},
 {{ ApiKeySelectionExpression }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigatewayv2.apis
WHERE data__Identifier = '<ApiId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>apis</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:PUT,
s3:getObject
```

### Delete
```json
apigateway:GET,
apigateway:DELETE,
s3:getObject
```

### List
```json
apigateway:GET,
s3:getObject
```

