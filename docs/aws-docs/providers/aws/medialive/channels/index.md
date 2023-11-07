---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - medialive
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>channels</td></tr>
<tr><td><b>Id</b></td><td><code>aws.medialive.channels</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>InputAttachments</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>InputSpecification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Destinations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Vpc</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>LogLevel</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ChannelClass</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EncoderSettings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>CdiInputSpecification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Inputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.medialive.channels<br/>WHERE region = 'us-east-1'
</pre>
