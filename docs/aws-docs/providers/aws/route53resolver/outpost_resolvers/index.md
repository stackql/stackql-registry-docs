---
title: outpost_resolvers
hide_title: false
hide_table_of_contents: false
keywords:
  - outpost_resolvers
  - route53resolver
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

Creates, updates, deletes or gets an <code>outpost_resolver</code> resource or lists <code>outpost_resolvers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outpost_resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::OutpostResolver.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.outpost_resolvers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><CopyableCode code="creator_request_id" /></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The OutpostResolver name.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The OutpostResolver ARN.</td></tr>
<tr><td><CopyableCode code="outpost_arn" /></td><td><code>string</code></td><td>The Outpost ARN.</td></tr>
<tr><td><CopyableCode code="preferred_instance_type" /></td><td><code>string</code></td><td>The OutpostResolver instance type.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The OutpostResolver status, possible values are CREATING, OPERATIONAL, UPDATING, DELETING, ACTION_NEEDED, FAILED_CREATION and FAILED_DELETION.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>The OutpostResolver status message.</td></tr>
<tr><td><CopyableCode code="instance_count" /></td><td><code>integer</code></td><td>The number of OutpostResolvers.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The OutpostResolver creation time</td></tr>
<tr><td><CopyableCode code="modification_time" /></td><td><code>string</code></td><td>The OutpostResolver last modified time</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-outpostresolver.html"><code>AWS::Route53Resolver::OutpostResolver</code></a>.

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
    <td><CopyableCode code="OutpostArn, PreferredInstanceType, Name, region" /></td>
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
Gets all <code>outpost_resolvers</code> in a region.
```sql
SELECT
region,
id,
creator_request_id,
name,
arn,
outpost_arn,
preferred_instance_type,
status,
status_message,
instance_count,
creation_time,
modification_time,
tags
FROM aws.route53resolver.outpost_resolvers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>outpost_resolver</code>.
```sql
SELECT
region,
id,
creator_request_id,
name,
arn,
outpost_arn,
preferred_instance_type,
status,
status_message,
instance_count,
creation_time,
modification_time,
tags
FROM aws.route53resolver.outpost_resolvers
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>outpost_resolver</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53resolver.outpost_resolvers (
 Name,
 OutpostArn,
 PreferredInstanceType,
 region
)
SELECT 
'{{ Name }}',
 '{{ OutpostArn }}',
 '{{ PreferredInstanceType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53resolver.outpost_resolvers (
 Name,
 OutpostArn,
 PreferredInstanceType,
 InstanceCount,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ OutpostArn }}',
 '{{ PreferredInstanceType }}',
 '{{ InstanceCount }}',
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
  - name: outpost_resolver
    props:
      - name: Name
        value: '{{ Name }}'
      - name: OutpostArn
        value: '{{ OutpostArn }}'
      - name: PreferredInstanceType
        value: '{{ PreferredInstanceType }}'
      - name: InstanceCount
        value: '{{ InstanceCount }}'
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
DELETE FROM aws.route53resolver.outpost_resolvers
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>outpost_resolvers</code> resource, the following permissions are required:

### Create
```json
route53resolver:CreateOutpostResolver,
route53resolver:GetOutpostResolver,
route53resolver:ListTagsForResource,
outposts:GetOutpost,
route53resolver:TagResource
```

### Read
```json
route53resolver:GetOutpostResolver,
route53resolver:ListTagsForResource
```

### Update
```json
route53resolver:UpdateOutpostResolver,
route53resolver:GetOutpostResolver,
route53resolver:UntagResource,
route53resolver:TagResource,
route53resolver:ListTagsForResource
```

### Delete
```json
route53resolver:DeleteOutpostResolver,
route53resolver:GetOutpostResolver,
route53resolver:ListOutpostResolvers,
route53resolver:ListResolverEndpoints
```

### List
```json
route53resolver:ListOutpostResolvers,
route53resolver:ListTagsForResource
```
