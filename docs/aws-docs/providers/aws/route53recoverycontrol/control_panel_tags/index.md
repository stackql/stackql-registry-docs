---
title: control_panel_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - control_panel_tags
  - route53recoverycontrol
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

Expands all tag keys and values for <code>control_panels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>control_panel_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Control Control Panel resource schema .</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.control_panel_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>Cluster to associate with the Control Panel</td></tr>
<tr><td><CopyableCode code="control_panel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the control panel. You can use any non-white space character in the name.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The deployment status of control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><CopyableCode code="default_control_panel" /></td><td><code>boolean</code></td><td>A flag that Amazon Route 53 Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Route 53 Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false.</td></tr>
<tr><td><CopyableCode code="routing_control_count" /></td><td><code>integer</code></td><td>Count of associated routing controls</td></tr>
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
Expands tags for all <code>control_panels</code> in a region.
```sql
SELECT
region,
cluster_arn,
control_panel_arn,
name,
status,
default_control_panel,
routing_control_count,
tag_key,
tag_value
FROM aws.route53recoverycontrol.control_panel_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>control_panel_tags</code> resource, see <a href="/providers/aws/route53recoverycontrol/control_panels/#permissions"><code>control_panels</code></a>


