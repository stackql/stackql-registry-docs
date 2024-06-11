---
title: routing_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_controls
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

Creates, updates, deletes or gets a <code>routing_control</code> resource or lists <code>routing_controls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Control Routing Control resource schema .</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.routing_controls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="routing_control_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the routing control.</td></tr>
<tr><td><CopyableCode code="control_panel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the control panel.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the routing control. You can use any non-white space character in the name.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>Arn associated with Control Panel</td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
List all <code>routing_controls</code> in a region.
```sql
SELECT
region,
routing_control_arn
FROM aws.route53recoverycontrol.routing_controls
WHERE region = 'us-east-1';
```
Gets all properties from a <code>routing_control</code>.
```sql
SELECT
region,
routing_control_arn,
control_panel_arn,
name,
status,
cluster_arn
FROM aws.route53recoverycontrol.routing_controls
WHERE region = 'us-east-1' AND data__Identifier = '<RoutingControlArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>routing_control</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53recoverycontrol.routing_controls (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53recoverycontrol.routing_controls (
 ControlPanelArn,
 Name,
 ClusterArn,
 region
)
SELECT 
 '{{ ControlPanelArn }}',
 '{{ Name }}',
 '{{ ClusterArn }}',
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
  - name: routing_control
    props:
      - name: ControlPanelArn
        value: '{{ ControlPanelArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: ClusterArn
        value: '{{ ClusterArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53recoverycontrol.routing_controls
WHERE data__Identifier = '<RoutingControlArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>routing_controls</code> resource, the following permissions are required:

### Create
```json
route53-recovery-control-config:CreateRoutingControl,
route53-recovery-control-config:DescribeRoutingControl,
route53-recovery-control-config:DescribeControlPanel,
route53-recovery-control-config:DescribeCluster
```

### Read
```json
route53-recovery-control-config:DescribeRoutingControl
```

### Update
```json
route53-recovery-control-config:UpdateRoutingControl,
route53-recovery-control-config:DescribeRoutingControl,
route53-recovery-control-config:DescribeControlPanel
```

### Delete
```json
route53-recovery-control-config:DescribeRoutingControl,
route53-recovery-control-config:DeleteRoutingControl
```

### List
```json
route53-recovery-control-config:ListRoutingControls
```

