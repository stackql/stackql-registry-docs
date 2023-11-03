---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
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
Retrieves a list of <code>buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.s3outposts.buckets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified bucket.</td></tr><tr><td><code>BucketName</code></td><td><code>string</code></td><td>A name for the bucket.</td></tr><tr><td><code>OutpostId</code></td><td><code>string</code></td><td>The id of the customer outpost on which the bucket resides.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this S3Outposts bucket.</td></tr><tr><td><code>LifecycleConfiguration</code></td><td><code>undefined</code></td><td>Rules that define how Amazon S3Outposts manages objects during their lifetime.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.s3outposts.buckets
WHERE region = 'us-east-1'
</pre>
