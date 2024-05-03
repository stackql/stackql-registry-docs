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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>replication_set</code> resource, use <code>replication_sets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ReplicationSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmincidents.replication_set" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the ReplicationSet.</td></tr>
<tr><td><CopyableCode code="regions" /></td><td><code>array</code></td><td>The ReplicationSet configuration.</td></tr>
<tr><td><CopyableCode code="deletion_protected" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to apply to the replication set.</td></tr>
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
arn,
regions,
deletion_protected,
tags
FROM aws.ssmincidents.replication_set
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>replication_set</code> resource, the following permissions are required:

### Read
```json
ssm-incidents:ListReplicationSets,
ssm-incidents:GetReplicationSet,
ssm-incidents:ListTagsForResource
```

### Update
```json
ssm-incidents:UpdateReplicationSet,
ssm-incidents:UpdateDeletionProtection,
ssm-incidents:GetReplicationSet,
ssm-incidents:TagResource,
ssm-incidents:UntagResource,
ssm-incidents:ListTagsForResource
```

### Delete
```json
ssm-incidents:DeleteReplicationSet,
ssm-incidents:GetReplicationSet
```

