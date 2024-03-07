---
title: observability_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - observability_configuration
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
Gets an individual <code>observability_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>observability_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>observability_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apprunner.observability_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>observability_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this ObservabilityConfiguration</td></tr>
<tr><td><code>observability_configuration_name</code></td><td><code>string</code></td><td>A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.</td></tr>
<tr><td><code>observability_configuration_revision</code></td><td><code>integer</code></td><td>The revision of this observability configuration. It's unique among all the active configurations ('Status': 'ACTIVE') that share the same ObservabilityConfigurationName.</td></tr>
<tr><td><code>latest</code></td><td><code>boolean</code></td><td>It's set to true for the configuration with the highest Revision among all configurations that share the same Name. It's set to false otherwise.</td></tr>
<tr><td><code>trace_configuration</code></td><td><code>object</code></td><td>The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>observability_configuration</code> resource, the following permissions are required:

### Read
<pre>
apprunner:DescribeObservabilityConfiguration</pre>

### Delete
<pre>
apprunner:DeleteObservabilityConfiguration</pre>


## Example
```sql
SELECT
region,
observability_configuration_arn,
observability_configuration_name,
observability_configuration_revision,
latest,
trace_configuration,
tags
FROM awscc.apprunner.observability_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ObservabilityConfigurationArn&gt;'
```
