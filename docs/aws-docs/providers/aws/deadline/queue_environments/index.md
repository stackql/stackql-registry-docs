---
title: queue_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_environments
  - deadline
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


Used to retrieve a list of <code>queue_environments</code> in a region or to create or delete a <code>queue_environments</code> resource, use <code>queue_environment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::QueueEnvironment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.queue_environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="queue_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="queue_environment_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
farm_id,
queue_id,
queue_environment_id
FROM aws.deadline.queue_environments
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "FarmId": "{{ FarmId }}",
 "Priority": "{{ Priority }}",
 "QueueId": "{{ QueueId }}",
 "Template": "{{ Template }}",
 "TemplateType": "{{ TemplateType }}"
}
>>>
--required properties only
INSERT INTO aws.deadline.queue_environments (
 FarmId,
 Priority,
 QueueId,
 Template,
 TemplateType,
 region
)
SELECT 
{{ .FarmId }},
 {{ .Priority }},
 {{ .QueueId }},
 {{ .Template }},
 {{ .TemplateType }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FarmId": "{{ FarmId }}",
 "Priority": "{{ Priority }}",
 "QueueId": "{{ QueueId }}",
 "Template": "{{ Template }}",
 "TemplateType": "{{ TemplateType }}"
}
>>>
--all properties
INSERT INTO aws.deadline.queue_environments (
 FarmId,
 Priority,
 QueueId,
 Template,
 TemplateType,
 region
)
SELECT 
 {{ .FarmId }},
 {{ .Priority }},
 {{ .QueueId }},
 {{ .Template }},
 {{ .TemplateType }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.deadline.queue_environments
WHERE data__Identifier = '<FarmId|QueueId|QueueEnvironmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>queue_environments</code> resource, the following permissions are required:

### Create
```json
deadline:CreateQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

### Delete
```json
deadline:DeleteQueueEnvironment,
deadline:GetQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

### List
```json
deadline:ListQueueEnvironments,
identitystore:ListGroupMembershipsForMember
```

