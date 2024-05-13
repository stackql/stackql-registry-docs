---
title: stage
hide_title: false
hide_table_of_contents: false
keywords:
  - stage
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


Gets or updates an individual <code>stage</code> resource, use <code>stages</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Stage</code> resource creates a stage for a deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.stage" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_log_setting" /></td><td><code>object</code></td><td>Access log settings, including the access log format and access log destination ARN.</td></tr>
<tr><td><CopyableCode code="cache_cluster_enabled" /></td><td><code>boolean</code></td><td>Specifies whether a cache cluster is enabled for the stage.</td></tr>
<tr><td><CopyableCode code="cache_cluster_size" /></td><td><code>string</code></td><td>The stage's cache capacity in GB. For more information about choosing a cache size, see &#91;Enabling API caching to enhance responsiveness&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;api-gateway-caching.html).</td></tr>
<tr><td><CopyableCode code="canary_setting" /></td><td><code>object</code></td><td>Settings for the canary deployment in this stage.</td></tr>
<tr><td><CopyableCode code="client_certificate_id" /></td><td><code>string</code></td><td>The identifier of a client certificate for an API stage.</td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td>The identifier of the Deployment that the stage points to.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The stage's description.</td></tr>
<tr><td><CopyableCode code="documentation_version" /></td><td><code>string</code></td><td>The version of the associated API documentation.</td></tr>
<tr><td><CopyableCode code="method_settings" /></td><td><code>array</code></td><td>A map that defines the method settings for a Stage resource. Keys (designated as <code>&#x2F;&#123;method_setting_key</code> below) are method paths defined as <code>&#123;resource_path&#125;&#x2F;&#123;http_method&#125;</code> for an individual method override, or <code>&#x2F;\*&#x2F;\*</code> for overriding all methods in the stage.</td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="stage_name" /></td><td><code>string</code></td><td>The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><CopyableCode code="tracing_enabled" /></td><td><code>boolean</code></td><td>Specifies whether active tracing with X-ray is enabled for the Stage.</td></tr>
<tr><td><CopyableCode code="variables" /></td><td><code>object</code></td><td>A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: <code>&#91;A-Za-z0-9-._~:&#x2F;?#&=,&#93;+</code>.</td></tr>
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
access_log_setting,
cache_cluster_enabled,
cache_cluster_size,
canary_setting,
client_certificate_id,
deployment_id,
description,
documentation_version,
method_settings,
rest_api_id,
stage_name,
tags,
tracing_enabled,
variables
FROM aws.apigateway.stage
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>|<StageName>';
```


## Permissions

To operate on the <code>stage</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH,
apigateway:PUT,
apigateway:DELETE
```

