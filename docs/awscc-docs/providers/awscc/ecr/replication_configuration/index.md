---
title: replication_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_configuration
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
Gets an individual <code>replication_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replication_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ecr.replication_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>replication_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>registry_id</code></td><td><code>string</code></td><td>The RegistryId associated with the aws account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>replication_configuration</code> resource, the following permissions are required:

### Read
<pre>
ecr:DescribeRegistry</pre>

### Update
<pre>
ecr:DescribeRegistry,
ecr:PutReplicationConfiguration,
iam:CreateServiceLinkedRole</pre>

### Delete
<pre>
ecr:DescribeRegistry,
ecr:PutReplicationConfiguration,
iam:CreateServiceLinkedRole</pre>


## Example
```sql
SELECT
region,
replication_configuration,
registry_id
FROM awscc.ecr.replication_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RegistryId&gt;'
```
