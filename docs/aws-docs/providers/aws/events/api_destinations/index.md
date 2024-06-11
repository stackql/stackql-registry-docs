---
title: api_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - api_destinations
  - events
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

Creates, updates, deletes or gets an <code>api_destination</code> resource or lists <code>api_destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::ApiDestination.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.api_destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the apiDestination.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="connection_arn" /></td><td><code>string</code></td><td>The arn of the connection.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The arn of the api destination.</td></tr>
<tr><td><CopyableCode code="invocation_rate_limit_per_second" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="invocation_endpoint" /></td><td><code>string</code></td><td>Url endpoint to invoke.</td></tr>
<tr><td><CopyableCode code="http_method" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ConnectionArn, InvocationEndpoint, HttpMethod, region" /></td>
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
List all <code>api_destinations</code> in a region.
```sql
SELECT
region,
name
FROM aws.events.api_destinations
WHERE region = 'us-east-1';
```
Gets all properties from an <code>api_destination</code>.
```sql
SELECT
region,
name,
description,
connection_arn,
arn,
invocation_rate_limit_per_second,
invocation_endpoint,
http_method
FROM aws.events.api_destinations
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_destination</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.events.api_destinations (
 ConnectionArn,
 InvocationEndpoint,
 HttpMethod,
 region
)
SELECT 
'{{ ConnectionArn }}',
 '{{ InvocationEndpoint }}',
 '{{ HttpMethod }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.events.api_destinations (
 Name,
 Description,
 ConnectionArn,
 InvocationRateLimitPerSecond,
 InvocationEndpoint,
 HttpMethod,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ ConnectionArn }}',
 '{{ InvocationRateLimitPerSecond }}',
 '{{ InvocationEndpoint }}',
 '{{ HttpMethod }}',
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
  - name: api_destination
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ConnectionArn
        value: '{{ ConnectionArn }}'
      - name: InvocationRateLimitPerSecond
        value: '{{ InvocationRateLimitPerSecond }}'
      - name: InvocationEndpoint
        value: '{{ InvocationEndpoint }}'
      - name: HttpMethod
        value: '{{ HttpMethod }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.events.api_destinations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>api_destinations</code> resource, the following permissions are required:

### Create
```json
events:CreateApiDestination,
events:DescribeApiDestination
```

### Read
```json
events:DescribeApiDestination
```

### Update
```json
events:UpdateApiDestination,
events:DescribeApiDestination
```

### Delete
```json
events:DeleteApiDestination,
events:DescribeApiDestination
```

### List
```json
events:ListApiDestinations
```

