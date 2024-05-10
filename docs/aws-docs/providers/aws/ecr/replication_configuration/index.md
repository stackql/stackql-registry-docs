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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>replication_configuration</code> resource, use <code>replication_configurations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ECR::ReplicationConfiguration resource configures the replication destinations for an Amazon Elastic Container Registry (Amazon Private ECR). For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;replication.html</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.replication_configuration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="replication_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="registry_id" /></td><td><code>string</code></td><td>The RegistryId associated with the aws account.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
replication_configuration,
registry_id
FROM aws.ecr.replication_configuration
WHERE region = 'us-east-1' AND data__Identifier = '<RegistryId>';
```


## Permissions

To operate on the <code>replication_configuration</code> resource, the following permissions are required:

### Read
```json
ecr:DescribeRegistry
```

### Update
```json
ecr:DescribeRegistry,
ecr:PutReplicationConfiguration,
iam:CreateServiceLinkedRole
```

