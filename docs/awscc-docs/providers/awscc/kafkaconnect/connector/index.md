---
title: connector
hide_title: false
hide_table_of_contents: false
keywords:
  - connector
  - kafkaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>connector</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connector</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kafkaconnect.connector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>capacity</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>connector_arn</code></td><td><code>string</code></td><td>Amazon Resource Name for the created Connector.</td></tr>
<tr><td><code>connector_configuration</code></td><td><code>object</code></td><td>The configuration for the connector.</td></tr>
<tr><td><code>connector_description</code></td><td><code>string</code></td><td>A summary description of the connector.</td></tr>
<tr><td><code>connector_name</code></td><td><code>string</code></td><td>The name of the connector.</td></tr>
<tr><td><code>kafka_cluster</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kafka_cluster_client_authentication</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kafka_cluster_encryption_in_transit</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kafka_connect_version</code></td><td><code>string</code></td><td>The version of Kafka Connect. It has to be compatible with both the Kafka cluster's version and the plugins.</td></tr>
<tr><td><code>log_delivery</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>plugins</code></td><td><code>array</code></td><td>List of plugins to use with the connector.</td></tr>
<tr><td><code>service_execution_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon S3 objects and other external resources.</td></tr>
<tr><td><code>worker_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
capacity,
connector_arn,
connector_configuration,
connector_description,
connector_name,
kafka_cluster,
kafka_cluster_client_authentication,
kafka_cluster_encryption_in_transit,
kafka_connect_version,
log_delivery,
plugins,
service_execution_role_arn,
worker_configuration
FROM awscc.kafkaconnect.connector
WHERE data__Identifier = '<ConnectorArn>';
```

## Permissions

To operate on the <code>connector</code> resource, the following permissions are required:

### Read
```json
kafkaconnect:DescribeConnector
```

### Delete
```json
kafkaconnect:DeleteConnector,
kafkaconnect:DescribeConnector,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries
```

### Update
```json
kafkaconnect:UpdateConnector,
kafkaconnect:DescribeConnector,
iam:CreateServiceLinkedRole,
logs:UpdateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
firehose:TagDeliveryStream
```

