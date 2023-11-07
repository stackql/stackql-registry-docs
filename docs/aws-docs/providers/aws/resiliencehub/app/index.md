---
title: app
hide_title: false
hide_table_of_contents: false
keywords:
  - app
  - resiliencehub
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>app</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app</td></tr>
<tr><td><b>Id</b></td><td><code>aws.resiliencehub.app</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the app.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>App description.</td></tr>
<tr><td><code>AppArn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the App.</td></tr>
<tr><td><code>ResiliencyPolicyArn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AppTemplateBody</code></td><td><code>string</code></td><td>A string containing full ResilienceHub app template body.</td></tr>
<tr><td><code>ResourceMappings</code></td><td><code>array</code></td><td>An array of ResourceMapping objects.</td></tr>
<tr><td><code>AppAssessmentSchedule</code></td><td><code>string</code></td><td>Assessment execution schedule.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.resiliencehub.app<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;AppArn&gt;'
</pre>
