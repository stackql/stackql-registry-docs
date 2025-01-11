---
title: influxdb_instance_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - influxdb_instance_tags
  - timestream
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

Expands all tag keys and values for <code>influxdb_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>influxdb_instance_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::InfluxDBInstance resource creates an InfluxDB instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.influxdb_instance_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td>The username for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="password" /></td><td><code>string</code></td><td>The password for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="organization" /></td><td><code>string</code></td><td>The organization for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="bucket" /></td><td><code>string</code></td><td>The bucket for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="db_instance_type" /></td><td><code>string</code></td><td>The compute instance of the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="vpc_subnet_ids" /></td><td><code>array</code></td><td>A list of EC2 subnet IDs for this InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>A list of Amazon EC2 VPC security groups to associate with this InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>Attach a public IP to the customer ENI.</td></tr>
<tr><td><CopyableCode code="db_storage_type" /></td><td><code>string</code></td><td>The storage type of the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="allocated_storage" /></td><td><code>integer</code></td><td>The allocated storage for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="db_parameter_group_identifier" /></td><td><code>string</code></td><td>The name of an existing InfluxDB parameter group.</td></tr>
<tr><td><CopyableCode code="log_delivery_configuration" /></td><td><code>object</code></td><td>Configuration for sending logs to customer account from the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Status of the InfluxDB Instance.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is associated with the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name that is associated with the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone (AZ) where the InfluxDB instance is created.</td></tr>
<tr><td><CopyableCode code="secondary_availability_zone" /></td><td><code>string</code></td><td>The Secondary Availability Zone (AZ) where the InfluxDB instance is created, if DeploymentType is set as WITH_MULTIAZ_STANDBY.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The connection endpoint for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="influx_auth_parameters_secret_arn" /></td><td><code>string</code></td><td>The Auth parameters secret Amazon Resource name (ARN) that is associated with the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The service generated unique identifier for InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="deployment_type" /></td><td><code>string</code></td><td>Deployment type of the InfluxDB Instance.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>influxdb_instances</code> in a region.
```sql
SELECT
region,
username,
password,
organization,
bucket,
db_instance_type,
vpc_subnet_ids,
vpc_security_group_ids,
publicly_accessible,
db_storage_type,
allocated_storage,
db_parameter_group_identifier,
log_delivery_configuration,
status,
arn,
name,
availability_zone,
secondary_availability_zone,
endpoint,
influx_auth_parameters_secret_arn,
id,
deployment_type,
tag_key,
tag_value
FROM aws.timestream.influxdb_instance_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>influxdb_instance_tags</code> resource, see <a href="/providers/aws/timestream/influxdb_instances/#permissions"><code>influxdb_instances</code></a>

