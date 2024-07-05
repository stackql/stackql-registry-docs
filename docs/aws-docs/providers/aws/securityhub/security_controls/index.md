---
title: security_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - security_controls
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

Creates, updates, deletes or gets a <code>security_control</code> resource or lists <code>security_controls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A security control in Security Hub describes a security best practice related to a specific resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.security_controls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="security_control_id" /></td><td><code>string</code></td><td>The unique identifier of a security control across standards. Values for this field typically consist of an AWS service name and a number, such as APIGateway.3.</td></tr>
<tr><td><CopyableCode code="security_control_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for a security control across standards, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1`. This parameter doesn't mention a specific standard.</td></tr>
<tr><td><CopyableCode code="last_update_reason" /></td><td><code>string</code></td><td>The most recent reason for updating the customizable properties of a security control. This differs from the UpdateReason field of the BatchUpdateStandardsControlAssociations API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An object that identifies the name of a control parameter, its current value, and whether it has been customized.</td></tr>
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
    <td><CopyableCode code="Parameters, region" /></td>
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
Gets all <code>security_controls</code> in a region.
```sql
SELECT
region,
security_control_id,
security_control_arn,
last_update_reason,
parameters
FROM aws.securityhub.security_controls
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>security_control</code>.
```sql
SELECT
region,
security_control_id,
security_control_arn,
last_update_reason,
parameters
FROM aws.securityhub.security_controls
WHERE region = 'us-east-1' AND data__Identifier = '<SecurityControlId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_control</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.security_controls (
 Parameters,
 region
)
SELECT 
'{{ Parameters }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.security_controls (
 SecurityControlId,
 SecurityControlArn,
 LastUpdateReason,
 Parameters,
 region
)
SELECT 
 '{{ SecurityControlId }}',
 '{{ SecurityControlArn }}',
 '{{ LastUpdateReason }}',
 '{{ Parameters }}',
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
  - name: security_control
    props:
      - name: SecurityControlId
        value: '{{ SecurityControlId }}'
      - name: SecurityControlArn
        value: null
      - name: LastUpdateReason
        value: '{{ LastUpdateReason }}'
      - name: Parameters
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.security_controls
WHERE data__Identifier = '<SecurityControlId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_controls</code> resource, the following permissions are required:

### Create
```json
securityhub:BatchGetSecurityControls,
securityhub:DescribeStandardsControls,
securityhub:UpdateSecurityControl,
securityhub:UpdateStandardsControl
```

### Read
```json
securityhub:BatchGetSecurityControls,
securityhub:DescribeStandardsControls
```

### Update
```json
securityhub:BatchGetSecurityControls,
securityhub:DescribeStandardsControls,
securityhub:UpdateSecurityControl,
securityhub:UpdateStandardsControl
```

### Delete
```json
securityhub:BatchGetSecurityControls,
securityhub:DescribeStandardsControls,
securityhub:UpdateSecurityControl,
securityhub:UpdateStandardsControl
```

### List
```json
securityhub:BatchGetSecurityControls,
securityhub:DescribeStandardsControls,
securityhub:ListSecurityControlDefinitions
```

