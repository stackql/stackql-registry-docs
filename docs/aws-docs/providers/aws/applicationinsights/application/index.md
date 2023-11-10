---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - applicationinsights
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.applicationinsights.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_group_name</code></td><td><code>string</code></td><td>The name of the resource group.</td></tr>
<tr><td><code>application_ar_n</code></td><td><code>string</code></td><td>The ARN of the ApplicationInsights application.</td></tr>
<tr><td><code>c_we_monitor_enabled</code></td><td><code>boolean</code></td><td>Indicates whether Application Insights can listen to CloudWatch events for the application resources.</td></tr>
<tr><td><code>ops_center_enabled</code></td><td><code>boolean</code></td><td>When set to true, creates opsItems for any problems detected on an application.</td></tr>
<tr><td><code>ops_item_sn_stopic_arn</code></td><td><code>string</code></td><td>The SNS topic provided to Application Insights that is associated to the created opsItem.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags of Application Insights application.</td></tr>
<tr><td><code>custom_components</code></td><td><code>array</code></td><td>The custom grouped components.</td></tr>
<tr><td><code>log_pattern_sets</code></td><td><code>array</code></td><td>The log pattern sets.</td></tr>
<tr><td><code>auto_configuration_enabled</code></td><td><code>boolean</code></td><td>If set to true, application will be configured with recommended monitoring configuration.</td></tr>
<tr><td><code>component_monitoring_settings</code></td><td><code>array</code></td><td>The monitoring settings of the components.</td></tr>
<tr><td><code>grouping_type</code></td><td><code>string</code></td><td>The grouping type of the application</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
resource_group_name,
application_ar_n,
c_we_monitor_enabled,
ops_center_enabled,
ops_item_sn_stopic_arn,
tags,
custom_components,
log_pattern_sets,
auto_configuration_enabled,
component_monitoring_settings,
grouping_type
FROM aws.applicationinsights.application
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApplicationARN&gt;'
```
