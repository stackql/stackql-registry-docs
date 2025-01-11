---
title: mail_manager_traffic_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - mail_manager_traffic_policies
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

Creates, updates, deletes or gets a <code>mail_manager_traffic_policy</code> resource or lists <code>mail_manager_traffic_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mail_manager_traffic_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::SES::MailManagerTrafficPolicy Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.mail_manager_traffic_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="default_action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_message_size_bytes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_statements" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_policy_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_policy_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_policy_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanagertrafficpolicy.html"><code>AWS::SES::MailManagerTrafficPolicy</code></a>.

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
    <td><CopyableCode code="DefaultAction, PolicyStatements, region" /></td>
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
Gets all <code>mail_manager_traffic_policies</code> in a region.
```sql
SELECT
region,
default_action,
max_message_size_bytes,
policy_statements,
tags,
traffic_policy_arn,
traffic_policy_id,
traffic_policy_name
FROM aws.ses.mail_manager_traffic_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>mail_manager_traffic_policy</code>.
```sql
SELECT
region,
default_action,
max_message_size_bytes,
policy_statements,
tags,
traffic_policy_arn,
traffic_policy_id,
traffic_policy_name
FROM aws.ses.mail_manager_traffic_policies
WHERE region = 'us-east-1' AND data__Identifier = '<TrafficPolicyId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mail_manager_traffic_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ses.mail_manager_traffic_policies (
 DefaultAction,
 PolicyStatements,
 region
)
SELECT 
'{{ DefaultAction }}',
 '{{ PolicyStatements }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ses.mail_manager_traffic_policies (
 DefaultAction,
 MaxMessageSizeBytes,
 PolicyStatements,
 Tags,
 TrafficPolicyName,
 region
)
SELECT 
 '{{ DefaultAction }}',
 '{{ MaxMessageSizeBytes }}',
 '{{ PolicyStatements }}',
 '{{ Tags }}',
 '{{ TrafficPolicyName }}',
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
  - name: mail_manager_traffic_policy
    props:
      - name: DefaultAction
        value: '{{ DefaultAction }}'
      - name: MaxMessageSizeBytes
        value: null
      - name: PolicyStatements
        value:
          - Conditions:
              - null
            Action: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TrafficPolicyName
        value: '{{ TrafficPolicyName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ses.mail_manager_traffic_policies
WHERE data__Identifier = '<TrafficPolicyId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>mail_manager_traffic_policies</code> resource, the following permissions are required:

### Create
```json
ses:TagResource,
ses:ListTagsForResource,
ses:GetTrafficPolicy,
ses:CreateTrafficPolicy
```

### Read
```json
ses:ListTagsForResource,
ses:GetTrafficPolicy
```

### Update
```json
ses:TagResource,
ses:UntagResource,
ses:ListTagsForResource,
ses:GetTrafficPolicy,
ses:UpdateTrafficPolicy
```

### Delete
```json
ses:GetTrafficPolicy,
ses:DeleteTrafficPolicy
```

### List
```json
ses:ListTrafficPolicies
```
