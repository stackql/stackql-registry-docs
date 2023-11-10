---
title: stage
hide_title: false
hide_table_of_contents: false
keywords:
  - stage
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
Gets an individual <code>stage</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stage</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.stage</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>deployment_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_deploy</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>route_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>stage_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stage_variables</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>access_policy_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_certificate_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>access_log_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_route_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
deployment_id,
description,
auto_deploy,
route_settings,
stage_name,
stage_variables,
access_policy_id,
client_certificate_id,
access_log_settings,
id,
api_id,
default_route_settings,
tags
FROM aws.apigatewayv2.stage
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
