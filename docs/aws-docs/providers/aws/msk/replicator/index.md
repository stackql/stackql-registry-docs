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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>replicator</code> resource, use <code>replicators</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replicator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Replicator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.replicator" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="replicator_arn" /></td><td><code>string</code></td><td>Amazon Resource Name for the created replicator.</td></tr>
<tr><td><CopyableCode code="replicator_name" /></td><td><code>string</code></td><td>The name of the replicator.</td></tr>
<tr><td><CopyableCode code="current_version" /></td><td><code>string</code></td><td>The current version of the MSK replicator.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A summary description of the replicator.</td></tr>
<tr><td><CopyableCode code="kafka_clusters" /></td><td><code>array</code></td><td>Specifies a list of Kafka clusters which are targets of the replicator.</td></tr>
<tr><td><CopyableCode code="replication_info_list" /></td><td><code>array</code></td><td>A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.</td></tr>
<tr><td><CopyableCode code="service_execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role used by the replicator to access external resources.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.msk.replicator
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

