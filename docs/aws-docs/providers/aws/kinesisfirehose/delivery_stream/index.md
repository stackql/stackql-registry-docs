---
title: delivery_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_stream
  - kinesisfirehose
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>delivery_stream</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>delivery_stream</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesisfirehose.delivery_stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>delivery_stream_encryption_configuration_input</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>delivery_stream_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>delivery_stream_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>elasticsearch_destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>amazonopensearchservice_destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>amazon_open_search_serverless_destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>extended_s3_destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kinesis_stream_source_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>redshift_destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>s3_destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>splunk_destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>http_endpoint_destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
delivery_stream_encryption_configuration_input,
delivery_stream_name,
delivery_stream_type,
elasticsearch_destination_configuration,
amazonopensearchservice_destination_configuration,
amazon_open_search_serverless_destination_configuration,
extended_s3_destination_configuration,
kinesis_stream_source_configuration,
redshift_destination_configuration,
s3_destination_configuration,
splunk_destination_configuration,
http_endpoint_destination_configuration,
tags
FROM aws.kinesisfirehose.delivery_stream
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DeliveryStreamName&gt;'
```