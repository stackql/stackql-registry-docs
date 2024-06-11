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

Creates, updates, deletes or gets an <code>api</code> resource or lists <code>apis</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::Api</code> resource creates an API. WebSocket APIs and HTTP APIs are supported. For more information about WebSocket APIs, see &#91;About WebSocket APIs in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html) in the *API Gateway Developer Guide*. For more information about HTTP APIs, see &#91;HTTP APIs&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html) in the *API Gateway Developer Guide.*</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.apis" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="route_selection_expression" /></td><td><code>string</code></td><td>The route selection expression for the API. For HTTP APIs, the <code>routeSelectionExpression</code> must be <code>$&#123;request.method&#125; $&#123;request.path&#125;</code>. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</td></tr>
<tr><td><CopyableCode code="body_s3_location" /></td><td><code>object</code></td><td>The S3 location of an OpenAPI definition. Supported only for HTTP APIs. To import an HTTP API, you must specify a <code>Body</code> or <code>BodyS3Location</code>. If you specify a <code>Body</code> or <code>BodyS3Location</code>, don't specify CloudFormation resources such as <code>AWS::ApiGatewayV2::Authorizer</code> or <code>AWS::ApiGatewayV2::Route</code>. API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the API.</td></tr>
<tr><td><CopyableCode code="api_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="base_path" /></td><td><code>string</code></td><td>Specifies how to interpret the base path of the API during import. Valid values are <code>ignore</code>, <code>prepend</code>, and <code>split</code>. The default value is <code>ignore</code>. To learn more, see &#91;Set the OpenAPI basePath Property&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html). Supported only for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="fail_on_warnings" /></td><td><code>boolean</code></td><td>Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.</td></tr>
<tr><td><CopyableCode code="disable_execute_api_endpoint" /></td><td><code>boolean</code></td><td>Specifies whether clients can invoke your API by using the default <code>execute-api</code> endpoint. By default, clients can invoke your API with the default https://&#123;api_id&#125;.execute-api.&#123;region&#125;.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</td></tr>
<tr><td><CopyableCode code="disable_schema_validation" /></td><td><code>boolean</code></td><td>Avoid validating models when creating a deployment. Supported only for WebSocket APIs.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the API. Required unless you specify an OpenAPI definition for <code>Body</code> or <code>S3BodyLocation</code>.</td></tr>
<tr><td><CopyableCode code="target" /></td><td><code>string</code></td><td>This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="credentials_arn" /></td><td><code>string</code></td><td>This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify <code>arn:aws:iam::*:user/*</code>. To use resource-based permissions on supported AWS services, specify <code>null</code>. Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="cors_configuration" /></td><td><code>object</code></td><td>A CORS configuration. Supported only for HTTP APIs. See &#91;Configuring CORS&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html) for more information.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>A version identifier for the API.</td></tr>
<tr><td><CopyableCode code="protocol_type" /></td><td><code>string</code></td><td>The API protocol. Valid values are <code>WEBSOCKET</code> or <code>HTTP</code>. Required unless you specify an OpenAPI definition for <code>Body</code> or <code>S3BodyLocation</code>.</td></tr>
<tr><td><CopyableCode code="route_key" /></td><td><code>string</code></td><td>This property is part of quick create. If you don't specify a <code>routeKey</code>, a default route of <code>$default</code> is created. The <code>$default</code> route acts as a catch-all for any request made to your API, for a particular stage. The <code>$default</code> route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="body" /></td><td><code>object</code></td><td>The OpenAPI definition. Supported only for HTTP APIs. To import an HTTP API, you must specify a <code>Body</code> or <code>BodyS3Location</code>. If you specify a <code>Body</code> or <code>BodyS3Location</code>, don't specify CloudFormation resources such as <code>AWS::ApiGatewayV2::Authorizer</code> or <code>AWS::ApiGatewayV2::Route</code>. API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><CopyableCode code="api_key_selection_expression" /></td><td><code>string</code></td><td>An API key selection expression. Supported only for WebSocket APIs. See &#91;API Key Selection Expressions&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions).</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>apis</code> in a region.
```sql
SELECT
region,
api_id
FROM aws.apigatewayv2.apis
WHERE region = 'us-east-1';
```
Gets all properties from an <code>api</code>.
```sql
SELECT
region,
route_selection_expression,
body_s3_location,
description,
api_endpoint,
base_path,
fail_on_warnings,
disable_execute_api_endpoint,
disable_schema_validation,
name,
target,
credentials_arn,
cors_configuration,
version,
protocol_type,
route_key,
api_id,
body,
tags,
api_key_selection_expression
FROM aws.apigatewayv2.apis
WHERE region = 'us-east-1' AND data__Identifier = '<ApiId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
'{{ RouteSelectionExpression }}',
 '{{ BodyS3Location }}',
 '{{ Description }}',
 '{{ BasePath }}',
 '{{ FailOnWarnings }}',
 '{{ DisableExecuteApiEndpoint }}',
 '{{ DisableSchemaValidation }}',
 '{{ Name }}',
 '{{ Target }}',
 '{{ CredentialsArn }}',
 '{{ CorsConfiguration }}',
 '{{ Version }}',
 '{{ ProtocolType }}',
 '{{ RouteKey }}',
 '{{ Body }}',
 '{{ Tags }}',
 '{{ ApiKeySelectionExpression }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ RouteSelectionExpression }}',
 '{{ BodyS3Location }}',
 '{{ Description }}',
 '{{ BasePath }}',
 '{{ FailOnWarnings }}',
 '{{ DisableExecuteApiEndpoint }}',
 '{{ DisableSchemaValidation }}',
 '{{ Name }}',
 '{{ Target }}',
 '{{ CredentialsArn }}',
 '{{ CorsConfiguration }}',
 '{{ Version }}',
 '{{ ProtocolType }}',
 '{{ RouteKey }}',
 '{{ Body }}',
 '{{ Tags }}',
 '{{ ApiKeySelectionExpression }}',
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
  - name: api
    props:
      - name: RouteSelectionExpression
        value: '{{ RouteSelectionExpression }}'
      - name: BodyS3Location
        value:
          Etag: '{{ Etag }}'
          Bucket: '{{ Bucket }}'
          Version: '{{ Version }}'
          Key: '{{ Key }}'
      - name: Description
        value: '{{ Description }}'
      - name: BasePath
        value: '{{ BasePath }}'
      - name: FailOnWarnings
        value: '{{ FailOnWarnings }}'
      - name: DisableExecuteApiEndpoint
        value: '{{ DisableExecuteApiEndpoint }}'
      - name: DisableSchemaValidation
        value: '{{ DisableSchemaValidation }}'
      - name: Name
        value: '{{ Name }}'
      - name: Target
        value: '{{ Target }}'
      - name: CredentialsArn
        value: '{{ CredentialsArn }}'
      - name: CorsConfiguration
        value:
          AllowOrigins:
            - '{{ AllowOrigins[0] }}'
          AllowCredentials: '{{ AllowCredentials }}'
          ExposeHeaders:
            - '{{ ExposeHeaders[0] }}'
          AllowHeaders:
            - '{{ AllowHeaders[0] }}'
          MaxAge: '{{ MaxAge }}'
          AllowMethods:
            - '{{ AllowMethods[0] }}'
      - name: Version
        value: '{{ Version }}'
      - name: ProtocolType
        value: '{{ ProtocolType }}'
      - name: RouteKey
        value: '{{ RouteKey }}'
      - name: Body
        value: {}
      - name: Tags
        value: {}
      - name: ApiKeySelectionExpression
        value: '{{ ApiKeySelectionExpression }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT,
apigateway:POST,
s3:getObject
```

### Read
```json
apigateway:GET,
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

