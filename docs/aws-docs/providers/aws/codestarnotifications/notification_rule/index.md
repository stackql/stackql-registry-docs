---
title: notification_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rule
  - codestarnotifications
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


Gets or updates an individual <code>notification_rule</code> resource, use <code>notification_rules</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeStarNotifications::NotificationRule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarnotifications.notification_rule" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="event_type_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_address" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="event_type_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="detail_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
event_type_id,
created_by,
target_address,
event_type_ids,
status,
detail_type,
resource,
targets,
tags,
name,
arn
FROM aws.codestarnotifications.notification_rule
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>notification_rule</code> resource, the following permissions are required:

### Read
```json
codestar-notifications:describeNotificationRule
```

### Update
```json
codestar-notifications:updateNotificationRule,
codestar-notifications:TagResource,
codestar-notifications:UntagResource
```

