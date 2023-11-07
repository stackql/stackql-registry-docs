---
title: record_set_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - record_set_groups
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>record_set_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>record_set_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>record_set_groups</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.record_set_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Comment</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>HostedZoneName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RecordSets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>HostedZoneId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.route53.record_set_groups<br/>WHERE region = 'us-east-1'
</pre>
