---
title: fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet
  - iotfleetwise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fleet</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotfleetwise.fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LastModificationTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SignalCatalogArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iotfleetwise.fleet<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
