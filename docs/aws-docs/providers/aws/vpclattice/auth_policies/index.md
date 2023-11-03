---
title: auth_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - auth_policies
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>auth_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auth_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.vpclattice.auth_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourceIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Policy</code></td><td><code>object</code></td><td></td></tr><tr><td><code>State</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.vpclattice.auth_policies
WHERE region = 'us-east-1'
</pre>
