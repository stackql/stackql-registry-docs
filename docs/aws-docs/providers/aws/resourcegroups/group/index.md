---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - resourcegroups
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.resourcegroups.group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the resource group</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the resource group</td></tr>
<tr><td><code>ResourceQuery</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Resource Group ARN.</td></tr>
<tr><td><code>Configuration</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Resources</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.resourcegroups.group<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Name&gt;'
</pre>
