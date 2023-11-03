---
title: pull_through_cache_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - pull_through_cache_rules
  - ecr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>pull_through_cache_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pull_through_cache_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ecr.pull_through_cache_rules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>EcrRepositoryPrefix</code></td><td><code>string</code></td><td>The ECRRepositoryPrefix is a custom alias for upstream registry url.</td></tr><tr><td><code>UpstreamRegistryUrl</code></td><td><code>string</code></td><td>The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ecr.pull_through_cache_rules
WHERE region = 'us-east-1'
</pre>
