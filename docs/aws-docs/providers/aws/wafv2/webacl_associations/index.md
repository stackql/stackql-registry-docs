---
title: webacl_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - webacl_associations
  - wafv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>webacl_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webacl_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.wafv2.webacl_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourceArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>WebACLArn</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.wafv2.webacl_associations
WHERE region = 'us-east-1'
</pre>
