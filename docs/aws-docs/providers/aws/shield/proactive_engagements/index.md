---
title: proactive_engagements
hide_title: false
hide_table_of_contents: false
keywords:
  - proactive_engagements
  - shield
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


Used to retrieve a list of <code>proactive_engagements</code> in a region or to create or delete a <code>proactive_engagements</code> resource, use <code>proactive_engagement</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proactive_engagements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Authorizes the Shield Response Team (SRT) to use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.proactive_engagements" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ProactiveEngagementStatus, EmergencyContactList, region" /></td>
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
account_id
FROM aws.shield.proactive_engagements
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>proactive_engagement</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.shield.proactive_engagements (
 ProactiveEngagementStatus,
 EmergencyContactList,
 region
)
SELECT 
'{{ ProactiveEngagementStatus }}',
 '{{ EmergencyContactList }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.shield.proactive_engagements (
 ProactiveEngagementStatus,
 EmergencyContactList,
 region
)
SELECT 
 '{{ ProactiveEngagementStatus }}',
 '{{ EmergencyContactList }}',
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
  - name: proactive_engagement
    props:
      - name: ProactiveEngagementStatus
        value: '{{ ProactiveEngagementStatus }}'
      - name: EmergencyContactList
        value:
          - ContactNotes: '{{ ContactNotes }}'
            EmailAddress: '{{ EmailAddress }}'
            PhoneNumber: '{{ PhoneNumber }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.shield.proactive_engagements
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>proactive_engagements</code> resource, the following permissions are required:

### Create
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings,
shield:AssociateProactiveEngagementDetails,
shield:UpdateEmergencyContactSettings,
shield:EnableProactiveEngagement
```

### Delete
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings,
shield:UpdateEmergencyContactSettings,
shield:DisableProactiveEngagement
```

### List
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings
```

