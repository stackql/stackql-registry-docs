---
title: location_s3
hide_title: false
hide_table_of_contents: false
keywords:
  - location_s3
  - datasync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>location_s3</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_s3</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location_s3</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datasync.location_s3</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>S3Config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>S3BucketArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon S3 bucket.</td></tr>
<tr><td><code>Subdirectory</code></td><td><code>string</code></td><td>A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.</td></tr>
<tr><td><code>S3StorageClass</code></td><td><code>string</code></td><td>The Amazon S3 storage class you want to store your files in when this location is used as a task destination.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>LocationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon S3 bucket location.</td></tr>
<tr><td><code>LocationUri</code></td><td><code>string</code></td><td>The URL of the S3 location that was described.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.datasync.location_s3<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;LocationArn&gt;'
</pre>
