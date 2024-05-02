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
Gets or operates on an individual <code>replication_set</code> resource, use <code>replication_sets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ReplicationSet</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssmincidents.replication_set</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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

