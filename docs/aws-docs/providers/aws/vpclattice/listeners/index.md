---
title: listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - listeners
  - vpclattice
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

Creates, updates, deletes or gets a <code>listener</code> resource or lists <code>listeners</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.listeners" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_action" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="DefaultAction, Protocol, region" /></td>
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
List all <code>listeners</code> in a region.
```sql
SELECT
region,
arn
FROM aws.vpclattice.listeners
WHERE region = 'us-east-1';
```
Gets all properties from a <code>listener</code>.
```sql
SELECT
region,
arn,
default_action,
id,
name,
port,
protocol,
service_arn,
service_id,
service_identifier,
tags
FROM aws.vpclattice.listeners
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>listener</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.vpclattice.listeners (
 DefaultAction,
 Protocol,
 region
)
SELECT 
'{{ DefaultAction }}',
 '{{ Protocol }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.vpclattice.listeners (
 DefaultAction,
 Name,
 Port,
 Protocol,
 ServiceIdentifier,
 Tags,
 region
)
SELECT 
 '{{ DefaultAction }}',
 '{{ Name }}',
 '{{ Port }}',
 '{{ Protocol }}',
 '{{ ServiceIdentifier }}',
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
  - name: listener
    props:
      - name: DefaultAction
        value:
          Forward:
            TargetGroups:
              - TargetGroupIdentifier: '{{ TargetGroupIdentifier }}'
                Weight: '{{ Weight }}'
          FixedResponse:
            StatusCode: '{{ StatusCode }}'
      - name: Name
        value: '{{ Name }}'
      - name: Port
        value: '{{ Port }}'
      - name: Protocol
        value: '{{ Protocol }}'
      - name: ServiceIdentifier
        value: '{{ ServiceIdentifier }}'
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
DELETE FROM aws.vpclattice.listeners
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>listeners</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateListener,
vpc-lattice:TagResource,
vpc-lattice:GetListener,
vpc-lattice:ListTagsForResource
```

### Read
```json
vpc-lattice:GetListener,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:UpdateListener,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:GetListener,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteListener
```

### List
```json
vpc-lattice:ListListeners
```

