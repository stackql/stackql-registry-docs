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

Creates, updates, deletes or gets a <code>method</code> resource or lists <code>methods</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Method</code> resource creates API Gateway methods that define the parameters and body that clients must send in their requests.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.methods" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="integration" /></td><td><code>object</code></td><td>Represents an <code>HTTP</code>, <code>HTTP_PROXY</code>, <code>AWS</code>, <code>AWS_PROXY</code>, or Mock integration.</td></tr>
<tr><td><CopyableCode code="operation_name" /></td><td><code>string</code></td><td>A human-friendly operation identifier for the method. For example, you can assign the <code>operationName</code> of <code>ListPets</code> for the <code>GET /pets</code> method in the <code>PetStore</code> example.</td></tr>
<tr><td><CopyableCode code="request_models" /></td><td><code>object</code></td><td>A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).</td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="authorization_scopes" /></td><td><code>array</code></td><td>A list of authorization scopes configured on the method. The scopes are used with a <code>COGNITO_USER_POOLS</code> authorizer to authorize the method invocation. The authorization works by matching the method scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any method scopes matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the method scope is configured, the client must provide an access token instead of an identity token for authorization purposes.</td></tr>
<tr><td><CopyableCode code="request_validator_id" /></td><td><code>string</code></td><td>The identifier of a RequestValidator for request validation.</td></tr>
<tr><td><CopyableCode code="request_parameters" /></td><td><code>object</code></td><td>A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of <code>method.request.&#123;location&#125;.&#123;name&#125;</code>, where <code>location</code> is <code>querystring</code>, <code>path</code>, or <code>header</code> and <code>name</code> is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (<code>true</code>) or optional (<code>false</code>). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or templates.</td></tr>
<tr><td><CopyableCode code="method_responses" /></td><td><code>array</code></td><td>Gets a method response associated with a given HTTP status code.</td></tr>
<tr><td><CopyableCode code="authorizer_id" /></td><td><code>string</code></td><td>The identifier of an authorizer to use on this method. The method's authorization type must be <code>CUSTOM</code> or <code>COGNITO_USER_POOLS</code>.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The Resource identifier for the MethodResponse resource.</td></tr>
<tr><td><CopyableCode code="api_key_required" /></td><td><code>boolean</code></td><td>A boolean flag specifying whether a valid ApiKey is required to invoke this method.</td></tr>
<tr><td><CopyableCode code="authorization_type" /></td><td><code>string</code></td><td>The method's authorization type. This parameter is required. For valid values, see &#91;Method&#93;(https://docs.aws.amazon.com/apigateway/latest/api/API_Method.html) in the *API Gateway API Reference*.<br />If you specify the <code>AuthorizerId</code> property, specify <code>CUSTOM</code> or <code>COGNITO_USER_POOLS</code> for this property.</td></tr>
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
    <td><CopyableCode code="RestApiId, ResourceId, HttpMethod, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>method</code>.
```sql
SELECT
region,
integration,
operation_name,
request_models,
rest_api_id,
authorization_scopes,
request_validator_id,
request_parameters,
method_responses,
authorizer_id,
resource_id,
api_key_required,
authorization_type,
http_method
FROM aws.apigateway.methods
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>|<ResourceId>|<HttpMethod>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>method</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.apigateway.methods (
 RestApiId,
 ResourceId,
 HttpMethod,
 region
)
SELECT 
'{{ RestApiId }}',
 '{{ ResourceId }}',
 '{{ HttpMethod }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.methods (
 Integration,
 OperationName,
 RequestModels,
 RestApiId,
 AuthorizationScopes,
 RequestValidatorId,
 RequestParameters,
 MethodResponses,
 AuthorizerId,
 ResourceId,
 ApiKeyRequired,
 AuthorizationType,
 HttpMethod,
 region
)
SELECT 
 '{{ Integration }}',
 '{{ OperationName }}',
 '{{ RequestModels }}',
 '{{ RestApiId }}',
 '{{ AuthorizationScopes }}',
 '{{ RequestValidatorId }}',
 '{{ RequestParameters }}',
 '{{ MethodResponses }}',
 '{{ AuthorizerId }}',
 '{{ ResourceId }}',
 '{{ ApiKeyRequired }}',
 '{{ AuthorizationType }}',
 '{{ HttpMethod }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: method
    props:
      - name: Integration
        value:
          CacheNamespace: '{{ CacheNamespace }}'
          ConnectionType: '{{ ConnectionType }}'
          IntegrationResponses:
            - ResponseTemplates: {}
              SelectionPattern: '{{ SelectionPattern }}'
              ContentHandling: '{{ ContentHandling }}'
              ResponseParameters: {}
              StatusCode: '{{ StatusCode }}'
          IntegrationHttpMethod: '{{ IntegrationHttpMethod }}'
          Uri: '{{ Uri }}'
          PassthroughBehavior: '{{ PassthroughBehavior }}'
          RequestParameters: {}
          ConnectionId: '{{ ConnectionId }}'
          Type: '{{ Type }}'
          CacheKeyParameters:
            - '{{ CacheKeyParameters[0] }}'
          ContentHandling: '{{ ContentHandling }}'
          RequestTemplates: {}
          TimeoutInMillis: '{{ TimeoutInMillis }}'
          Credentials: '{{ Credentials }}'
      - name: OperationName
        value: '{{ OperationName }}'
      - name: RequestModels
        value: {}
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: AuthorizationScopes
        value:
          - '{{ AuthorizationScopes[0] }}'
      - name: RequestValidatorId
        value: '{{ RequestValidatorId }}'
      - name: RequestParameters
        value: {}
      - name: MethodResponses
        value:
          - ResponseParameters: {}
            StatusCode: '{{ StatusCode }}'
            ResponseModels: {}
      - name: AuthorizerId
        value: '{{ AuthorizerId }}'
      - name: ResourceId
        value: '{{ ResourceId }}'
      - name: ApiKeyRequired
        value: '{{ ApiKeyRequired }}'
      - name: AuthorizationType
        value: '{{ AuthorizationType }}'
      - name: HttpMethod
        value: '{{ HttpMethod }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.methods
WHERE data__Identifier = '<RestApiId|ResourceId|HttpMethod>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>methods</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Create
```json
apigateway:PUT,
apigateway:GET,
iam:PassRole
```

### Update
```json
apigateway:GET,
apigateway:DELETE,
apigateway:PUT,
iam:PassRole
```

### Delete
```json
apigateway:DELETE
```

