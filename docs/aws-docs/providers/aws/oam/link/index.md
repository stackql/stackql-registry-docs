---
title: link
hide_title: false
hide_table_of_contents: false
keywords:
  - link
  - oam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>link</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.oam.link</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Label</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LabelTemplate</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResourceTypes</code></td><td><code>array</code></td><td></td></tr><tr><td><code>SinkIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>Tags to apply to the link</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.oam.link
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>
