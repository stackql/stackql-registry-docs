---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - synthetics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>groups</td></tr>
<tr><td><b>Id</b></td><td><code>aws.synthetics.groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the group.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Id of the group.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ResourceArns</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.synthetics.groups<br/>WHERE region = 'us-east-1'
</pre>
