---
title: replicator
hide_title: false
hide_table_of_contents: false
keywords:
  - replicator
  - msk
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>replicator</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replicator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replicator</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.msk.replicator</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>replicator_arn</code></td><td><code>string</code></td><td>Amazon Resource Name for the created replicator.</td></tr>
<tr><td><code>replicator_name</code></td><td><code>string</code></td><td>The name of the replicator.</td></tr>
<tr><td><code>current_version</code></td><td><code>string</code></td><td>The current version of the MSK replicator.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A summary description of the replicator.</td></tr>
<tr><td><code>kafka_clusters</code></td><td><code>array</code></td><td>Specifies a list of Kafka clusters which are targets of the replicator.</td></tr>
<tr><td><code>replication_info_list</code></td><td><code>array</code></td><td>A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.</td></tr>
<tr><td><code>service_execution_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role used by the replicator to access external resources.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
replicator_arn,
replicator_name,
current_version,
description,
kafka_clusters,
replication_info_list,
service_execution_role_arn,
tags
FROM awscc.msk.replicator
WHERE data__Identifier = '<ReplicatorArn>';
```

## Permissions

To operate on the <code>replicator</code> resource, the following permissions are required:

### Read
```json
kafka:DescribeReplicator,
kafka:ListTagsForResource
```

### Update
```json
kafka:DescribeReplicator,
kafka:ListTagsForResource,
kafka:TagResource,
kafka:UntagResource,
kafka:UpdateReplicationInfo
```

### Delete
```json
kafka:DeleteReplicator,
kafka:DescribeReplicator,
kafka:ListTagsForResource,
kafka:UntagResource
```

