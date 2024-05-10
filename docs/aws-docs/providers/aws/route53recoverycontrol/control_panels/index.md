---
title: control_panels
hide_title: false
hide_table_of_contents: false
keywords:
  - control_panels
  - route53recoverycontrol
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


Used to retrieve a list of <code>control_panels</code> in a region or to create or delete a <code>control_panels</code> resource, use <code>control_panel</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>control_panels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Control Control Panel resource schema .</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.control_panels" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="control_panel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
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
control_panel_arn
FROM aws.route53recoverycontrol.control_panels
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.route53recoverycontrol.control_panels (
 Name,
 region
)
SELECT 
{{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ClusterArn": "{{ ClusterArn }}",
 "Name": "{{ Name }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.route53recoverycontrol.control_panels (
 ClusterArn,
 Name,
 Tags,
 region
)
SELECT 
 {{ ClusterArn }},
 {{ Name }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53recoverycontrol.control_panels
WHERE data__Identifier = '<ControlPanelArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>control_panels</code> resource, the following permissions are required:

### Create
```json
route53-recovery-control-config:CreateControlPanel,
route53-recovery-control-config:DescribeCluster,
route53-recovery-control-config:DescribeControlPanel,
route53-recovery-control-config:ListTagsForResource,
route53-recovery-control-config:TagResource
```

### Delete
```json
route53-recovery-control-config:DeleteControlPanel,
route53-recovery-control-config:DescribeControlPanel
```

### List
```json
route53-recovery-control-config:ListControlPanels
```

