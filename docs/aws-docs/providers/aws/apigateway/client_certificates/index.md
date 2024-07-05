---
title: client_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - client_certificates
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

Creates, updates, deletes or gets a <code>client_certificate</code> resource or lists <code>client_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::ClientCertificate</code> resource creates a client certificate that API Gateway uses to configure client-side SSL authentication for sending requests to the integration endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.client_certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="client_certificate_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the client certificate.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>client_certificates</code> in a region.
```sql
SELECT
region,
client_certificate_id,
description,
tags
FROM aws.apigateway.client_certificates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>client_certificate</code>.
```sql
SELECT
region,
client_certificate_id,
description,
tags
FROM aws.apigateway.client_certificates
WHERE region = 'us-east-1' AND data__Identifier = '<ClientCertificateId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>client_certificate</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.client_certificates (
 Description,
 Tags,
 region
)
SELECT 
'{{ Description }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.client_certificates (
 Description,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
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
  - name: client_certificate
    props:
      - name: Description
        value: '{{ Description }}'
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
DELETE FROM aws.apigateway.client_certificates
WHERE data__Identifier = '<ClientCertificateId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>client_certificates</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET,
apigateway:PUT
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH,
apigateway:PUT,
apigateway:DELETE
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```

