---
title: node
hide_title: false
hide_table_of_contents: false
keywords:
  - node
  - managedblockchain
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>node</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>node</td></tr>
<tr><td><b>Id</b></td><td><code>aws.managedblockchain.node</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>NodeId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MemberId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>NetworkId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>NodeConfiguration</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.managedblockchain.node<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;NodeId&gt;'
</pre>
