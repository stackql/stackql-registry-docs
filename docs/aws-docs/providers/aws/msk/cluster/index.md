---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
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

Gets or operates on an individual <code>cluster</code> resource, use <code>clusters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.cluster" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="broker_node_group_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="enhanced_monitoring" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kafka_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="number_of_broker_nodes" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="open_monitoring" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="current_version" /></td><td><code>string</code></td><td>The current version of the MSK cluster</td></tr>
<tr><td><CopyableCode code="client_authentication" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="configuration_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="storage_mode" /></td><td><code>string</code></td><td></td></tr>
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
broker_node_group_info,
enhanced_monitoring,
kafka_version,
number_of_broker_nodes,
encryption_info,
open_monitoring,
cluster_name,
arn,
current_version,
client_authentication,
logging_info,
tags,
configuration_info,
storage_mode
FROM aws.msk.cluster
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>cluster</code> resource, the following permissions are required:

### Update
```json
kafka:UpdateMonitoring,
kafka:UpdateClusterKafkaVersion,
kafka:UpdateClusterConfiguration,
kafka:UpdateBrokerType,
kafka:UpdateBrokerCount,
kafka:UpdateBrokerStorage,
kafka:UpdateStorage,
kafka:UpdateSecurity,
kafka:UpdateConnectivity,
kafka:DescribeCluster,
kafka:DescribeClusterOperation,
kafka:TagResource,
kafka:UntagResource,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
ec2:DescribeSecurityGroups,
iam:AttachRolePolicy,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
kms:DescribeKey,
kms:CreateGrant,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
s3:GetBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
firehose:TagDeliveryStream,
acm-pca:GetCertificateAuthorityCertificate
```

### Delete
```json
kafka:DeleteCluster,
kafka:DescribeCluster
```

### Read
```json
kafka:DescribeCluster
```

