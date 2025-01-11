---
title: mail_manager_ingress_points
hide_title: false
hide_table_of_contents: false
keywords:
  - mail_manager_ingress_points
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

Creates, updates, deletes or gets a <code>mail_manager_ingress_point</code> resource or lists <code>mail_manager_ingress_points</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mail_manager_ingress_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::SES::MailManagerIngressPoint Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.mail_manager_ingress_points" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="a_record" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_policy_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ingress_point_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="ingress_point_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ingress_point_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ingress_point_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_to_update" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-mailmanageringresspoint.html"><code>AWS::SES::MailManagerIngressPoint</code></a>.

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
    <td><CopyableCode code="Type, TrafficPolicyId, RuleSetId, region" /></td>
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
Gets all <code>mail_manager_ingress_points</code> in a region.
```sql
SELECT
region,
a_record,
traffic_policy_id,
ingress_point_configuration,
ingress_point_arn,
ingress_point_id,
ingress_point_name,
rule_set_id,
status,
status_to_update,
tags,
type
FROM aws.ses.mail_manager_ingress_points
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>mail_manager_ingress_point</code>.
```sql
SELECT
region,
a_record,
traffic_policy_id,
ingress_point_configuration,
ingress_point_arn,
ingress_point_id,
ingress_point_name,
rule_set_id,
status,
status_to_update,
tags,
type
FROM aws.ses.mail_manager_ingress_points
WHERE region = 'us-east-1' AND data__Identifier = '<IngressPointId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mail_manager_ingress_point</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ses.mail_manager_ingress_points (
 TrafficPolicyId,
 RuleSetId,
 Type,
 region
)
SELECT 
'{{ TrafficPolicyId }}',
 '{{ RuleSetId }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ses.mail_manager_ingress_points (
 TrafficPolicyId,
 IngressPointConfiguration,
 IngressPointName,
 RuleSetId,
 StatusToUpdate,
 Tags,
 Type,
 region
)
SELECT 
 '{{ TrafficPolicyId }}',
 '{{ IngressPointConfiguration }}',
 '{{ IngressPointName }}',
 '{{ RuleSetId }}',
 '{{ StatusToUpdate }}',
 '{{ Tags }}',
 '{{ Type }}',
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
  - name: mail_manager_ingress_point
    props:
      - name: TrafficPolicyId
        value: '{{ TrafficPolicyId }}'
      - name: IngressPointConfiguration
        value: null
      - name: IngressPointName
        value: '{{ IngressPointName }}'
      - name: RuleSetId
        value: '{{ RuleSetId }}'
      - name: StatusToUpdate
        value: '{{ StatusToUpdate }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ses.mail_manager_ingress_points
WHERE data__Identifier = '<IngressPointId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>mail_manager_ingress_points</code> resource, the following permissions are required:

### Create
```json
ses:TagResource,
ses:ListTagsForResource,
ses:GetIngressPoint,
ses:CreateIngressPoint,
iam:CreateServiceLinkedRole
```

### Read
```json
ses:ListTagsForResource,
ses:GetIngressPoint
```

### Update
```json
ses:TagResource,
ses:UntagResource,
ses:ListTagsForResource,
ses:GetIngressPoint,
ses:UpdateIngressPoint
```

### Delete
```json
ses:GetIngressPoint,
ses:DeleteIngressPoint
```

### List
```json
ses:ListIngressPoints
```
