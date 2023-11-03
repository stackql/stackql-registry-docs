---
title: access_log_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - access_log_subscription
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
Gets an individual <code>access_log_subscription</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_log_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.vpclattice.access_log_subscription</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DestinationArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResourceArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResourceId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResourceIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.vpclattice.access_log_subscription
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>'
</pre>
