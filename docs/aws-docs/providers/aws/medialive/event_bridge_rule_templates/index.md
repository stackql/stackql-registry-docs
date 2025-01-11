---
title: event_bridge_rule_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - event_bridge_rule_templates
  - medialive
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

Creates, updates, deletes or gets an <code>event_bridge_rule_template</code> resource or lists <code>event_bridge_rule_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_bridge_rule_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::EventBridgeRuleTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.event_bridge_rule_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>An eventbridge rule template's ARN (Amazon Resource Name)</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Placeholder documentation for __timestampIso8601</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A resource's optional description.</td></tr>
<tr><td><CopyableCode code="event_targets" /></td><td><code>array</code></td><td>Placeholder documentation for __listOfEventBridgeRuleTemplateTarget</td></tr>
<tr><td><CopyableCode code="event_type" /></td><td><code>string</code></td><td>The type of event to match with the rule.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>An eventbridge rule template group's id. AWS provided template groups have ids that start with `aws-`</td></tr>
<tr><td><CopyableCode code="group_identifier" /></td><td><code>string</code></td><td>An eventbridge rule template group's identifier. Can be either be its id or current name.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>An eventbridge rule template's id. AWS provided templates have ids that start with `aws-`</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td>Placeholder documentation for __string</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td>Placeholder documentation for __timestampIso8601</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A resource's name. Names must be unique within the scope of a resource type in a specific region.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Represents the tags associated with a resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-eventbridgeruletemplate.html"><code>AWS::MediaLive::EventBridgeRuleTemplate</code></a>.

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
    <td><CopyableCode code="EventType, GroupIdentifier, Name, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>event_bridge_rule_templates</code> in a region.
```sql
SELECT
region,
arn,
created_at,
description,
event_targets,
event_type,
group_id,
group_identifier,
id,
identifier,
modified_at,
name,
tags
FROM aws.medialive.event_bridge_rule_templates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>event_bridge_rule_template</code>.
```sql
SELECT
region,
arn,
created_at,
description,
event_targets,
event_type,
group_id,
group_identifier,
id,
identifier,
modified_at,
name,
tags
FROM aws.medialive.event_bridge_rule_templates
WHERE region = 'us-east-1' AND data__Identifier = '<Identifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_bridge_rule_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.medialive.event_bridge_rule_templates (
 EventType,
 GroupIdentifier,
 Name,
 region
)
SELECT 
'{{ EventType }}',
 '{{ GroupIdentifier }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.event_bridge_rule_templates (
 Description,
 EventTargets,
 EventType,
 GroupIdentifier,
 Name,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ EventTargets }}',
 '{{ EventType }}',
 '{{ GroupIdentifier }}',
 '{{ Name }}',
 '{{ Tags }}',
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
  - name: event_bridge_rule_template
    props:
      - name: Description
        value: '{{ Description }}'
      - name: EventTargets
        value:
          - Arn: '{{ Arn }}'
      - name: EventType
        value: '{{ EventType }}'
      - name: GroupIdentifier
        value: '{{ GroupIdentifier }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.medialive.event_bridge_rule_templates
WHERE data__Identifier = '<Identifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_bridge_rule_templates</code> resource, the following permissions are required:

### Create
```json
medialive:CreateEventBridgeRuleTemplate,
medialive:GetEventBridgeRuleTemplate,
medialive:CreateTags
```

### Read
```json
medialive:GetEventBridgeRuleTemplate
```

### Update
```json
medialive:UpdateEventBridgeRuleTemplate,
medialive:GetEventBridgeRuleTemplate,
medialive:CreateTags,
medialive:DeleteTags
```

### Delete
```json
medialive:DeleteEventBridgeRuleTemplate
```

### List
```json
medialive:ListEventBridgeRuleTemplates
```
