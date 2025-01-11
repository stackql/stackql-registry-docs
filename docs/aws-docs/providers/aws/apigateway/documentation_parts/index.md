---
title: documentation_parts
hide_title: false
hide_table_of_contents: false
keywords:
  - documentation_parts
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

Creates, updates, deletes or gets a <code>documentation_part</code> resource or lists <code>documentation_parts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documentation_parts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::DocumentationPart</code> resource creates a documentation part for an API. For more information, see &#91;Representation of API Documentation in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-representation.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.documentation_parts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="documentation_part_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>object</code></td><td>The <code>Location</code> property specifies the location of the Amazon API Gateway API entity that the documentation applies to. <code>Location</code> is a property of the &#91;AWS::ApiGateway::DocumentationPart&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html) resource.<br />For more information about each property, including constraints and valid values, see &#91;DocumentationPart&#93;(https://docs.aws.amazon.com/apigateway/latest/api/API_DocumentationPartLocation.html) in the *Amazon API Gateway REST API Reference*.</td></tr>
<tr><td><CopyableCode code="properties" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html"><code>AWS::ApiGateway::DocumentationPart</code></a>.

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
    <td><CopyableCode code="Location, Properties, RestApiId, region" /></td>
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
Gets all <code>documentation_parts</code> in a region.
```sql
SELECT
region,
documentation_part_id,
location,
properties,
rest_api_id
FROM aws.apigateway.documentation_parts
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>documentation_part</code>.
```sql
SELECT
region,
documentation_part_id,
location,
properties,
rest_api_id
FROM aws.apigateway.documentation_parts
WHERE region = 'us-east-1' AND data__Identifier = '<DocumentationPartId>|<RestApiId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>documentation_part</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.documentation_parts (
 Location,
 Properties,
 RestApiId,
 region
)
SELECT 
'{{ Location }}',
 '{{ Properties }}',
 '{{ RestApiId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.documentation_parts (
 Location,
 Properties,
 RestApiId,
 region
)
SELECT 
 '{{ Location }}',
 '{{ Properties }}',
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
  - name: documentation_part
    props:
      - name: Location
        value:
          Method: '{{ Method }}'
          Name: '{{ Name }}'
          Path: '{{ Path }}'
          StatusCode: '{{ StatusCode }}'
          Type: '{{ Type }}'
      - name: Properties
        value: '{{ Properties }}'
      - name: RestApiId
        value: '{{ RestApiId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.documentation_parts
WHERE data__Identifier = '<DocumentationPartId|RestApiId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>documentation_parts</code> resource, the following permissions are required:

### Create
```json
apigateway:GET,
apigateway:POST
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```
