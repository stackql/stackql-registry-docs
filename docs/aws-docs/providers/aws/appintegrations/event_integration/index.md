---
title: event_integration
hide_title: false
hide_table_of_contents: false
keywords:
  - event_integration
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


Gets or updates an individual <code>event_integration</code> resource, use <code>event_integrations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppIntegrations::EventIntegration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.event_integration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The event integration description.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
description,
event_integration_arn,
name,
event_bridge_bus,
event_filter,
tags
FROM aws.appintegrations.event_integration
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>event_integration</code> resource, the following permissions are required:

### Read
```json
app-integrations:GetEventIntegration,
app-integrations:ListTagsForResource
```

### Update
```json
app-integrations:GetEventIntegration,
app-integrations:UpdateEventIntegration,
app-integrations:TagResource,
app-integrations:UntagResource
```

