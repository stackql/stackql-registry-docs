---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
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
Gets an individual <code>account</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigateway.account</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Primary identifier which is manually generated.</td></tr><tr><td><code>CloudWatchRoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that has write access to CloudWatch Logs in your account.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.account
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
