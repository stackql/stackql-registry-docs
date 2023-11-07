---
title: index
hide_title: false
hide_table_of_contents: false
keywords:
  - index
  - kendra
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>index</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>index</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>index</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kendra.index</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description for the index</td></tr>
<tr><td><code>ServerSideEncryptionConfiguration</code></td><td><code>object</code></td><td>Server side encryption configuration</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags for labeling the index</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Edition</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DocumentMetadataConfigurations</code></td><td><code>array</code></td><td>Document metadata configurations</td></tr>
<tr><td><code>CapacityUnits</code></td><td><code>object</code></td><td>Capacity units</td></tr>
<tr><td><code>UserContextPolicy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>UserTokenConfigurations</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.kendra.index<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
