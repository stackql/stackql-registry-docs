---
title: task_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - task_templates
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>task_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.connect.task_templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The identifier (arn) of the task template.</td></tr>
<tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>The identifier (arn) of the instance.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the task template.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the task template.</td></tr>
<tr><td><code>ContactFlowArn</code></td><td><code>string</code></td><td>The identifier of the contact flow.</td></tr>
<tr><td><code>Constraints</code></td><td><code>object</code></td><td>The constraints for the task template</td></tr>
<tr><td><code>Defaults</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Fields</code></td><td><code>array</code></td><td>The list of task template's fields</td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ClientToken</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.connect.task_templates
WHERE region = 'us-east-1'
</pre>
