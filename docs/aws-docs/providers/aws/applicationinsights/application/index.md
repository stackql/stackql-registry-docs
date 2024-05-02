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
<tr><td><b>Description</b></td><td>Resource schema for AWS::ApplicationInsights::Application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.applicationinsights.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_group_name</code></td><td><code>string</code></td><td>The name of the resource group.</td></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td>The ARN of the ApplicationInsights application.</td></tr>
<tr><td><code>cwe_monitor_enabled</code></td><td><code>boolean</code></td><td>Indicates whether Application Insights can listen to CloudWatch events for the application resources.</td></tr>
<tr><td><code>ops_center_enabled</code></td><td><code>boolean</code></td><td>When set to true, creates opsItems for any problems detected on an application.</td></tr>
<tr><td><code>ops_item_sns_topic_arn</code></td><td><code>string</code></td><td>The SNS topic provided to Application Insights that is associated to the created opsItem.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags of Application Insights application.</td></tr>
<tr><td><code>custom_components</code></td><td><code>array</code></td><td>The custom grouped components.</td></tr>
<tr><td><code>log_pattern_sets</code></td><td><code>array</code></td><td>The log pattern sets.</td></tr>
<tr><td><code>auto_configuration_enabled</code></td><td><code>boolean</code></td><td>If set to true, application will be configured with recommended monitoring configuration.</td></tr>
<tr><td><code>component_monitoring_settings</code></td><td><code>array</code></td><td>The monitoring settings of the components.</td></tr>
<tr><td><code>grouping_type</code></td><td><code>string</code></td><td>The grouping type of the application</td></tr>
<tr><td><code>attach_missing_permission</code></td><td><code>boolean</code></td><td>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
resource_group_name,
application_arn,
cwe_monitor_enabled,
ops_center_enabled,
ops_item_sns_topic_arn,
tags,
custom_components,
log_pattern_sets,
auto_configuration_enabled,
component_monitoring_settings,
grouping_type,
attach_missing_permission
FROM aws.applicationinsights.application
WHERE data__Identifier = '<ApplicationARN>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
*
```

### Update
```json
*
```

### Delete
```json
*
```

