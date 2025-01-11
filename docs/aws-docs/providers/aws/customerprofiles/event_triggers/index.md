---
title: event_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - event_triggers
  - customerprofiles
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

Creates, updates, deletes or gets an <code>event_trigger</code> resource or lists <code>event_triggers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An event trigger resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.event_triggers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="event_trigger_name" /></td><td><code>string</code></td><td>The unique name of the event trigger.</td></tr>
<tr><td><CopyableCode code="object_type_name" /></td><td><code>string</code></td><td>The unique name of the object type.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the event trigger.</td></tr>
<tr><td><CopyableCode code="event_trigger_conditions" /></td><td><code>array</code></td><td>A list of conditions that determine when an event should trigger the destination.</td></tr>
<tr><td><CopyableCode code="event_trigger_limits" /></td><td><code>object</code></td><td>Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.</td></tr>
<tr><td><CopyableCode code="segment_filter" /></td><td><code>string</code></td><td>The destination is triggered only for profiles that meet the criteria of a segment definition.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the event trigger was created.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The timestamp of when the event trigger was most recently updated.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html"><code>AWS::CustomerProfiles::EventTrigger</code></a>.

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
    <td><CopyableCode code="DomainName, EventTriggerName, ObjectTypeName, EventTriggerConditions, region" /></td>
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
Gets all <code>event_triggers</code> in a region.
```sql
SELECT
region,
domain_name,
event_trigger_name,
object_type_name,
description,
event_trigger_conditions,
event_trigger_limits,
segment_filter,
created_at,
last_updated_at,
tags
FROM aws.customerprofiles.event_triggers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>event_trigger</code>.
```sql
SELECT
region,
domain_name,
event_trigger_name,
object_type_name,
description,
event_trigger_conditions,
event_trigger_limits,
segment_filter,
created_at,
last_updated_at,
tags
FROM aws.customerprofiles.event_triggers
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>|<EventTriggerName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_trigger</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.customerprofiles.event_triggers (
 DomainName,
 EventTriggerName,
 ObjectTypeName,
 EventTriggerConditions,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ EventTriggerName }}',
 '{{ ObjectTypeName }}',
 '{{ EventTriggerConditions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.customerprofiles.event_triggers (
 DomainName,
 EventTriggerName,
 ObjectTypeName,
 Description,
 EventTriggerConditions,
 EventTriggerLimits,
 SegmentFilter,
 Tags,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ EventTriggerName }}',
 '{{ ObjectTypeName }}',
 '{{ Description }}',
 '{{ EventTriggerConditions }}',
 '{{ EventTriggerLimits }}',
 '{{ SegmentFilter }}',
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
  - name: event_trigger
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: EventTriggerName
        value: '{{ EventTriggerName }}'
      - name: ObjectTypeName
        value: '{{ ObjectTypeName }}'
      - name: Description
        value: '{{ Description }}'
      - name: EventTriggerConditions
        value:
          - EventTriggerDimensions:
              - ObjectAttributes:
                  - Source: '{{ Source }}'
                    FieldName: '{{ FieldName }}'
                    ComparisonOperator: '{{ ComparisonOperator }}'
                    Values:
                      - '{{ Values[0] }}'
            LogicalOperator: '{{ LogicalOperator }}'
      - name: EventTriggerLimits
        value:
          EventExpiration: '{{ EventExpiration }}'
          Periods:
            - Unit: '{{ Unit }}'
              Value: '{{ Value }}'
              MaxInvocationsPerProfile: '{{ MaxInvocationsPerProfile }}'
              Unlimited: '{{ Unlimited }}'
      - name: SegmentFilter
        value: '{{ SegmentFilter }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.customerprofiles.event_triggers
WHERE data__Identifier = '<DomainName|EventTriggerName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_triggers</code> resource, the following permissions are required:

### Create
```json
profile:CreateEventTrigger,
profile:TagResource
```

### Read
```json
profile:GetEventTrigger
```

### Update
```json
profile:GetEventTrigger,
profile:UpdateEventTrigger,
profile:UntagResource,
profile:TagResource
```

### Delete
```json
profile:DeleteEventTrigger
```

### List
```json
profile:ListEventTriggers
```
