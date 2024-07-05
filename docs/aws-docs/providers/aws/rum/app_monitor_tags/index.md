---
title: app_monitor_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - app_monitor_tags
  - rum
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

Expands all tag keys and values for <code>app_monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_monitor_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RUM::AppMonitor</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rum.app_monitor_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID of the new app monitor.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the app monitor</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The top-level internet domain name for which your application has administrative authority.</td></tr>
<tr><td><CopyableCode code="cw_log_enabled" /></td><td><code>boolean</code></td><td>Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to CWLlong in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur CWLlong charges. If you omit this parameter, the default is false</td></tr>
<tr><td><CopyableCode code="app_monitor_configuration" /></td><td><code>object</code></td><td>AppMonitor configuration</td></tr>
<tr><td><CopyableCode code="custom_events" /></td><td><code>object</code></td><td>AppMonitor custom events configuration</td></tr>
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
Expands tags for all <code>app_monitors</code> in a region.
```sql
SELECT
region,
id,
name,
domain,
cw_log_enabled,
app_monitor_configuration,
custom_events,
tag_key,
tag_value
FROM aws.rum.app_monitor_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>app_monitor_tags</code> resource, see <a href="/providers/aws/rum/app_monitors/#permissions"><code>app_monitors</code></a>


