---
title: methods
hide_title: false
hide_table_of_contents: false
keywords:
  - methods
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


Used to retrieve a list of <code>methods</code> in a region or to create or delete a <code>methods</code> resource, use <code>method</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::Method`` resource creates API Gateway methods that define the parameters and body that clients must send in their requests.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.methods" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The Resource identifier for the MethodResponse resource.</td></tr>
<tr><td><CopyableCode code="http_method" /></td><td><code>string</code></td><td>The method's HTTP verb.</td></tr>
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
rest_api_id,
resource_id,
http_method
FROM aws.apigateway.methods
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
 "HttpMethod": "{{ HttpMethod }}",
 "ResourceId": "{{ ResourceId }}",
 "RestApiId": "{{ RestApiId }}"
}
>>>
--required properties only
INSERT INTO aws.apigateway.methods (
 HttpMethod,
 ResourceId,
 RestApiId,
 region
)
SELECT 
{{ .HttpMethod }},
 {{ .ResourceId }},
 {{ .RestApiId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ApiKeyRequired": "{{ ApiKeyRequired }}",
 "AuthorizationScopes": [
  "{{ AuthorizationScopes[0] }}"
 ],
 "AuthorizationType": "{{ AuthorizationType }}",
 "AuthorizerId": "{{ AuthorizerId }}",
 "HttpMethod": "{{ HttpMethod }}",
 "Integration": {
  "CacheKeyParameters": [
   "{{ CacheKeyParameters[0] }}"
  ],
  "CacheNamespace": "{{ CacheNamespace }}",
  "ConnectionId": "{{ ConnectionId }}",
  "ConnectionType": "{{ ConnectionType }}",
  "ContentHandling": "{{ ContentHandling }}",
  "Credentials": "{{ Credentials }}",
  "IntegrationHttpMethod": "{{ IntegrationHttpMethod }}",
  "IntegrationResponses": [
   {
    "ContentHandling": "{{ ContentHandling }}",
    "ResponseParameters": {},
    "ResponseTemplates": {},
    "SelectionPattern": "{{ SelectionPattern }}",
    "StatusCode": "{{ StatusCode }}"
   }
  ],
  "PassthroughBehavior": "{{ PassthroughBehavior }}",
  "RequestParameters": {},
  "RequestTemplates": {},
  "TimeoutInMillis": "{{ TimeoutInMillis }}",
  "Type": "{{ Type }}",
  "Uri": "{{ Uri }}"
 },
 "MethodResponses": [
  {
   "ResponseModels": {},
   "ResponseParameters": {},
   "StatusCode": "{{ StatusCode }}"
  }
 ],
 "OperationName": "{{ OperationName }}",
 "RequestModels": {},
 "RequestParameters": {},
 "RequestValidatorId": "{{ RequestValidatorId }}",
 "ResourceId": "{{ ResourceId }}",
 "RestApiId": "{{ RestApiId }}"
}
>>>
--all properties
INSERT INTO aws.apigateway.methods (
 ApiKeyRequired,
 AuthorizationScopes,
 AuthorizationType,
 AuthorizerId,
 HttpMethod,
 Integration,
 MethodResponses,
 OperationName,
 RequestModels,
 RequestParameters,
 RequestValidatorId,
 ResourceId,
 RestApiId,
 region
)
SELECT 
 {{ .ApiKeyRequired }},
 {{ .AuthorizationScopes }},
 {{ .AuthorizationType }},
 {{ .AuthorizerId }},
 {{ .HttpMethod }},
 {{ .Integration }},
 {{ .MethodResponses }},
 {{ .OperationName }},
 {{ .RequestModels }},
 {{ .RequestParameters }},
 {{ .RequestValidatorId }},
 {{ .ResourceId }},
 {{ .RestApiId }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigateway.methods
WHERE data__Identifier = '<RestApiId|ResourceId|HttpMethod>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>methods</code> resource, the following permissions are required:

### Create
```json
apigateway:PUT,
apigateway:GET,
iam:PassRole
```

### Delete
```json
apigateway:DELETE
```

