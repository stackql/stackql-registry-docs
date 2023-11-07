---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
Retrieves a list of <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.msk.clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>BrokerNodeGroupInfo</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>EnhancedMonitoring</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KafkaVersion</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>NumberOfBrokerNodes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>EncryptionInfo</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>OpenMonitoring</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ClusterName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CurrentVersion</code></td><td><code>string</code></td><td>The current version of the MSK cluster</td></tr>
<tr><td><code>ClientAuthentication</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LoggingInfo</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><code>ConfigurationInfo</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>StorageMode</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.msk.clusters
WHERE region = 'us-east-1'
</pre>
