---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - apigateway
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

Creates, updates, deletes or gets a <code>resource</code> resource or lists <code>resources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Resource</code> resource creates a resource in an API.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.resources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="parent_id" /></td><td><code>string</code></td><td>The parent resource's identifier.</td></tr>
<tr><td><CopyableCode code="path_part" /></td><td><code>string</code></td><td>The last path segment for this resource.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
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
    <td><CopyableCode code="ParentId, PathPart, RestApiId, region" /></td>
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
List all <code>resources</code> in a region.
```sql
SELECT
region,
rest_api_id,
resource_id
FROM aws.apigateway.resources
WHERE region = 'us-east-1';
```
Gets all properties from a <code>resource</code>.
```sql
SELECT
region,
parent_id,
path_part,
resource_id,
rest_api_id
FROM aws.apigateway.resources
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>|<ResourceId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.resources (
 ParentId,
 PathPart,
 RestApiId,
 region
)
SELECT 
'{{ ParentId }}',
 '{{ PathPart }}',
 '{{ RestApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.resources (
 ParentId,
 PathPart,
 RestApiId,
 region
)
SELECT 
 '{{ ParentId }}',
 '{{ PathPart }}',
 '{{ RestApiId }}',
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
  - name: resource
    props:
      - name: ParentId
        value: '{{ ParentId }}'
      - name: PathPart
        value: '{{ PathPart }}'
      - name: RestApiId
        value: '{{ RestApiId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.resources
WHERE data__Identifier = '<RestApiId|ResourceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resources</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Create
```json
apigateway:POST
```

### Update
```json
apigateway:GET,
apigateway:PATCH
```

### List
```json
apigateway:GET
```

### Delete
```json
apigateway:DELETE
```

