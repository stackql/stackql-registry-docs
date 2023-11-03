---
title: deployment
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment
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
Gets an individual <code>deployment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigateway.deployment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DeploymentId</code></td><td><code>string</code></td><td>Primary Id for this resource</td></tr><tr><td><code>DeploymentCanarySettings</code></td><td><code>undefined</code></td><td>Specifies settings for the canary deployment.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the purpose of the API Gateway deployment.</td></tr><tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The ID of the RestApi resource to deploy. </td></tr><tr><td><code>StageDescription</code></td><td><code>undefined</code></td><td>Configures the stage that API Gateway creates with this deployment.</td></tr><tr><td><code>StageName</code></td><td><code>string</code></td><td>A name for the stage that API Gateway creates with this deployment. Use only alphanumeric characters.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.deployment
WHERE region = 'us-east-1' AND data__Identifier = '<DeploymentId>' AND data__Identifier = '<RestApiId>'
</pre>
