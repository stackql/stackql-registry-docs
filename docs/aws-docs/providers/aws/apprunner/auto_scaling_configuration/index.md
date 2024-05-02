---
title: auto_scaling_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_configuration
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
Gets an individual <code>auto_scaling_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes an AWS App Runner automatic configuration resource that enables automatic scaling of instances used to process web requests. You can share an auto scaling configuration across multiple services.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apprunner.auto_scaling_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_scaling_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this auto scaling configuration.</td></tr>
<tr><td><code>auto_scaling_configuration_name</code></td><td><code>string</code></td><td>The customer-provided auto scaling configuration name.  When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration. The auto scaling configuration name can be used in multiple revisions of a configuration.</td></tr>
<tr><td><code>auto_scaling_configuration_revision</code></td><td><code>integer</code></td><td>The revision of this auto scaling configuration. It's unique among all the active configurations ("Status": "ACTIVE") that share the same AutoScalingConfigurationName.</td></tr>
<tr><td><code>max_concurrency</code></td><td><code>integer</code></td><td>The maximum number of concurrent requests that an instance processes. If the number of concurrent requests exceeds this limit, App Runner scales the service up to use more instances to process the requests.</td></tr>
<tr><td><code>max_size</code></td><td><code>integer</code></td><td>The maximum number of instances that an App Runner service scales up to. At most MaxSize instances actively serve traffic for your service.</td></tr>
<tr><td><code>min_size</code></td><td><code>integer</code></td><td>The minimum number of instances that App Runner provisions for a service. The service always has at least MinSize provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.</td></tr>
<tr><td><code>latest</code></td><td><code>boolean</code></td><td>It's set to true for the configuration with the highest Revision among all configurations that share the same AutoScalingConfigurationName. It's set to false otherwise. App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of metadata items that you can associate with your auto scaling configuration resource. A tag is a key-value pair.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
auto_scaling_configuration_arn,
auto_scaling_configuration_name,
auto_scaling_configuration_revision,
max_concurrency,
max_size,
min_size,
latest,
tags
FROM aws.apprunner.auto_scaling_configuration
WHERE data__Identifier = '<AutoScalingConfigurationArn>';
```

## Permissions

To operate on the <code>auto_scaling_configuration</code> resource, the following permissions are required:

### Read
```json
apprunner:DescribeAutoScalingConfiguration
```

### Delete
```json
apprunner:DeleteAutoScalingConfiguration
```

