---
title: replication_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_sets
  - ssmincidents
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>replication_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ssmincidents.replication_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td>The ARN of the ReplicationSet.</td></tr>
<tr><td><code>Regions</code></td><td><code>undefined</code></td><td>The ReplicationSet configuration.</td></tr>
<tr><td><code>DeletionProtected</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags to apply to the replication set.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ssmincidents.replication_sets
WHERE region = 'us-east-1'
</pre>
