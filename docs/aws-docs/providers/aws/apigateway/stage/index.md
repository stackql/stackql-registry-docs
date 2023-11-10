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
<tr><td><b>Id</b></td><td><code>aws.apigateway.stage</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_log_setting</code></td><td><code>object</code></td><td>Specifies settings for logging access in this stage.</td></tr>
<tr><td><code>cache_cluster_enabled</code></td><td><code>boolean</code></td><td>Indicates whether cache clustering is enabled for the stage.</td></tr>
<tr><td><code>cache_cluster_size</code></td><td><code>string</code></td><td>The stage's cache cluster size.</td></tr>
<tr><td><code>canary_setting</code></td><td><code>object</code></td><td>Specifies settings for the canary deployment in this stage.</td></tr>
<tr><td><code>client_certificate_id</code></td><td><code>string</code></td><td>The ID of the client certificate that API Gateway uses to call your integration endpoints in the stage. </td></tr>
<tr><td><code>deployment_id</code></td><td><code>string</code></td><td>The ID of the deployment that the stage is associated with. This parameter is required to create a stage. </td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the stage.</td></tr>
<tr><td><code>documentation_version</code></td><td><code>string</code></td><td>The version ID of the API documentation snapshot.</td></tr>
<tr><td><code>method_settings</code></td><td><code>array</code></td><td>Settings for all methods in the stage.</td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The ID of the RestApi resource that you're deploying with this stage.</td></tr>
<tr><td><code>stage_name</code></td><td><code>string</code></td><td>The name of the stage, which API Gateway uses as the first path segment in the invoked Uniform Resource Identifier (URI).</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of arbitrary tags (key-value pairs) to associate with the stage.</td></tr>
<tr><td><code>tracing_enabled</code></td><td><code>boolean</code></td><td>Specifies whether active X-Ray tracing is enabled for this stage.</td></tr>
<tr><td><code>variables</code></td><td><code>object</code></td><td>A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value.</td></tr>
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
FROM aws.apigateway.stage
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RestApiId&gt;'
AND data__Identifier = '&lt;StageName&gt;'
```
