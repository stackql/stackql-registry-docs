---
title: vdm_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - vdm_attributes
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

Creates, updates, deletes or gets a <code>vdm_attribute</code> resource or lists <code>vdm_attributes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vdm_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::VdmAttributes</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.vdm_attributes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vdm_attributes_resource_id" /></td><td><code>string</code></td><td>Unique identifier for this resource</td></tr>
<tr><td><CopyableCode code="dashboard_attributes" /></td><td><code>Preferences regarding the Dashboard feature.</code></td><td></td></tr>
<tr><td><CopyableCode code="guardian_attributes" /></td><td><code>Preferences regarding the Guardian feature.</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>vdm_attribute</code>.
```sql
SELECT
region,
vdm_attributes_resource_id,
dashboard_attributes,
guardian_attributes
FROM aws.ses.vdm_attributes
WHERE region = 'us-east-1' AND data__Identifier = '<VdmAttributesResourceId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vdm_attribute</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ses.vdm_attributes (
 DashboardAttributes,
 GuardianAttributes,
 region
)
SELECT 
'{{ DashboardAttributes }}',
 '{{ GuardianAttributes }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ses.vdm_attributes (
 DashboardAttributes,
 GuardianAttributes,
 region
)
SELECT 
 '{{ DashboardAttributes }}',
 '{{ GuardianAttributes }}',
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
  - name: vdm_attribute
    props:
      - name: DashboardAttributes
        value:
          EngagementMetrics: '{{ EngagementMetrics }}'
      - name: GuardianAttributes
        value:
          OptimizedSharedDelivery: '{{ OptimizedSharedDelivery }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ses.vdm_attributes
WHERE data__Identifier = '<VdmAttributesResourceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vdm_attributes</code> resource, the following permissions are required:

### Create
```json
ses:PutAccountVdmAttributes,
ses:GetAccount
```

### Read
```json
ses:GetAccount
```

### Update
```json
ses:PutAccountVdmAttributes,
ses:GetAccount
```

### Delete
```json
ses:PutAccountVdmAttributes,
ses:GetAccount
```

