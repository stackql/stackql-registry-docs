---
title: aggregation_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregation_authorizations
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>aggregation_authorizations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aggregation_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.aggregation_authorizations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AuthorizedAccountId</code></td><td><code>string</code></td><td>The 12-digit account ID of the account authorized to aggregate data.</td></tr><tr><td><code>AuthorizedAwsRegion</code></td><td><code>string</code></td><td>The region authorized to collect aggregated data.</td></tr><tr><td><code>AggregationAuthorizationArn</code></td><td><code>string</code></td><td>The ARN of the AggregationAuthorization.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags for the AggregationAuthorization.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.config.aggregation_authorizations
WHERE region = 'us-east-1'
</pre>
