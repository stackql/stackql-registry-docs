---
title: collections
hide_title: false
hide_table_of_contents: false
keywords:
  - collections
  - opensearchserverless
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

Creates, updates, deletes or gets a <code>collection</code> resource or lists <code>collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless collection resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.collections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the collection</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the collection</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the collection.<br />The name must meet the following criteria:<br />Unique to your account and AWS Region<br />Starts with a lowercase letter<br />Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)<br />Contains between 3 and 32 characters<br /></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>List of tags to be added to the resource</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the collection.</td></tr>
<tr><td><CopyableCode code="collection_endpoint" /></td><td><code>string</code></td><td>The endpoint for the collection.</td></tr>
<tr><td><CopyableCode code="dashboard_endpoint" /></td><td><code>string</code></td><td>The OpenSearch Dashboards endpoint for the collection.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The possible types for the collection</td></tr>
<tr><td><CopyableCode code="standby_replicas" /></td><td><code>string</code></td><td>The possible standby replicas for the collection</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-collection.html"><code>AWS::OpenSearchServerless::Collection</code></a>.

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
Gets all <code>collections</code> in a region.
```sql
SELECT
region,
description,
id,
name,
tags,
arn,
collection_endpoint,
dashboard_endpoint,
type,
standby_replicas
FROM aws.opensearchserverless.collections
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>collection</code>.
```sql
SELECT
region,
description,
id,
name,
tags,
arn,
collection_endpoint,
dashboard_endpoint,
type,
standby_replicas
FROM aws.opensearchserverless.collections
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>collection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.opensearchserverless.collections (
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
INSERT INTO aws.opensearchserverless.collections (
 Description,
 Name,
 Tags,
 Type,
 StandbyReplicas,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ Tags }}',
 '{{ Type }}',
 '{{ StandbyReplicas }}',
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
  - name: collection
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'
      - name: StandbyReplicas
        value: '{{ StandbyReplicas }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.opensearchserverless.collections
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>collections</code> resource, the following permissions are required:

### Create
```json
aoss:CreateCollection,
aoss:BatchGetCollection,
iam:CreateServiceLinkedRole
```

### Delete
```json
aoss:DeleteCollection,
aoss:BatchGetCollection
```

### List
```json
aoss:ListCollections
```

### Read
```json
aoss:BatchGetCollection
```

### Update
```json
aoss:UpdateCollection,
aoss:BatchGetCollection
```
