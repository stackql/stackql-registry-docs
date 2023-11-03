---
title: instance_group_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_config
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>instance_group_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_group_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.emr.instance_group_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>JobFlowId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AutoScalingPolicy</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>BidPrice</code></td><td><code>string</code></td><td></td></tr><tr><td><code>InstanceCount</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>EbsConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>InstanceRole</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CustomAmiId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Configurations</code></td><td><code>array</code></td><td></td></tr><tr><td><code>InstanceType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Market</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.emr.instance_group_config
WHERE region = 'us-east-1' AND data__Identifier = '<Id>'
</pre>
