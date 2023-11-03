---
title: access_point
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point
  - s3outposts
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_point</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.s3outposts.access_point</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified AccessPoint.</td></tr><tr><td><code>Bucket</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the bucket you want to associate this AccessPoint with.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>A name for the AccessPoint.</td></tr><tr><td><code>VpcConfiguration</code></td><td><code>undefined</code></td><td>Virtual Private Cloud (VPC) from which requests can be made to the AccessPoint.</td></tr><tr><td><code>Policy</code></td><td><code>object</code></td><td>The access point policy associated with this access point.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.s3outposts.access_point
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>'
</pre>
