---
title: streaming_distribution
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_distribution
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>streaming_distribution</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_distribution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>streaming_distribution</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudfront.streaming_distribution</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>streaming_distribution_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
domain_name,
streaming_distribution_config,
tags
FROM aws.cloudfront.streaming_distribution
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
