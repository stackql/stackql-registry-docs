---
title: app_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - app_tags
  - resiliencehub
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

Expands all tag keys and values for <code>apps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::ResilienceHub::App.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resiliencehub.app_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the app.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>App description.</td></tr>
<tr><td><CopyableCode code="app_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the App.</td></tr>
<tr><td><CopyableCode code="resiliency_policy_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
<tr><td><CopyableCode code="regulatory_policy_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Regulatory Policy.</td></tr>
<tr><td><CopyableCode code="app_template_body" /></td><td><code>string</code></td><td>A string containing full ResilienceHub app template body.</td></tr>
<tr><td><CopyableCode code="resource_mappings" /></td><td><code>array</code></td><td>An array of ResourceMapping objects.</td></tr>
<tr><td><CopyableCode code="app_assessment_schedule" /></td><td><code>string</code></td><td>Assessment execution schedule.</td></tr>
<tr><td><CopyableCode code="permission_model" /></td><td><code>object</code></td><td>Defines the roles and credentials that AWS Resilience Hub would use while creating the application, importing its resources, and running an assessment.</td></tr>
<tr><td><CopyableCode code="event_subscriptions" /></td><td><code>array</code></td><td>The list of events you would like to subscribe and get notification for.</td></tr>
<tr><td><CopyableCode code="drift_status" /></td><td><code>string</code></td><td>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</td></tr>
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
Expands tags for all <code>apps</code> in a region.
```sql
SELECT
region,
name,
description,
app_arn,
resiliency_policy_arn,
regulatory_policy_arn,
app_template_body,
resource_mappings,
app_assessment_schedule,
permission_model,
event_subscriptions,
drift_status,
tag_key,
tag_value
FROM aws.resiliencehub.app_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>app_tags</code> resource, see <a href="/providers/aws/resiliencehub/apps/#permissions"><code>apps</code></a>

