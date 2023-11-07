---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - codedeploy
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codedeploy.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ApplicationName</code></td><td><code>string</code></td><td>A name for the application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name.</td></tr>
<tr><td><code>ComputePlatform</code></td><td><code>string</code></td><td>The compute platform that CodeDeploy deploys the application to.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define. </td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.codedeploy.application<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ApplicationName&gt;'
</pre>
