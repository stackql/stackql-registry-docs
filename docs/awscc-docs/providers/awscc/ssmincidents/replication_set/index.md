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
<tr><td><b>Description</b></td><td>replication_set</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssmincidents.replication_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the ReplicationSet.</td></tr>
<tr><td><code>regions</code></td><td><code>array</code></td><td>The ReplicationSet configuration.</td></tr>
<tr><td><code>deletion_protected</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to apply to the replication set.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>replication_set</code> resource, the following permissions are required:

### Read
<pre>
ssm-incidents:ListReplicationSets,
ssm-incidents:GetReplicationSet,
ssm-incidents:ListTagsForResource</pre>

### Update
<pre>
ssm-incidents:UpdateReplicationSet,
ssm-incidents:UpdateDeletionProtection,
ssm-incidents:GetReplicationSet,
ssm-incidents:TagResource,
ssm-incidents:UntagResource,
ssm-incidents:ListTagsForResource</pre>

### Delete
<pre>
ssm-incidents:DeleteReplicationSet,
ssm-incidents:GetReplicationSet</pre>


## Example
```sql
SELECT
region,
arn,
regions,
deletion_protected,
tags
FROM awscc.ssmincidents.replication_set
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
