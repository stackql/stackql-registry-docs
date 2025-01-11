---
title: gateway_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_responses
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

Creates, updates, deletes or gets a <code>gateway_response</code> resource or lists <code>gateway_responses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::GatewayResponse</code> resource creates a gateway response for your API. For more information, see &#91;API Gateway Responses&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html#api-gateway-gatewayResponse-definition) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.gateway_responses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="response_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="response_parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="response_templates" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html"><code>AWS::ApiGateway::GatewayResponse</code></a>.

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
    <td><CopyableCode code="ResponseType, RestApiId, region" /></td>
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
Gets all <code>gateway_responses</code> in a region.
```sql
SELECT
region,
id,
rest_api_id,
response_type,
status_code,
response_parameters,
response_templates
FROM aws.apigateway.gateway_responses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>gateway_response</code>.
```sql
SELECT
region,
id,
rest_api_id,
response_type,
status_code,
response_parameters,
response_templates
FROM aws.apigateway.gateway_responses
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateway_response</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.gateway_responses (
 RestApiId,
 ResponseType,
 region
)
SELECT 
'{{ RestApiId }}',
 '{{ ResponseType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.gateway_responses (
 RestApiId,
 ResponseType,
 StatusCode,
 ResponseParameters,
 ResponseTemplates,
 region
)
SELECT 
 '{{ RestApiId }}',
 '{{ ResponseType }}',
 '{{ StatusCode }}',
 '{{ ResponseParameters }}',
 '{{ ResponseTemplates }}',
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
  - name: gateway_response
    props:
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: ResponseType
        value: '{{ ResponseType }}'
      - name: StatusCode
        value: '{{ StatusCode }}'
      - name: ResponseParameters
        value: {}
      - name: ResponseTemplates
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.gateway_responses
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>gateway_responses</code> resource, the following permissions are required:

### Create
```json
apigateway:PUT,
apigateway:GET
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PUT
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
