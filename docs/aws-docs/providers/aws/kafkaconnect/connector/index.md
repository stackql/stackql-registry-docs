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
<tr><td><b>Id</b></td><td><code>aws.kafkaconnect.connector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Capacity</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ConnectorArn</code></td><td><code>string</code></td><td>Amazon Resource Name for the created Connector.</td></tr>
<tr><td><code>ConnectorConfiguration</code></td><td><code>object</code></td><td>The configuration for the connector.</td></tr>
<tr><td><code>ConnectorDescription</code></td><td><code>string</code></td><td>A summary description of the connector.</td></tr>
<tr><td><code>ConnectorName</code></td><td><code>string</code></td><td>The name of the connector.</td></tr>
<tr><td><code>KafkaCluster</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>KafkaClusterClientAuthentication</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>KafkaClusterEncryptionInTransit</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>KafkaConnectVersion</code></td><td><code>string</code></td><td>The version of Kafka Connect. It has to be compatible with both the Kafka cluster's version and the plugins.</td></tr>
<tr><td><code>LogDelivery</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Plugins</code></td><td><code>array</code></td><td>List of plugins to use with the connector.</td></tr>
<tr><td><code>ServiceExecutionRoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon S3 objects and other external resources.</td></tr>
<tr><td><code>WorkerConfiguration</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.kafkaconnect.connector<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ConnectorArn&gt;'
</pre>
