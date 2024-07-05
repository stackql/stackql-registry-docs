---
title: event_integrations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - event_integrations_list_only
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

Lists <code>event_integrations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/event_integrations/"><code>event_integrations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_integrations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppIntegrations::EventIntegration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.event_integrations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The event integration description.</td></tr>
<tr><td><CopyableCode code="event_integration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the event integration.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the event integration.</td></tr>
<tr><td><CopyableCode code="event_bridge_bus" /></td><td><code>string</code></td><td>The Amazon Eventbridge bus for the event integration.</td></tr>
<tr><td><CopyableCode code="event_filter" /></td><td><code>object</code></td><td>The EventFilter (source) associated with the event integration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the event integration.</td></tr>
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
Lists all <code>event_integrations</code> in a region.
```sql
SELECT
region,
name
FROM aws.appintegrations.event_integrations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_integrations_list_only</code> resource, see <a href="/providers/aws/appintegrations/event_integrations/#permissions"><code>event_integrations</code></a>


