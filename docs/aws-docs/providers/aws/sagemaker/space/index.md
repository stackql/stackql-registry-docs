---
title: space
hide_title: false
hide_table_of_contents: false
keywords:
  - space
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>space</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>space</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>space</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.space</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SpaceArn</code></td><td><code>string</code></td><td>The space Amazon Resource Name (ARN).</td></tr>
<tr><td><code>DomainId</code></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><code>SpaceName</code></td><td><code>string</code></td><td>A name for the Space.</td></tr>
<tr><td><code>SpaceSettings</code></td><td><code>undefined</code></td><td>A collection of settings.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of tags to apply to the space.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.sagemaker.space<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;DomainId&gt;'<br/>AND data__Identifier = '&lt;SpaceName&gt;'
</pre>
