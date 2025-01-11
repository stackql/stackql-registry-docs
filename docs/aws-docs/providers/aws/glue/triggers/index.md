---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - glue
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

Creates, updates, deletes or gets a <code>trigger</code> resource or lists <code>triggers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Glue::Trigger</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.triggers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of trigger that this is.</td></tr>
<tr><td><CopyableCode code="start_on_creation" /></td><td><code>boolean</code></td><td>Set to true to start SCHEDULED and CONDITIONAL triggers when created. True is not supported for ON_DEMAND triggers.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of this trigger.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td>The actions initiated by this trigger.</td></tr>
<tr><td><CopyableCode code="event_batching_condition" /></td><td><code>object</code></td><td>Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.</td></tr>
<tr><td><CopyableCode code="workflow_name" /></td><td><code>string</code></td><td>The name of the workflow associated with the trigger.</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>string</code></td><td>A cron expression used to specify the schedule.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags to use with this trigger.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the trigger.</td></tr>
<tr><td><CopyableCode code="predicate" /></td><td><code>object</code></td><td>The predicate of this trigger, which defines when it will fire.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html"><code>AWS::Glue::Trigger</code></a>.

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
    <td><CopyableCode code="Type, Actions, region" /></td>
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
Gets all <code>triggers</code> in a region.
```sql
SELECT
region,
type,
start_on_creation,
description,
actions,
event_batching_condition,
workflow_name,
schedule,
tags,
name,
predicate
FROM aws.glue.triggers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>trigger</code>.
```sql
SELECT
region,
type,
start_on_creation,
description,
actions,
event_batching_condition,
workflow_name,
schedule,
tags,
name,
predicate
FROM aws.glue.triggers
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trigger</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.glue.triggers (
 Type,
 Actions,
 region
)
SELECT 
'{{ Type }}',
 '{{ Actions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.glue.triggers (
 Type,
 StartOnCreation,
 Description,
 Actions,
 EventBatchingCondition,
 WorkflowName,
 Schedule,
 Tags,
 Name,
 Predicate,
 region
)
SELECT 
 '{{ Type }}',
 '{{ StartOnCreation }}',
 '{{ Description }}',
 '{{ Actions }}',
 '{{ EventBatchingCondition }}',
 '{{ WorkflowName }}',
 '{{ Schedule }}',
 '{{ Tags }}',
 '{{ Name }}',
 '{{ Predicate }}',
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
  - name: trigger
    props:
      - name: Type
        value: '{{ Type }}'
      - name: StartOnCreation
        value: '{{ StartOnCreation }}'
      - name: Description
        value: '{{ Description }}'
      - name: Actions
        value:
          - NotificationProperty:
              NotifyDelayAfter: '{{ NotifyDelayAfter }}'
            CrawlerName: '{{ CrawlerName }}'
            Timeout: '{{ Timeout }}'
            JobName: '{{ JobName }}'
            Arguments: {}
            SecurityConfiguration: '{{ SecurityConfiguration }}'
      - name: EventBatchingCondition
        value:
          BatchSize: '{{ BatchSize }}'
          BatchWindow: '{{ BatchWindow }}'
      - name: WorkflowName
        value: '{{ WorkflowName }}'
      - name: Schedule
        value: '{{ Schedule }}'
      - name: Tags
        value: {}
      - name: Name
        value: '{{ Name }}'
      - name: Predicate
        value:
          Logical: '{{ Logical }}'
          Conditions:
            - JobName: '{{ JobName }}'
              CrawlerName: '{{ CrawlerName }}'
              State: '{{ State }}'
              CrawlState: '{{ CrawlState }}'
              LogicalOperator: '{{ LogicalOperator }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.glue.triggers
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>triggers</code> resource, the following permissions are required:

### Create
```json
glue:CreateTrigger,
glue:GetTrigger,
glue:TagResource
```

### Read
```json
glue:GetTrigger,
glue:GetTags
```

### Update
```json
glue:UpdateTrigger,
glue:UntagResource,
glue:TagResource
```

### Delete
```json
glue:DeleteTrigger,
glue:GetTrigger
```

### List
```json
glue:ListTriggers
```
