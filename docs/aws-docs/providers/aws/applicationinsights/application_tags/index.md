---
title: application_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - application_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ApplicationInsights::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationinsights.application_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_group_name" /></td><td><code>string</code></td><td>The name of the resource group.</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the ApplicationInsights application.</td></tr>
<tr><td><CopyableCode code="cwe_monitor_enabled" /></td><td><code>boolean</code></td><td>Indicates whether Application Insights can listen to CloudWatch events for the application resources.</td></tr>
<tr><td><CopyableCode code="ops_center_enabled" /></td><td><code>boolean</code></td><td>When set to true, creates opsItems for any problems detected on an application.</td></tr>
<tr><td><CopyableCode code="ops_item_sns_topic_arn" /></td><td><code>string</code></td><td>The SNS topic provided to Application Insights that is associated to the created opsItem.</td></tr>
<tr><td><CopyableCode code="custom_components" /></td><td><code>array</code></td><td>The custom grouped components.</td></tr>
<tr><td><CopyableCode code="log_pattern_sets" /></td><td><code>array</code></td><td>The log pattern sets.</td></tr>
<tr><td><CopyableCode code="auto_configuration_enabled" /></td><td><code>boolean</code></td><td>If set to true, application will be configured with recommended monitoring configuration.</td></tr>
<tr><td><CopyableCode code="component_monitoring_settings" /></td><td><code>array</code></td><td>The monitoring settings of the components.</td></tr>
<tr><td><CopyableCode code="grouping_type" /></td><td><code>string</code></td><td>The grouping type of the application</td></tr>
<tr><td><CopyableCode code="attach_missing_permission" /></td><td><code>boolean</code></td><td>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>applications</code> in a region.
```sql
SELECT
region,
resource_group_name,
application_arn,
cwe_monitor_enabled,
ops_center_enabled,
ops_item_sns_topic_arn,
custom_components,
log_pattern_sets,
auto_configuration_enabled,
component_monitoring_settings,
grouping_type,
attach_missing_permission,
tag_key,
tag_value
FROM aws.applicationinsights.application_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>application_tags</code> resource, see <a href="/providers/aws/applicationinsights/applications/#permissions"><code>applications</code></a>


