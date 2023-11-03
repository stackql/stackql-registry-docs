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
null
<tr><td><b>Id</b></td><td><code>aws.kinesisfirehose.delivery_stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DeliveryStreamEncryptionConfigurationInput</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DeliveryStreamName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DeliveryStreamType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ElasticsearchDestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AmazonopensearchserviceDestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AmazonOpenSearchServerlessDestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ExtendedS3DestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KinesisStreamSourceConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RedshiftDestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>S3DestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SplunkDestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>HttpEndpointDestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.kinesisfirehose.delivery_stream
WHERE region = 'us-east-1' AND data__Identifier = '<DeliveryStreamName>'
</pre>
