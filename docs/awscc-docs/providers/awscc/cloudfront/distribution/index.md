---
title: distribution
hide_title: false
hide_table_of_contents: false
keywords:
  - distribution
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
Gets an individual <code>distribution</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distribution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>distribution</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.distribution</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>distribution_config</code></td><td><code>object</code></td><td>The distribution's configuration.</td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A complex type that contains zero or more ``Tag`` elements.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>distribution</code> resource, the following permissions are required:

### Delete
<pre>
cloudfront:DeleteDistribution,
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig</pre>

### Read
<pre>
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig</pre>

### Update
<pre>
cloudfront:GetDistribution,
cloudfront:GetDistributionConfig,
cloudfront:UpdateDistribution,
cloudfront:UpdateDistributionWithStagingConfig,
cloudfront:ListTagsForResource,
cloudfront:TagResource,
cloudfront:UntagResource</pre>


## Example
```sql
SELECT
region,
distribution_config,
domain_name,
id,
tags
FROM awscc.cloudfront.distribution
WHERE data__Identifier = '&lt;Id&gt;'
```
