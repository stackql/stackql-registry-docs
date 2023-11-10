---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - elasticsearch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticsearch.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>elasticsearch_cluster_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>elasticsearch_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_publishing_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>snapshot_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>v_pc_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>node_to_node_encryption_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>access_policies</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_endpoint_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cognito_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>advanced_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>advanced_security_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>e_bs_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>encryption_at_rest_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
elasticsearch_cluster_config,
domain_name,
elasticsearch_version,
log_publishing_options,
snapshot_options,
v_pc_options,
node_to_node_encryption_options,
access_policies,
domain_endpoint_options,
domain_arn,
cognito_options,
advanced_options,
advanced_security_options,
domain_endpoint,
e_bs_options,
id,
arn,
encryption_at_rest_options,
tags
FROM aws.elasticsearch.domain
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
