---
title: autoshift_observer_notification_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - autoshift_observer_notification_statuses
  - arczonalshift
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

Creates, updates, deletes or gets an <code>autoshift_observer_notification_status</code> resource or lists <code>autoshift_observer_notification_statuses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autoshift_observer_notification_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ARCZonalShift::AutoshiftObserverNotificationStatus Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.arczonalshift.autoshift_observer_notification_statuses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>object</code></td><td>Definition of AWS::ARCZonalShift::AutoshiftObserverNotificationStatus Resource Type</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>User account id, used as part of the primary identifier for the resource</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>Region, used as part of the primary identifier for the resource</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-autoshiftobservernotificationstatus.html"><code>AWS::ARCZonalShift::AutoshiftObserverNotificationStatus</code></a>.

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
    <td><CopyableCode code="Status, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>autoshift_observer_notification_statuses</code> in a region.
```sql
SELECT
region,
status,
account_id,
region
FROM aws.arczonalshift.autoshift_observer_notification_statuses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>autoshift_observer_notification_status</code>.
```sql
SELECT
region,
status,
account_id,
region
FROM aws.arczonalshift.autoshift_observer_notification_statuses
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>|<Region>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>autoshift_observer_notification_status</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.arczonalshift.autoshift_observer_notification_statuses (
 Status,
 region
)
SELECT 
'{{ Status }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.arczonalshift.autoshift_observer_notification_statuses (
 Status,
 region
)
SELECT 
 '{{ Status }}',
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
  - name: autoshift_observer_notification_status
    props:
      - name: Status
        value:
          Status: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.arczonalshift.autoshift_observer_notification_statuses
WHERE data__Identifier = '<AccountId|Region>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>autoshift_observer_notification_statuses</code> resource, the following permissions are required:

### Create
```json
arc-zonal-shift:UpdateAutoshiftObserverNotificationStatus
```

### Read
```json
arc-zonal-shift:GetAutoshiftObserverNotificationStatus
```

### Delete
```json
arc-zonal-shift:UpdateAutoshiftObserverNotificationStatus,
arc-zonal-shift:GetAutoshiftObserverNotificationStatus
```

### List
```json
arc-zonal-shift:GetAutoshiftObserverNotificationStatus
```
