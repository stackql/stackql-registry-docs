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
Gets an individual <code>stage</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stage</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.stage</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_log_setting</code></td><td><code>object</code></td><td>Access log settings, including the access log format and access log destination ARN.</td></tr>
<tr><td><code>cache_cluster_enabled</code></td><td><code>boolean</code></td><td>Specifies whether a cache cluster is enabled for the stage.</td></tr>
<tr><td><code>cache_cluster_size</code></td><td><code>string</code></td><td>The stage's cache capacity in GB. For more information about choosing a cache size, see &#91;Enabling API caching to enhance responsiveness&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;api-gateway-caching.html).</td></tr>
<tr><td><code>canary_setting</code></td><td><code>object</code></td><td>Settings for the canary deployment in this stage.</td></tr>
<tr><td><code>client_certificate_id</code></td><td><code>string</code></td><td>The identifier of a client certificate for an API stage.</td></tr>
<tr><td><code>deployment_id</code></td><td><code>string</code></td><td>The identifier of the Deployment that the stage points to.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The stage's description.</td></tr>
<tr><td><code>documentation_version</code></td><td><code>string</code></td><td>The version of the associated API documentation.</td></tr>
<tr><td><code>method_settings</code></td><td><code>array</code></td><td>A map that defines the method settings for a Stage resource. Keys (designated as ``&#x2F;&#123;method_setting_key`` below) are method paths defined as ``&#123;resource_path&#125;&#x2F;&#123;http_method&#125;`` for an individual method override, or ``&#x2F;\*&#x2F;\*`` for overriding all methods in the stage.</td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>stage_name</code></td><td><code>string</code></td><td>The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><code>tracing_enabled</code></td><td><code>boolean</code></td><td>Specifies whether active tracing with X-ray is enabled for the Stage.</td></tr>
<tr><td><code>variables</code></td><td><code>object</code></td><td>A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: ``&#91;A-Za-z0-9-._~:&#x2F;?#&=,&#93;+``.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.apigateway.stage
WHERE data__Identifier = '<RestApiId>|<StageName>';
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

### Delete
```json
apigateway:DELETE
```

