---
title: app_blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - app_blocks
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>app_blocks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app_blocks</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.app_blocks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DisplayName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SourceS3Location</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SetupScriptDetails</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>CreatedTime</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appstream.app_blocks<br/>WHERE region = 'us-east-1'
</pre>
