---
title: notification_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rules
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

Creates, updates, deletes or gets a <code>notification_rule</code> resource or lists <code>notification_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeStarNotifications::NotificationRule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarnotifications.notification_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="event_type_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="EventTypeIds, Resource, DetailType, Targets, Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>notification_rules</code> in a region.
```sql
SELECT
region,
arn
FROM aws.codestarnotifications.notification_rules
WHERE region = 'us-east-1';
```
Gets all properties from a <code>notification_rule</code>.
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
FROM aws.codestarnotifications.notification_rules
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.codestarnotifications.notification_rules (
 EventTypeIds,
 DetailType,
 Resource,
 Targets,
 Name,
 region
)
SELECT 
'{{ EventTypeIds }}',
 '{{ DetailType }}',
 '{{ Resource }}',
 '{{ Targets }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.codestarnotifications.notification_rules (
 EventTypeId,
 CreatedBy,
 TargetAddress,
 EventTypeIds,
 Status,
 DetailType,
 Resource,
 Targets,
 Tags,
 Name,
 region
)
SELECT 
 '{{ EventTypeId }}',
 '{{ CreatedBy }}',
 '{{ TargetAddress }}',
 '{{ EventTypeIds }}',
 '{{ Status }}',
 '{{ DetailType }}',
 '{{ Resource }}',
 '{{ Targets }}',
 '{{ Tags }}',
 '{{ Name }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: notification_rule
    props:
      - name: EventTypeId
        value: '{{ EventTypeId }}'
      - name: CreatedBy
        value: '{{ CreatedBy }}'
      - name: TargetAddress
        value: '{{ TargetAddress }}'
      - name: EventTypeIds
        value:
          - '{{ EventTypeIds[0] }}'
      - name: Status
        value: '{{ Status }}'
      - name: DetailType
        value: '{{ DetailType }}'
      - name: Resource
        value: '{{ Resource }}'
      - name: Targets
        value:
          - TargetType: '{{ TargetType }}'
            TargetAddress: '{{ TargetAddress }}'
      - name: Tags
        value: {}
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.codestarnotifications.notification_rules
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>notification_rules</code> resource, the following permissions are required:

### Create
```json
codestar-notifications:createNotificationRule
```

### List
```json
codestar-notifications:listNotificationRules
```

### Read
```json
codestar-notifications:describeNotificationRule
```

### Delete
```json
codestar-notifications:deleteNotificationRule,
codestar-notifications:describeNotificationRule
```

### Update
```json
codestar-notifications:updateNotificationRule,
codestar-notifications:TagResource,
codestar-notifications:UntagResource
```

