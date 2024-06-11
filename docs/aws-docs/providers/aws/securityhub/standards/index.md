---
title: standards
hide_title: false
hide_table_of_contents: false
keywords:
  - standards
  - securityhub
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

Creates, updates, deletes or gets a <code>standard</code> resource or lists <code>standards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SecurityHub::Standard</code> resource specifies the enablement of a security standard. The standard is identified by the <code>StandardsArn</code> property. To view a list of ASH standards and their Amazon Resource Names (ARNs), use the &#91;DescribeStandards&#93;(https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API operation. You must create a separate <code>AWS::SecurityHub::Standard</code> resource for each standard that you want to enable. For more information about ASH standards, see &#91;standards reference&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.standards" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="standards_subscription_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="standards_arn" /></td><td><code>string</code></td><td>The ARN of the standard that you want to enable. To view a list of available ASH standards and their ARNs, use the &#91;DescribeStandards&#93;(https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html) API operation.</td></tr>
<tr><td><CopyableCode code="disabled_standards_controls" /></td><td><code>array</code></td><td>Specifies which controls are to be disabled in a standard. *Maximum*: <code>100</code></td></tr>
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
    <td><CopyableCode code="StandardsArn, region" /></td>
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
List all <code>standards</code> in a region.
```sql
SELECT
region,
standards_subscription_arn
FROM aws.securityhub.standards
WHERE region = 'us-east-1';
```
Gets all properties from a <code>standard</code>.
```sql
SELECT
region,
standards_subscription_arn,
standards_arn,
disabled_standards_controls
FROM aws.securityhub.standards
WHERE region = 'us-east-1' AND data__Identifier = '<StandardsSubscriptionArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>standard</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.standards (
 StandardsArn,
 region
)
SELECT 
'{{ StandardsArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.standards (
 StandardsArn,
 DisabledStandardsControls,
 region
)
SELECT 
 '{{ StandardsArn }}',
 '{{ DisabledStandardsControls }}',
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
  - name: standard
    props:
      - name: StandardsArn
        value: '{{ StandardsArn }}'
      - name: DisabledStandardsControls
        value:
          - StandardsControlArn: '{{ StandardsControlArn }}'
            Reason: '{{ Reason }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.standards
WHERE data__Identifier = '<StandardsSubscriptionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>standards</code> resource, the following permissions are required:

### Create
```json
securityhub:GetEnabledStandards,
securityhub:BatchEnableStandards,
securityhub:UpdateStandardsControl
```

### Read
```json
securityhub:GetEnabledStandards,
securityhub:DescribeStandardsControls
```

### Update
```json
securityhub:GetEnabledStandards,
securityhub:UpdateStandardsControl
```

### Delete
```json
securityhub:GetEnabledStandards,
securityhub:BatchDisableStandards
```

### List
```json
securityhub:GetEnabledStandards
```

