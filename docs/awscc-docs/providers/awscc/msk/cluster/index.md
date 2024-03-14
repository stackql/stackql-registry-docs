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
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.msk.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>broker_node_group_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>enhanced_monitoring</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kafka_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>number_of_broker_nodes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>encryption_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>open_monitoring</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>current_version</code></td><td><code>string</code></td><td>The current version of the MSK cluster</td></tr>
<tr><td><code>client_authentication</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>logging_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><code>configuration_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>storage_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.msk.cluster
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

