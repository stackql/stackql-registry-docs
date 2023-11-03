---
title: replication_set
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_set
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
Gets an individual <code>replication_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssmincidents.replication_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td>The ARN of the ReplicationSet.</td></tr><tr><td><code>Regions</code></td><td><code>undefined</code></td><td>The ReplicationSet configuration.</td></tr><tr><td><code>DeletionProtected</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags to apply to the replication set.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.ssmincidents.replication_set
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
```
