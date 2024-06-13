---
title: mitigation_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - mitigation_actions
  - iot
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

Creates, updates, deletes or gets a <code>mitigation_action</code> resource or lists <code>mitigation_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mitigation_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Mitigation actions can be used to take actions to mitigate issues that were found in an Audit finding or Detect violation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.mitigation_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="action_name" /></td><td><code>string</code></td><td>A unique identifier for the mitigation action.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="action_params" /></td><td><code>object</code></td><td>The set of parameters for this mitigation action. You can specify only one type of parameter (in other words, you can apply only one action for each defined mitigation action).</td></tr>
<tr><td><CopyableCode code="mitigation_action_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mitigation_action_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="RoleArn, ActionParams, region" /></td>
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
List all <code>mitigation_actions</code> in a region.
```sql
SELECT
region,
action_name
FROM aws.iot.mitigation_actions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>mitigation_action</code>.
```sql
SELECT
region,
action_name,
role_arn,
tags,
action_params,
mitigation_action_arn,
mitigation_action_id
FROM aws.iot.mitigation_actions
WHERE region = 'us-east-1' AND data__Identifier = '<ActionName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mitigation_action</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.mitigation_actions (
 RoleArn,
 ActionParams,
 region
)
SELECT 
'{{ RoleArn }}',
 '{{ ActionParams }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.mitigation_actions (
 ActionName,
 RoleArn,
 Tags,
 ActionParams,
 region
)
SELECT 
 '{{ ActionName }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ ActionParams }}',
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
  - name: mitigation_action
    props:
      - name: ActionName
        value: '{{ ActionName }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ActionParams
        value:
          AddThingsToThingGroupParams:
            OverrideDynamicGroups: '{{ OverrideDynamicGroups }}'
            ThingGroupNames:
              - '{{ ThingGroupNames[0] }}'
          EnableIoTLoggingParams:
            LogLevel: '{{ LogLevel }}'
            RoleArnForLogging: '{{ RoleArnForLogging }}'
          PublishFindingToSnsParams:
            TopicArn: '{{ TopicArn }}'
          ReplaceDefaultPolicyVersionParams:
            TemplateName: '{{ TemplateName }}'
          UpdateCACertificateParams:
            Action: '{{ Action }}'
          UpdateDeviceCertificateParams:
            Action: '{{ Action }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iot.mitigation_actions
WHERE data__Identifier = '<ActionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>mitigation_actions</code> resource, the following permissions are required:

### Create
```json
iot:CreateMitigationAction,
iot:DescribeMitigationAction,
iot:TagResource,
iam:PassRole
```

### Read
```json
iot:DescribeMitigationAction,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateMitigationAction,
iot:ListTagsForResource,
iot:UntagResource,
iot:TagResource,
iam:PassRole
```

### Delete
```json
iot:DescribeMitigationAction,
iot:DeleteMitigationAction
```

### List
```json
iot:ListMitigationActions
```

