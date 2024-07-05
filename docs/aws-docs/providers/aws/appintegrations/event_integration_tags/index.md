---
title: event_integration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - event_integration_tags
  - appintegrations
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

Expands all tag keys and values for <code>event_integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_integration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppIntegrations::EventIntegration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.event_integration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The event integration description.</td></tr>
<tr><td><CopyableCode code="event_integration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the event integration.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the event integration.</td></tr>
<tr><td><CopyableCode code="event_bridge_bus" /></td><td><code>string</code></td><td>The Amazon Eventbridge bus for the event integration.</td></tr>
<tr><td><CopyableCode code="event_filter" /></td><td><code>object</code></td><td>The EventFilter (source) associated with the event integration.</td></tr>
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
Expands tags for all <code>event_integrations</code> in a region.
```sql
SELECT
region,
description,
event_integration_arn,
name,
event_bridge_bus,
event_filter,
tag_key,
tag_value
FROM aws.appintegrations.event_integration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_integration_tags</code> resource, see <a href="/providers/aws/appintegrations/event_integrations/#permissions"><code>event_integrations</code></a>

