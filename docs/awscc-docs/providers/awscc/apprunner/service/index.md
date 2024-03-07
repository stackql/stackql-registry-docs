---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
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
Gets an individual <code>service</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apprunner.service</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>service_name</code></td><td><code>string</code></td><td>The AppRunner Service Name.</td></tr>
<tr><td><code>service_id</code></td><td><code>string</code></td><td>The AppRunner Service Id</td></tr>
<tr><td><code>service_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AppRunner Service.</td></tr>
<tr><td><code>service_url</code></td><td><code>string</code></td><td>The Service Url of the AppRunner Service.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>AppRunner Service status.</td></tr>
<tr><td><code>source_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>instance_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>health_check_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>observability_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>auto_scaling_configuration_arn</code></td><td><code>string</code></td><td>Autoscaling configuration ARN</td></tr>
<tr><td><code>network_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>service</code> resource, the following permissions are required:

### Read
<pre>
apprunner:DescribeService</pre>

### Update
<pre>
apprunner:UpdateService,
iam:PassRole</pre>

### Delete
<pre>
apprunner:DeleteService</pre>


## Example
```sql
SELECT
region,
service_name,
service_id,
service_arn,
service_url,
status,
source_configuration,
instance_configuration,
tags,
encryption_configuration,
health_check_configuration,
observability_configuration,
auto_scaling_configuration_arn,
network_configuration
FROM awscc.apprunner.service
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ServiceArn&gt;'
```
