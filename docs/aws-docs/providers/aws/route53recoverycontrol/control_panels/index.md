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

Creates, updates, deletes or gets a <code>control_panel</code> resource or lists <code>control_panels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>control_panels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Control Control Panel resource schema .</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.control_panels" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>Cluster to associate with the Control Panel</td></tr>
<tr><td><CopyableCode code="control_panel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the control panel. You can use any non-white space character in the name.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The deployment status of control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><CopyableCode code="default_control_panel" /></td><td><code>boolean</code></td><td>A flag that Amazon Route 53 Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Route 53 Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false.</td></tr>
<tr><td><CopyableCode code="routing_control_count" /></td><td><code>integer</code></td><td>Count of associated routing controls</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
Gets all <code>control_panels</code> in a region.
```sql
SELECT
region,
cluster_arn,
control_panel_arn,
name,
status,
default_control_panel,
routing_control_count,
tags
FROM aws.route53recoverycontrol.control_panels
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>control_panel</code>.
```sql
SELECT
region,
cluster_arn,
control_panel_arn,
name,
status,
default_control_panel,
routing_control_count,
tags
FROM aws.route53recoverycontrol.control_panels
WHERE region = 'us-east-1' AND data__Identifier = '<ControlPanelArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>control_panel</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53recoverycontrol.control_panels (
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
INSERT INTO aws.route53recoverycontrol.control_panels (
 ClusterArn,
 Name,
 Tags,
 region
)
SELECT 
 '{{ ClusterArn }}',
 '{{ Name }}',
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
  - name: control_panel
    props:
      - name: ClusterArn
        value: '{{ ClusterArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
route53-recovery-control-config:DescribeControlPanel,
route53-recovery-control-config:ListTagsForResource
```

### Update
```json
route53-recovery-control-config:UpdateControlPanel,
route53-recovery-control-config:DescribeControlPanel,
route53-recovery-control-config:ListTagsForResource,
route53-recovery-control-config:TagResource,
route53-recovery-control-config:UntagResource
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

