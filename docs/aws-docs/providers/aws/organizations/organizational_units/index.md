---
title: organizational_units
hide_title: false
hide_table_of_contents: false
keywords:
  - organizational_units
  - organizations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>organizational_units</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizational_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.organizations.organizational_units</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this OU.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>The unique identifier (ID) associated with this OU.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The friendly name of this OU.</td></tr><tr><td><code>ParentId</code></td><td><code>string</code></td><td>The unique identifier (ID) of the parent root or OU that you want to create the new OU in.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of tags that you want to attach to the newly created OU.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.organizations.organizational_units
WHERE region = 'us-east-1'
</pre>
