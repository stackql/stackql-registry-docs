---
title: tracker_consumers
hide_title: false
hide_table_of_contents: false
keywords:
  - tracker_consumers
  - location
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>tracker_consumers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracker_consumers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tracker_consumers</td></tr>
<tr><td><b>Id</b></td><td><code>aws.location.tracker_consumers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ConsumerArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TrackerName</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.location.tracker_consumers
WHERE region = 'us-east-1'
</pre>
