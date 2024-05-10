---
title: rest_api
hide_title: false
hide_table_of_contents: false
keywords:
  - rest_api
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


Gets or updates an individual <code>rest_api</code> resource, use <code>rest_apis</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rest_api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::RestApi`` resource creates a REST API. For more information, see &#91;restapi:create&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;api&#x2F;API_CreateRestApi.html) in the *Amazon API Gateway REST API Reference*.&lt;br&#x2F;&gt; On January 1, 2016, the Swagger Specification was donated to the &#91;OpenAPI initiative&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;www.openapis.org&#x2F;), becoming the foundation of the OpenAPI Specification.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.rest_api" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="root_resource_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="api_key_source_type" /></td><td><code>string</code></td><td>The source of the API key for metering requests according to a usage plan. Valid values are: ``HEADER`` to read the API key from the ``X-API-Key`` header of a request. ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom authorizer.</td></tr>
<tr><td><CopyableCode code="binary_media_types" /></td><td><code>array</code></td><td>The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</td></tr>
<tr><td><CopyableCode code="body" /></td><td><code>object</code></td><td>An OpenAPI specification that defines a set of RESTful APIs in JSON format. For YAML templates, you can also provide the specification in YAML format.</td></tr>
<tr><td><CopyableCode code="body_s3_location" /></td><td><code>object</code></td><td>The Amazon Simple Storage Service (Amazon S3) location that points to an OpenAPI file, which defines a set of RESTful APIs in JSON or YAML format.</td></tr>
<tr><td><CopyableCode code="clone_from" /></td><td><code>string</code></td><td>The ID of the RestApi that you want to clone from.</td></tr>
<tr><td><CopyableCode code="endpoint_configuration" /></td><td><code>object</code></td><td>A list of the endpoint types of the API. Use this property when creating an API. When importing an existing API, specify the endpoint configuration types using the ``Parameters`` property.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the RestApi.</td></tr>
<tr><td><CopyableCode code="disable_execute_api_endpoint" /></td><td><code>boolean</code></td><td>Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint. By default, clients can invoke your API with the default ``https:&#x2F;&#x2F;&#123;api_id&#125;.execute-api.&#123;region&#125;.amazonaws.com`` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint</td></tr>
<tr><td><CopyableCode code="fail_on_warnings" /></td><td><code>boolean</code></td><td>A query parameter to indicate whether to rollback the API update (``true``) or not (``false``) when a warning is encountered. The default value is ``false``.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the RestApi. A name is required if the REST API is not based on an OpenAPI specification.</td></tr>
<tr><td><CopyableCode code="minimum_compression_size" /></td><td><code>integer</code></td><td>A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.</td></tr>
<tr><td><CopyableCode code="mode" /></td><td><code>string</code></td><td>This property applies only when you use OpenAPI to define your REST API. The ``Mode`` determines how API Gateway handles resource updates.&lt;br&#x2F;&gt; Valid values are ``overwrite`` or ``merge``. &lt;br&#x2F;&gt; For ``overwrite``, the new API definition replaces the existing one. The existing API identifier remains unchanged.&lt;br&#x2F;&gt;  For ``merge``, the new API definition is merged with the existing API.&lt;br&#x2F;&gt; If you don't specify this property, a default value is chosen. For REST APIs created before March 29, 2021, the default is ``overwrite``. For REST APIs created after March 29, 2021, the new API definition takes precedence, but any container types such as endpoint configurations and binary media types are merged with the existing API. &lt;br&#x2F;&gt; Use the default mode to define top-level ``RestApi`` properties in addition to using OpenAPI. Generally, it's preferred to use API Gateway's OpenAPI extensions to model these properties.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>A policy document that contains the permissions for the ``RestApi`` resource. To set the ARN for the policy, use the ``!Join`` intrinsic function with ``""`` as delimiter and values of ``"execute-api:&#x2F;"`` and ``"*"``.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set ``ignore=documentation`` as a ``parameters`` value, as in the AWS CLI command of ``aws apigateway import-rest-api --parameters ignore=documentation --body 'file:&#x2F;&#x2F;&#x2F;path&#x2F;to&#x2F;imported-api-body.json'``.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The key-value map of strings. The valid character set is &#91;a-zA-Z+-=._:&#x2F;&#93;. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.</td></tr>
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

## `SELECT` Example
```sql
SELECT
region,
rest_api_id,
root_resource_id,
api_key_source_type,
binary_media_types,
body,
body_s3_location,
clone_from,
endpoint_configuration,
description,
disable_execute_api_endpoint,
fail_on_warnings,
name,
minimum_compression_size,
mode,
policy,
parameters,
tags
FROM aws.apigateway.rest_api
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>';
```


## Permissions

To operate on the <code>rest_api</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
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

