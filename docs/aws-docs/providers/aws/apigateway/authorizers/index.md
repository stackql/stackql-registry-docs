---
title: authorizers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizers
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

Creates, updates, deletes or gets an <code>authorizer</code> resource or lists <code>authorizers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Authorizer</code> resource creates an authorization layer that API Gateway activates for methods that have authorization enabled. API Gateway activates the authorizer when a client calls those methods.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.authorizers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="authorizer_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td>Optional customer-defined field, used in OpenAPI imports and exports without functional impact.</td></tr>
<tr><td><CopyableCode code="authorizer_credentials" /></td><td><code>string</code></td><td>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null.</td></tr>
<tr><td><CopyableCode code="authorizer_result_ttl_in_seconds" /></td><td><code>integer</code></td><td>The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, the default value is 300. The maximum value is 3600, or 1 hour.</td></tr>
<tr><td><CopyableCode code="authorizer_uri" /></td><td><code>string</code></td><td>Specifies the authorizer's Uniform Resource Identifier (URI). For <code>TOKEN</code> or <code>REQUEST</code> authorizers, this must be a well-formed Lambda function URI, for example, <code>arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:&#123;account_id&#125;:function:&#123;lambda_function_name&#125;/invocations</code>. In general, the URI has this form <code>arn:aws:apigateway:&#123;region&#125;:lambda:path/&#123;service_api&#125;</code>, where <code>&#123;region&#125;</code> is the same as the region hosting the Lambda function, <code>path</code> indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial <code>/</code>. For Lambda functions, this is usually of the form <code>/2015-03-31/functions/&#91;FunctionARN&#93;/invocations</code>.</td></tr>
<tr><td><CopyableCode code="identity_source" /></td><td><code>string</code></td><td>The identity source for which authorization is requested. For a <code>TOKEN</code> or <code>COGNITO_USER_POOLS</code> authorizer, this is required and specifies the request header mapping expression for the custom header holding the authorization token submitted by the client. For example, if the token header name is <code>Auth</code>, the header mapping expression is <code>method.request.header.Auth</code>. For the <code>REQUEST</code> authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an <code>Auth</code> header, a <code>Name</code> query string parameter are defined as identity sources, this value is <code>method.request.header.Auth, method.request.querystring.Name</code>. These parameters will be used to derive the authorization caching key and to perform runtime validation of the <code>REQUEST</code> authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional.</td></tr>
<tr><td><CopyableCode code="identity_validation_expression" /></td><td><code>string</code></td><td>A validation expression for the incoming identity token. For <code>TOKEN</code> authorizers, this value is a regular expression. For <code>COGNITO_USER_POOLS</code> authorizers, API Gateway will match the <code>aud</code> field of the incoming token from the client against the specified regular expression. It will invoke the authorizer's Lambda function when there is a match. Otherwise, it will return a 401 Unauthorized response without calling the Lambda function. The validation expression does not apply to the <code>REQUEST</code> authorizer.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the authorizer.</td></tr>
<tr><td><CopyableCode code="provider_arns" /></td><td><code>array</code></td><td>A list of the Amazon Cognito user pool ARNs for the <code>COGNITO_USER_POOLS</code> authorizer. Each element is of this format: <code>arn:aws:cognito-idp:&#123;region&#125;:&#123;account_id&#125;:userpool/&#123;user_pool_id&#125;</code>. For a <code>TOKEN</code> or <code>REQUEST</code> authorizer, this is not defined.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The authorizer type. Valid values are <code>TOKEN</code> for a Lambda function using a single authorization token submitted in a custom header, <code>REQUEST</code> for a Lambda function using incoming request parameters, and <code>COGNITO_USER_POOLS</code> for using an Amazon Cognito user pool.</td></tr>
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
    <td><CopyableCode code="RestApiId, Type, Name, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>authorizers</code> in a region.
```sql
SELECT
region,
rest_api_id,
authorizer_id
FROM aws.apigateway.authorizers
WHERE region = 'us-east-1';
```
Gets all properties from an <code>authorizer</code>.
```sql
SELECT
region,
rest_api_id,
authorizer_id,
auth_type,
authorizer_credentials,
authorizer_result_ttl_in_seconds,
authorizer_uri,
identity_source,
identity_validation_expression,
name,
provider_arns,
type
FROM aws.apigateway.authorizers
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>|<AuthorizerId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorizer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.authorizers (
 RestApiId,
 Name,
 Type,
 region
)
SELECT 
'{{ RestApiId }}',
 '{{ Name }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.authorizers (
 RestApiId,
 AuthType,
 AuthorizerCredentials,
 AuthorizerResultTtlInSeconds,
 AuthorizerUri,
 IdentitySource,
 IdentityValidationExpression,
 Name,
 ProviderARNs,
 Type,
 region
)
SELECT 
 '{{ RestApiId }}',
 '{{ AuthType }}',
 '{{ AuthorizerCredentials }}',
 '{{ AuthorizerResultTtlInSeconds }}',
 '{{ AuthorizerUri }}',
 '{{ IdentitySource }}',
 '{{ IdentityValidationExpression }}',
 '{{ Name }}',
 '{{ ProviderARNs }}',
 '{{ Type }}',
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
  - name: authorizer
    props:
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: AuthType
        value: '{{ AuthType }}'
      - name: AuthorizerCredentials
        value: '{{ AuthorizerCredentials }}'
      - name: AuthorizerResultTtlInSeconds
        value: '{{ AuthorizerResultTtlInSeconds }}'
      - name: AuthorizerUri
        value: '{{ AuthorizerUri }}'
      - name: IdentitySource
        value: '{{ IdentitySource }}'
      - name: IdentityValidationExpression
        value: '{{ IdentityValidationExpression }}'
      - name: Name
        value: '{{ Name }}'
      - name: ProviderARNs
        value:
          - '{{ ProviderARNs[0] }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.authorizers
WHERE data__Identifier = '<RestApiId|AuthorizerId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>authorizers</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
iam:PassRole
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH,
iam:PassRole
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```

