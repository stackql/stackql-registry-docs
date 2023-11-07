---
title: security_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - security_keys
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
Retrieves a list of <code>security_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>security_keys</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.security_keys</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstanceId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AssociationId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.connect.security_keys<br/>WHERE region = 'us-east-1'
</pre>
