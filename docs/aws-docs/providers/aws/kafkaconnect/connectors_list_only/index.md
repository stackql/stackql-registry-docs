---
title: connectors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>connectors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/connectors/"><code>connectors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::KafkaConnect::Connector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.connectors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="capacity" /></td><td><code>object</code></td><td>Information about the capacity allocated to the connector.</td></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td>Amazon Resource Name for the created Connector.</td></tr>
<tr><td><CopyableCode code="connector_configuration" /></td><td><code>object</code></td><td>The configuration for the connector.</td></tr>
<tr><td><CopyableCode code="connector_description" /></td><td><code>string</code></td><td>A summary description of the connector.</td></tr>
<tr><td><CopyableCode code="connector_name" /></td><td><code>string</code></td><td>The name of the connector.</td></tr>
<tr><td><CopyableCode code="kafka_cluster" /></td><td><code>object</code></td><td>Details of how to connect to the Kafka cluster.</td></tr>
<tr><td><CopyableCode code="kafka_cluster_client_authentication" /></td><td><code>object</code></td><td>Details of the client authentication used by the Kafka cluster.</td></tr>
<tr><td><CopyableCode code="kafka_cluster_encryption_in_transit" /></td><td><code>object</code></td><td>Details of encryption in transit to the Kafka cluster.</td></tr>
<tr><td><CopyableCode code="kafka_connect_version" /></td><td><code>string</code></td><td>The version of Kafka Connect. It has to be compatible with both the Kafka cluster's version and the plugins.</td></tr>
<tr><td><CopyableCode code="log_delivery" /></td><td><code>object</code></td><td>Details of what logs are delivered and where they are delivered.</td></tr>
<tr><td><CopyableCode code="plugins" /></td><td><code>array</code></td><td>List of plugins to use with the connector.</td></tr>
<tr><td><CopyableCode code="service_execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon S3 objects and other external resources.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><CopyableCode code="worker_configuration" /></td><td><code>object</code></td><td>The configuration of the workers, which are the processes that run the connector logic.</td></tr>
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
Lists all <code>connectors</code> in a region.
```sql
SELECT
region,
connector_arn
FROM aws.kafkaconnect.connectors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>connectors_list_only</code> resource, see <a href="/providers/aws/kafkaconnect/connectors/#permissions"><code>connectors</code></a>


