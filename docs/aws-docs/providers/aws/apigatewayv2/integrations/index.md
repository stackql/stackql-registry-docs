---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
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

Creates, updates, deletes or gets an <code>integration</code> resource or lists <code>integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The API identifier.</td></tr>
<tr><td><CopyableCode code="connection_id" /></td><td><code>string</code></td><td>The ID of the VPC link for a private integration. Supported only for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="connection_type" /></td><td><code>string</code></td><td>The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.</td></tr>
<tr><td><CopyableCode code="content_handling_strategy" /></td><td><code>string</code></td><td>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT.</td></tr>
<tr><td><CopyableCode code="credentials_arn" /></td><td><code>string</code></td><td>Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, don't specify this parameter.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the integration.</td></tr>
<tr><td><CopyableCode code="integration_method" /></td><td><code>string</code></td><td>Specifies the integration's HTTP method type.</td></tr>
<tr><td><CopyableCode code="integration_subtype" /></td><td><code>string</code></td><td>Supported only for HTTP API AWS_PROXY integrations. Specifies the AWS service action to invoke.</td></tr>
<tr><td><CopyableCode code="integration_id" /></td><td><code>string</code></td><td>The integration ID.</td></tr>
<tr><td><CopyableCode code="integration_type" /></td><td><code>string</code></td><td>The integration type of an integration.</td></tr>
<tr><td><CopyableCode code="integration_uri" /></td><td><code>string</code></td><td>For a Lambda integration, specify the URI of a Lambda function. For an HTTP integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.</td></tr>
<tr><td><CopyableCode code="passthrough_behavior" /></td><td><code>string</code></td><td>Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.</td></tr>
<tr><td><CopyableCode code="payload_format_version" /></td><td><code>string</code></td><td>Specifies the format of the payload sent to an integration. Required for HTTP APIs. For HTTP APIs, supported values for Lambda proxy integrations are 1.0 and 2.0 For all other integrations, 1.0 is the only supported value.</td></tr>
<tr><td><CopyableCode code="request_parameters" /></td><td><code>object</code></td><td>A key-value map specifying parameters.</td></tr>
<tr><td><CopyableCode code="request_templates" /></td><td><code>object</code></td><td>A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client.</td></tr>
<tr><td><CopyableCode code="response_parameters" /></td><td><code>object</code></td><td>Parameters that transform the HTTP response from a backend integration before returning the response to clients. Supported only for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="template_selection_expression" /></td><td><code>string</code></td><td>The template selection expression for the integration. Supported only for WebSocket APIs.</td></tr>
<tr><td><CopyableCode code="timeout_in_millis" /></td><td><code>integer</code></td><td>Custom timeout between 50 and 29000 milliseconds for WebSocket APIs and between 50 and 30000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="tls_config" /></td><td><code>object</code></td><td>The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html"><code>AWS::ApiGatewayV2::Integration</code></a>.

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
    <td><CopyableCode code="ApiId, IntegrationType, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>integrations</code> in a region.
```sql
SELECT
region,
api_id,
connection_id,
connection_type,
content_handling_strategy,
credentials_arn,
description,
integration_method,
integration_subtype,
integration_id,
integration_type,
integration_uri,
passthrough_behavior,
payload_format_version,
request_parameters,
request_templates,
response_parameters,
template_selection_expression,
timeout_in_millis,
tls_config
FROM aws.apigatewayv2.integrations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>integration</code>.
```sql
SELECT
region,
api_id,
connection_id,
connection_type,
content_handling_strategy,
credentials_arn,
description,
integration_method,
integration_subtype,
integration_id,
integration_type,
integration_uri,
passthrough_behavior,
payload_format_version,
request_parameters,
request_templates,
response_parameters,
template_selection_expression,
timeout_in_millis,
tls_config
FROM aws.apigatewayv2.integrations
WHERE region = 'us-east-1' AND data__Identifier = '<ApiId>|<IntegrationId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigatewayv2.integrations (
 ApiId,
 IntegrationType,
 region
)
SELECT 
'{{ ApiId }}',
 '{{ IntegrationType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigatewayv2.integrations (
 ApiId,
 ConnectionId,
 ConnectionType,
 ContentHandlingStrategy,
 CredentialsArn,
 Description,
 IntegrationMethod,
 IntegrationSubtype,
 IntegrationType,
 IntegrationUri,
 PassthroughBehavior,
 PayloadFormatVersion,
 RequestParameters,
 RequestTemplates,
 ResponseParameters,
 TemplateSelectionExpression,
 TimeoutInMillis,
 TlsConfig,
 region
)
SELECT 
 '{{ ApiId }}',
 '{{ ConnectionId }}',
 '{{ ConnectionType }}',
 '{{ ContentHandlingStrategy }}',
 '{{ CredentialsArn }}',
 '{{ Description }}',
 '{{ IntegrationMethod }}',
 '{{ IntegrationSubtype }}',
 '{{ IntegrationType }}',
 '{{ IntegrationUri }}',
 '{{ PassthroughBehavior }}',
 '{{ PayloadFormatVersion }}',
 '{{ RequestParameters }}',
 '{{ RequestTemplates }}',
 '{{ ResponseParameters }}',
 '{{ TemplateSelectionExpression }}',
 '{{ TimeoutInMillis }}',
 '{{ TlsConfig }}',
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
  - name: integration
    props:
      - name: ApiId
        value: '{{ ApiId }}'
      - name: ConnectionId
        value: '{{ ConnectionId }}'
      - name: ConnectionType
        value: '{{ ConnectionType }}'
      - name: ContentHandlingStrategy
        value: '{{ ContentHandlingStrategy }}'
      - name: CredentialsArn
        value: '{{ CredentialsArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: IntegrationMethod
        value: '{{ IntegrationMethod }}'
      - name: IntegrationSubtype
        value: '{{ IntegrationSubtype }}'
      - name: IntegrationType
        value: '{{ IntegrationType }}'
      - name: IntegrationUri
        value: '{{ IntegrationUri }}'
      - name: PassthroughBehavior
        value: '{{ PassthroughBehavior }}'
      - name: PayloadFormatVersion
        value: '{{ PayloadFormatVersion }}'
      - name: RequestParameters
        value: {}
      - name: RequestTemplates
        value: {}
      - name: ResponseParameters
        value: {}
      - name: TemplateSelectionExpression
        value: '{{ TemplateSelectionExpression }}'
      - name: TimeoutInMillis
        value: '{{ TimeoutInMillis }}'
      - name: TlsConfig
        value:
          ServerNameToVerify: '{{ ServerNameToVerify }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigatewayv2.integrations
WHERE data__Identifier = '<ApiId|IntegrationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>integrations</code> resource, the following permissions are required:

### Create
```json
apigateway:POST
```

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT
```

### Read
```json
apigateway:GET
```

### Delete
```json
apigateway:GET,
apigateway:DELETE
```

### List
```json
apigateway:GET
```
