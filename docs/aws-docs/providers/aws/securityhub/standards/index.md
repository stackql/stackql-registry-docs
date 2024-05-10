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


Used to retrieve a list of <code>standards</code> in a region or to create or delete a <code>standards</code> resource, use <code>standard</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SecurityHub::Standard`` resource specifies the enablement of a security standard. The standard is identified by the ``StandardsArn`` property. To view a list of ASH standards and their Amazon Resource Names (ARNs), use the &#91;DescribeStandards&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;1.0&#x2F;APIReference&#x2F;API_DescribeStandards.html) API operation.&lt;br&#x2F;&gt; You must create a separate ``AWS::SecurityHub::Standard`` resource for each standard that you want to enable.&lt;br&#x2F;&gt; For more information about ASH standards, see &#91;standards reference&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;latest&#x2F;userguide&#x2F;standards-reference.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.standards" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="standards_subscription_arn" /></td><td><code>string</code></td><td></td></tr>
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
standards_subscription_arn
FROM aws.securityhub.standards
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>standard</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- standard.iql (required properties only)
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
-- standard.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
securityhub:GetEnabledStandards,
securityhub:BatchDisableStandards
```

### List
```json
securityhub:GetEnabledStandards
```

