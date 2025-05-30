---
title: mail_manager_addon_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - mail_manager_addon_subscriptions
  - ses
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

Creates, updates, deletes or gets a <code>mail_manager_addon_subscription</code> resource or lists <code>mail_manager_addon_subscriptions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mail_manager_addon_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::SES::MailManagerAddonSubscription Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.mail_manager_addon_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="addon_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="addon_subscription_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="addon_subscription_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanageraddonsubscription.html"><code>AWS::SES::MailManagerAddonSubscription</code></a>.

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
    <td><CopyableCode code="AddonName, region" /></td>
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
Gets all <code>mail_manager_addon_subscriptions</code> in a region.
```sql
SELECT
region,
addon_name,
addon_subscription_arn,
addon_subscription_id,
tags
FROM aws.ses.mail_manager_addon_subscriptions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>mail_manager_addon_subscription</code>.
```sql
SELECT
region,
addon_name,
addon_subscription_arn,
addon_subscription_id,
tags
FROM aws.ses.mail_manager_addon_subscriptions
WHERE region = 'us-east-1' AND data__Identifier = '<AddonSubscriptionId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mail_manager_addon_subscription</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ses.mail_manager_addon_subscriptions (
 AddonName,
 region
)
SELECT 
'{{ AddonName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ses.mail_manager_addon_subscriptions (
 AddonName,
 Tags,
 region
)
SELECT 
 '{{ AddonName }}',
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
  - name: mail_manager_addon_subscription
    props:
      - name: AddonName
        value: '{{ AddonName }}'
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
DELETE FROM aws.ses.mail_manager_addon_subscriptions
WHERE data__Identifier = '<AddonSubscriptionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>mail_manager_addon_subscriptions</code> resource, the following permissions are required:

### Create
```json
ses:TagResource,
ses:ListTagsForResource,
ses:GetAddonSubscription,
ses:CreateAddonSubscription
```

### Read
```json
ses:ListTagsForResource,
ses:GetAddonSubscription
```

### Update
```json
ses:TagResource,
ses:UntagResource,
ses:ListTagsForResource,
ses:GetAddonSubscription
```

### Delete
```json
ses:GetAddonSubscription,
ses:DeleteAddonSubscription
```

### List
```json
ses:ListAddonSubscriptions
```
