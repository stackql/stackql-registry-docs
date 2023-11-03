---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - apprunner
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apprunner.services</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ServiceName</code></td><td><code>string</code></td><td>The AppRunner Service Name.</td></tr><tr><td><code>ServiceId</code></td><td><code>string</code></td><td>The AppRunner Service Id</td></tr><tr><td><code>ServiceArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AppRunner Service.</td></tr><tr><td><code>ServiceUrl</code></td><td><code>string</code></td><td>The Service Url of the AppRunner Service.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>AppRunner Service status.</td></tr><tr><td><code>SourceConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>InstanceConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>EncryptionConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>HealthCheckConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ObservabilityConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AutoScalingConfigurationArn</code></td><td><code>string</code></td><td>Autoscaling configuration ARN</td></tr><tr><td><code>NetworkConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apprunner.services
WHERE region = 'us-east-1'
</pre>
