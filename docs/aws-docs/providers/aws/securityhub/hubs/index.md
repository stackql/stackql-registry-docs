---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
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

Creates, updates, deletes or gets a <code>hub</code> resource or lists <code>hubs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::Hub resource represents the implementation of the AWS Security Hub service in your account. One hub resource is created for each Region in which you enable Security Hub.<br /></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.hubs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>An ARN is automatically created for the customer.</td></tr>
<tr><td><CopyableCode code="enable_default_standards" /></td><td><code>boolean</code></td><td>Whether to enable the security standards that Security Hub has designated as automatically enabled.</td></tr>
<tr><td><CopyableCode code="control_finding_generator" /></td><td><code>string</code></td><td>This field, used when enabling Security Hub, specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to SECURITY_CONTROL, Security Hub generates a single finding for a control check even when the check applies to multiple enabled standards. If the value for this field is set to STANDARD_CONTROL, Security Hub generates separate findings for a control check when the check applies to multiple enabled standards.</td></tr>
<tr><td><CopyableCode code="auto_enable_controls" /></td><td><code>boolean</code></td><td>Whether to automatically enable new controls when they are added to standards that are enabled</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="subscribed_at" /></td><td><code>string</code></td><td>The date and time when Security Hub was enabled in the account.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html"><code>AWS::SecurityHub::Hub</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>hubs</code> in a region.
```sql
SELECT
region,
arn,
enable_default_standards,
control_finding_generator,
auto_enable_controls,
tags,
subscribed_at
FROM aws.securityhub.hubs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>hub</code>.
```sql
SELECT
region,
arn,
enable_default_standards,
control_finding_generator,
auto_enable_controls,
tags,
subscribed_at
FROM aws.securityhub.hubs
WHERE region = 'us-east-1' AND data__Identifier = '<ARN>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hub</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.hubs (
 EnableDefaultStandards,
 ControlFindingGenerator,
 AutoEnableControls,
 Tags,
 region
)
SELECT 
'{{ EnableDefaultStandards }}',
 '{{ ControlFindingGenerator }}',
 '{{ AutoEnableControls }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.hubs (
 EnableDefaultStandards,
 ControlFindingGenerator,
 AutoEnableControls,
 Tags,
 region
)
SELECT 
 '{{ EnableDefaultStandards }}',
 '{{ ControlFindingGenerator }}',
 '{{ AutoEnableControls }}',
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
  - name: hub
    props:
      - name: EnableDefaultStandards
        value: '{{ EnableDefaultStandards }}'
      - name: ControlFindingGenerator
        value: '{{ ControlFindingGenerator }}'
      - name: AutoEnableControls
        value: '{{ AutoEnableControls }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.hubs
WHERE data__Identifier = '<ARN>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>hubs</code> resource, the following permissions are required:

### Create
```json
securityhub:EnableSecurityHub,
securityhub:UpdateSecurityHubConfiguration,
securityhub:TagResource,
securityhub:ListTagsForResource
```

### Read
```json
securityhub:DescribeHub,
securityhub:ListTagsForResource
```

### Update
```json
securityhub:DescribeHub,
securityhub:UpdateSecurityHubConfiguration,
securityhub:TagResource,
securityhub:UntagResource,
securityhub:ListTagsForResource
```

### Delete
```json
securityhub:DisableSecurityHub
```

### List
```json
securityhub:DescribeHub,
securityhub:ListTagsForResource
```
