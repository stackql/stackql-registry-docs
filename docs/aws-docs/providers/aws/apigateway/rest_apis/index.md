---
title: rest_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - rest_apis
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


Used to retrieve a list of <code>rest_apis</code> in a region or to create or delete a <code>rest_apis</code> resource, use <code>rest_api</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rest_apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::RestApi`` resource creates a REST API. For more information, see &#91;restapi:create&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;api&#x2F;API_CreateRestApi.html) in the *Amazon API Gateway REST API Reference*.&lt;br&#x2F;&gt; On January 1, 2016, the Swagger Specification was donated to the &#91;OpenAPI initiative&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;www.openapis.org&#x2F;), becoming the foundation of the OpenAPI Specification.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.rest_apis" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
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
rest_api_id
FROM aws.apigateway.rest_apis
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>rest_api</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- rest_api.iql (required properties only)
INSERT INTO aws.apigateway.rest_apis (
 ApiKeySourceType,
 BinaryMediaTypes,
 Body,
 BodyS3Location,
 CloneFrom,
 EndpointConfiguration,
 Description,
 DisableExecuteApiEndpoint,
 FailOnWarnings,
 Name,
 MinimumCompressionSize,
 Mode,
 Policy,
 Parameters,
 Tags,
 region
)
SELECT 
'{{ ApiKeySourceType }}',
 '{{ BinaryMediaTypes }}',
 '{{ Body }}',
 '{{ BodyS3Location }}',
 '{{ CloneFrom }}',
 '{{ EndpointConfiguration }}',
 '{{ Description }}',
 '{{ DisableExecuteApiEndpoint }}',
 '{{ FailOnWarnings }}',
 '{{ Name }}',
 '{{ MinimumCompressionSize }}',
 '{{ Mode }}',
 '{{ Policy }}',
 '{{ Parameters }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- rest_api.iql (all properties)
INSERT INTO aws.apigateway.rest_apis (
 ApiKeySourceType,
 BinaryMediaTypes,
 Body,
 BodyS3Location,
 CloneFrom,
 EndpointConfiguration,
 Description,
 DisableExecuteApiEndpoint,
 FailOnWarnings,
 Name,
 MinimumCompressionSize,
 Mode,
 Policy,
 Parameters,
 Tags,
 region
)
SELECT 
 '{{ ApiKeySourceType }}',
 '{{ BinaryMediaTypes }}',
 '{{ Body }}',
 '{{ BodyS3Location }}',
 '{{ CloneFrom }}',
 '{{ EndpointConfiguration }}',
 '{{ Description }}',
 '{{ DisableExecuteApiEndpoint }}',
 '{{ FailOnWarnings }}',
 '{{ Name }}',
 '{{ MinimumCompressionSize }}',
 '{{ Mode }}',
 '{{ Policy }}',
 '{{ Parameters }}',
 '{{ Tags }}',
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
  - name: rest_api
    props:
      - name: ApiKeySourceType
        value: '{{ ApiKeySourceType }}'
      - name: BinaryMediaTypes
        value:
          - '{{ BinaryMediaTypes[0] }}'
      - name: Body
        value: {}
      - name: BodyS3Location
        value:
          Bucket: '{{ Bucket }}'
          ETag: '{{ ETag }}'
          Version: '{{ Version }}'
          Key: '{{ Key }}'
      - name: CloneFrom
        value: '{{ CloneFrom }}'
      - name: EndpointConfiguration
        value:
          Types:
            - '{{ Types[0] }}'
          VpcEndpointIds:
            - '{{ VpcEndpointIds[0] }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisableExecuteApiEndpoint
        value: '{{ DisableExecuteApiEndpoint }}'
      - name: FailOnWarnings
        value: '{{ FailOnWarnings }}'
      - name: Name
        value: '{{ Name }}'
      - name: MinimumCompressionSize
        value: '{{ MinimumCompressionSize }}'
      - name: Mode
        value: '{{ Mode }}'
      - name: Policy
        value: {}
      - name: Parameters
        value: {}
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apigateway.rest_apis
WHERE data__Identifier = '<RestApiId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rest_apis</code> resource, the following permissions are required:

### Create
```json
apigateway:GET,
apigateway:POST,
apigateway:PUT,
apigateway:PATCH,
apigateway:UpdateRestApiPolicy,
s3:GetObject,
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

