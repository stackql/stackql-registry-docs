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
null
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.stage</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DeploymentId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AutoDeploy</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>RouteSettings</code></td><td><code>object</code></td><td></td></tr><tr><td><code>StageName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>StageVariables</code></td><td><code>object</code></td><td></td></tr><tr><td><code>AccessPolicyId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ClientCertificateId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AccessLogSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DefaultRouteSettings</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigatewayv2.stage
WHERE region = 'us-east-1' AND data__Identifier = '<Id>'
</pre>
