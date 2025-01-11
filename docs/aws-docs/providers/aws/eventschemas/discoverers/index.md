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

Creates, updates, deletes or gets a <code>discoverer</code> resource or lists <code>discoverers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discoverers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Discoverer</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.discoverers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="discoverer_arn" /></td><td><code>string</code></td><td>The ARN of the discoverer.</td></tr>
<tr><td><CopyableCode code="discoverer_id" /></td><td><code>string</code></td><td>The Id of the discoverer.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the discoverer.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>The ARN of the event bus.</td></tr>
<tr><td><CopyableCode code="cross_account" /></td><td><code>boolean</code></td><td>Defines whether event schemas from other accounts are discovered. Default is True.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Defines the current state of the discoverer.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with the resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html"><code>AWS::EventSchemas::Discoverer</code></a>.

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
    <td><CopyableCode code="SourceArn, region" /></td>
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
Gets all <code>discoverers</code> in a region.
```sql
SELECT
region,
discoverer_arn,
discoverer_id,
description,
source_arn,
cross_account,
state,
tags
FROM aws.eventschemas.discoverers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>discoverer</code>.
```sql
SELECT
region,
discoverer_arn,
discoverer_id,
description,
source_arn,
cross_account,
state,
tags
FROM aws.eventschemas.discoverers
WHERE region = 'us-east-1' AND data__Identifier = '<DiscovererArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>discoverer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
schemas:DescribeDiscoverer
```

### Update
```json
schemas:DescribeDiscoverer,
schemas:UpdateDiscoverer,
schemas:TagResource,
schemas:UntagResource,
schemas:ListTagsForResource,
events:PutTargets,
events:PutRule
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
