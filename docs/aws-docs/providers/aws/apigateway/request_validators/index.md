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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>request_validator</code> resource or lists <code>request_validators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>request_validators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::RequestValidator</code> resource sets up basic validation rules for incoming requests to your API. For more information, see &#91;Enable Basic Request Validation for an API in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.request_validators" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="request_validator_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="validate_request_body" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="validate_request_parameters" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html"><code>AWS::ApiGateway::RequestValidator</code></a>.

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
    <td><CopyableCode code="RestApiId, region" /></td>
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
Gets all <code>request_validators</code> in a region.
```sql
SELECT
region,
request_validator_id,
name,
rest_api_id,
validate_request_body,
validate_request_parameters
FROM aws.apigateway.request_validators
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>request_validator</code>.
```sql
SELECT
region,
request_validator_id,
name,
rest_api_id,
validate_request_body,
validate_request_parameters
FROM aws.apigateway.request_validators
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>|<RequestValidatorId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>request_validator</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.request_validators (
 RestApiId,
 region
)
SELECT 
'{{ RestApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.request_validators (
 Name,
 RestApiId,
 ValidateRequestBody,
 ValidateRequestParameters,
 region
)
SELECT 
 '{{ Name }}',
 '{{ RestApiId }}',
 '{{ ValidateRequestBody }}',
 '{{ ValidateRequestParameters }}',
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
  - name: request_validator
    props:
      - name: Name
        value: '{{ Name }}'
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: ValidateRequestBody
        value: '{{ ValidateRequestBody }}'
      - name: ValidateRequestParameters
        value: '{{ ValidateRequestParameters }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.request_validators
WHERE data__Identifier = '<RestApiId|RequestValidatorId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>request_validators</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET
```

### Update
```json
apigateway:PATCH,
apigateway:GET
```

### Delete
```json
apigateway:DELETE
```

### Read
```json
apigateway:GET
```

### List
```json
apigateway:GET
```
