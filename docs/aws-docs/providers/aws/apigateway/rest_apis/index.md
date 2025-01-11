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

Creates, updates, deletes or gets a <code>rest_api</code> resource or lists <code>rest_apis</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rest_apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::RestApi</code> resource creates a REST API. For more information, see &#91;restapi:create&#93;(https://docs.aws.amazon.com/apigateway/latest/api/API_CreateRestApi.html) in the *Amazon API Gateway REST API Reference*.<br />On January 1, 2016, the Swagger Specification was donated to the &#91;OpenAPI initiative&#93;(https://docs.aws.amazon.com/https://www.openapis.org/), becoming the foundation of the OpenAPI Specification.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.rest_apis" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>A policy document that contains the permissions for the <code>RestApi</code> resource. To set the ARN for the policy, use the <code>!Join</code> intrinsic function with <code>""</code> as delimiter and values of <code>"execute-api:/"</code> and <code>"*"</code>.</td></tr>
<tr><td><CopyableCode code="body_s3_location" /></td><td><code>object</code></td><td>The Amazon Simple Storage Service (Amazon S3) location that points to an OpenAPI file, which defines a set of RESTful APIs in JSON or YAML format.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="minimum_compression_size" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="clone_from" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mode" /></td><td><code>string</code></td><td>This property applies only when you use OpenAPI to define your REST API. The <code>Mode</code> determines how API Gateway handles resource updates.<br />Valid values are <code>overwrite</code> or <code>merge</code>. <br />For <code>overwrite</code>, the new API definition replaces the existing one. The existing API identifier remains unchanged.<br />For <code>merge</code>, the new API definition is merged with the existing API.<br />If you don't specify this property, a default value is chosen. For REST APIs created before March 29, 2021, the default is <code>overwrite</code>. For REST APIs created after March 29, 2021, the new API definition takes precedence, but any container types such as endpoint configurations and binary media types are merged with the existing API. <br />Use the default mode to define top-level <code>RestApi</code> properties in addition to using OpenAPI. Generally, it's preferred to use API Gateway's OpenAPI extensions to model these properties.</td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disable_execute_api_endpoint" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="fail_on_warnings" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="binary_media_types" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the RestApi. A name is required if the REST API is not based on an OpenAPI specification.</td></tr>
<tr><td><CopyableCode code="root_resource_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_key_source_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_configuration" /></td><td><code>object</code></td><td>A list of the endpoint types of the API. Use this property when creating an API. When importing an existing API, specify the endpoint configuration types using the <code>Parameters</code> property.</td></tr>
<tr><td><CopyableCode code="body" /></td><td><code>object</code></td><td>An OpenAPI specification that defines a set of RESTful APIs in JSON format. For YAML templates, you can also provide the specification in YAML format.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html"><code>AWS::ApiGateway::RestApi</code></a>.

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
Gets all <code>rest_apis</code> in a region.
```sql
SELECT
region,
policy,
body_s3_location,
description,
minimum_compression_size,
parameters,
clone_from,
mode,
rest_api_id,
disable_execute_api_endpoint,
fail_on_warnings,
binary_media_types,
name,
root_resource_id,
api_key_source_type,
endpoint_configuration,
body,
tags
FROM aws.apigateway.rest_apis
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>rest_api</code>.
```sql
SELECT
region,
policy,
body_s3_location,
description,
minimum_compression_size,
parameters,
clone_from,
mode,
rest_api_id,
disable_execute_api_endpoint,
fail_on_warnings,
binary_media_types,
name,
root_resource_id,
api_key_source_type,
endpoint_configuration,
body,
tags
FROM aws.apigateway.rest_apis
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rest_api</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.rest_apis (
 Policy,
 BodyS3Location,
 Description,
 MinimumCompressionSize,
 Parameters,
 CloneFrom,
 Mode,
 DisableExecuteApiEndpoint,
 FailOnWarnings,
 BinaryMediaTypes,
 Name,
 ApiKeySourceType,
 EndpointConfiguration,
 Body,
 Tags,
 region
)
SELECT 
'{{ Policy }}',
 '{{ BodyS3Location }}',
 '{{ Description }}',
 '{{ MinimumCompressionSize }}',
 '{{ Parameters }}',
 '{{ CloneFrom }}',
 '{{ Mode }}',
 '{{ DisableExecuteApiEndpoint }}',
 '{{ FailOnWarnings }}',
 '{{ BinaryMediaTypes }}',
 '{{ Name }}',
 '{{ ApiKeySourceType }}',
 '{{ EndpointConfiguration }}',
 '{{ Body }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.rest_apis (
 Policy,
 BodyS3Location,
 Description,
 MinimumCompressionSize,
 Parameters,
 CloneFrom,
 Mode,
 DisableExecuteApiEndpoint,
 FailOnWarnings,
 BinaryMediaTypes,
 Name,
 ApiKeySourceType,
 EndpointConfiguration,
 Body,
 Tags,
 region
)
SELECT 
 '{{ Policy }}',
 '{{ BodyS3Location }}',
 '{{ Description }}',
 '{{ MinimumCompressionSize }}',
 '{{ Parameters }}',
 '{{ CloneFrom }}',
 '{{ Mode }}',
 '{{ DisableExecuteApiEndpoint }}',
 '{{ FailOnWarnings }}',
 '{{ BinaryMediaTypes }}',
 '{{ Name }}',
 '{{ ApiKeySourceType }}',
 '{{ EndpointConfiguration }}',
 '{{ Body }}',
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
      - name: Policy
        value: {}
      - name: BodyS3Location
        value:
          Bucket: '{{ Bucket }}'
          ETag: '{{ ETag }}'
          Version: '{{ Version }}'
          Key: '{{ Key }}'
      - name: Description
        value: '{{ Description }}'
      - name: MinimumCompressionSize
        value: '{{ MinimumCompressionSize }}'
      - name: Parameters
        value: {}
      - name: CloneFrom
        value: '{{ CloneFrom }}'
      - name: Mode
        value: '{{ Mode }}'
      - name: DisableExecuteApiEndpoint
        value: '{{ DisableExecuteApiEndpoint }}'
      - name: FailOnWarnings
        value: '{{ FailOnWarnings }}'
      - name: BinaryMediaTypes
        value:
          - '{{ BinaryMediaTypes[0] }}'
      - name: Name
        value: '{{ Name }}'
      - name: ApiKeySourceType
        value: '{{ ApiKeySourceType }}'
      - name: EndpointConfiguration
        value:
          Types:
            - '{{ Types[0] }}'
          VpcEndpointIds:
            - '{{ VpcEndpointIds[0] }}'
      - name: Body
        value: {}
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.rest_apis
WHERE data__Identifier = '<RestApiId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rest_apis</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

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

### Update
```json
apigateway:GET,
apigateway:DELETE,
apigateway:PATCH,
apigateway:PUT,
apigateway:UpdateRestApiPolicy,
s3:GetObject,
iam:PassRole
```

### List
```json
apigateway:GET
```

### Delete
```json
apigateway:DELETE
```
