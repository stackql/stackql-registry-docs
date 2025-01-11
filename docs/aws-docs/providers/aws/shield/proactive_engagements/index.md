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

Creates, updates, deletes or gets a <code>proactive_engagement</code> resource or lists <code>proactive_engagements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proactive_engagements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Authorizes the Shield Response Team (SRT) to use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.proactive_engagements" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="proactive_engagement_status" /></td><td><code>string</code></td><td>If `ENABLED`, the Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.<br />If `DISABLED`, the SRT will not proactively notify contacts about escalations or to initiate proactive customer support.</td></tr>
<tr><td><CopyableCode code="emergency_contact_list" /></td><td><code>array</code></td><td>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support.<br />To enable proactive engagement, the contact list must include at least one phone number.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-proactiveengagement.html"><code>AWS::Shield::ProactiveEngagement</code></a>.

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
Gets all <code>proactive_engagements</code> in a region.
```sql
SELECT
region,
account_id,
proactive_engagement_status,
emergency_contact_list
FROM aws.shield.proactive_engagements
;
```
Gets all properties from an individual <code>proactive_engagement</code>.
```sql
SELECT
region,
account_id,
proactive_engagement_status,
emergency_contact_list
FROM aws.shield.proactive_engagements
WHERE data__Identifier = '<AccountId>';
```

## `INSERT` example

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

## `DELETE` example

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

### Read
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings
```

### Update
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings,
shield:UpdateEmergencyContactSettings,
shield:EnableProactiveEngagement,
shield:DisableProactiveEngagement
```

### List
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings
```
