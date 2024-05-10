---
title: discoverers
hide_title: false
hide_table_of_contents: false
keywords:
  - discoverers
  - eventschemas
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


Used to retrieve a list of <code>discoverers</code> in a region or to create or delete a <code>discoverers</code> resource, use <code>discoverer</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discoverers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Discoverer</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.discoverers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="discoverer_arn" /></td><td><code>string</code></td><td>The ARN of the discoverer.</td></tr>
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
discoverer_arn
FROM aws.eventschemas.discoverers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>discoverer</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- discoverer.iql (required properties only)
INSERT INTO aws.eventschemas.discoverers (
 SourceArn,
 region
)
SELECT 
'{{ SourceArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- discoverer.iql (all properties)
INSERT INTO aws.eventschemas.discoverers (
 Description,
 SourceArn,
 CrossAccount,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ SourceArn }}',
 '{{ CrossAccount }}',
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
  - name: discoverer
    props:
      - name: Description
        value: '{{ Description }}'
      - name: SourceArn
        value: '{{ SourceArn }}'
      - name: CrossAccount
        value: '{{ CrossAccount }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.eventschemas.discoverers
WHERE data__Identifier = '<DiscovererArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>discoverers</code> resource, the following permissions are required:

### Create
```json
schemas:CreateDiscoverer,
schemas:DescribeDiscoverer,
schemas:TagResource,
events:PutRule,
events:PutTargets,
events:EnableRule,
events:ListTargetsByRule,
iam:CreateServiceLinkedRole
```

### Delete
```json
schemas:DescribeDiscoverer,
schemas:DeleteDiscoverer,
events:DeleteRule,
events:DisableRule,
events:RemoveTargets
```

### List
```json
schemas:ListDiscoverers
```

