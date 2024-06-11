---
title: resource_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_collections
  - devopsguru
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

Creates, updates, deletes or gets a <code>resource_collection</code> resource or lists <code>resource_collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the ResourceCollection resource in the Amazon DevOps Guru.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.devopsguru.resource_collections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_collection_filter" /></td><td><code>Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_collection_type" /></td><td><code>string</code></td><td>The type of ResourceCollection</td></tr>
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
    <td><CopyableCode code="ResourceCollectionFilter, region" /></td>
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
List all <code>resource_collections</code> in a region.
```sql
SELECT
region,
resource_collection_type
FROM aws.devopsguru.resource_collections
WHERE region = 'us-east-1';
```
Gets all properties from a <code>resource_collection</code>.
```sql
SELECT
region,
resource_collection_filter,
resource_collection_type
FROM aws.devopsguru.resource_collections
WHERE region = 'us-east-1' AND data__Identifier = '<ResourceCollectionType>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_collection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.devopsguru.resource_collections (
 ResourceCollectionFilter,
 region
)
SELECT 
'{{ ResourceCollectionFilter }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.devopsguru.resource_collections (
 ResourceCollectionFilter,
 region
)
SELECT 
 '{{ ResourceCollectionFilter }}',
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
  - name: resource_collection
    props:
      - name: ResourceCollectionFilter
        value:
          CloudFormation:
            StackNames:
              - '{{ StackNames[0] }}'
          Tags:
            - AppBoundaryKey: '{{ AppBoundaryKey }}'
              TagValues:
                - '{{ TagValues[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.devopsguru.resource_collections
WHERE data__Identifier = '<ResourceCollectionType>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_collections</code> resource, the following permissions are required:

### Create
```json
devops-guru:UpdateResourceCollection,
devops-guru:GetResourceCollection
```

### Read
```json
devops-guru:GetResourceCollection
```

### Delete
```json
devops-guru:UpdateResourceCollection,
devops-guru:GetResourceCollection
```

### List
```json
devops-guru:GetResourceCollection
```

### Update
```json
devops-guru:UpdateResourceCollection,
devops-guru:GetResourceCollection
```

