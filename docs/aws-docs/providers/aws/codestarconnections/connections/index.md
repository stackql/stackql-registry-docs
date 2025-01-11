---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - codestarconnections
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

Creates, updates, deletes or gets a <code>connection</code> resource or lists <code>connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeStarConnections::Connection resource which can be used to connect external source providers with AWS CodePipeline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarconnections.connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connection_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the connection. The ARN is used as the connection reference when the connection is shared between AWS services.</td></tr>
<tr><td><CopyableCode code="connection_name" /></td><td><code>string</code></td><td>The name of the connection. Connection names must be unique in an AWS user account.</td></tr>
<tr><td><CopyableCode code="connection_status" /></td><td><code>string</code></td><td>The current status of the connection.</td></tr>
<tr><td><CopyableCode code="owner_account_id" /></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.</td></tr>
<tr><td><CopyableCode code="provider_type" /></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured. You must specify either a ProviderType or a HostArn.</td></tr>
<tr><td><CopyableCode code="host_arn" /></td><td><code>string</code></td><td>The host arn configured to represent the infrastructure where your third-party provider is installed. You must specify either a ProviderType or a HostArn.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Specifies the tags applied to a connection.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html"><code>AWS::CodeStarConnections::Connection</code></a>.

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
    <td><CopyableCode code="ConnectionName, region" /></td>
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
Gets all <code>connections</code> in a region.
```sql
SELECT
region,
connection_arn,
connection_name,
connection_status,
owner_account_id,
provider_type,
host_arn,
tags
FROM aws.codestarconnections.connections
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>connection</code>.
```sql
SELECT
region,
connection_arn,
connection_name,
connection_status,
owner_account_id,
provider_type,
host_arn,
tags
FROM aws.codestarconnections.connections
WHERE region = 'us-east-1' AND data__Identifier = '<ConnectionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.codestarconnections.connections (
 ConnectionName,
 region
)
SELECT 
'{{ ConnectionName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.codestarconnections.connections (
 ConnectionName,
 ProviderType,
 HostArn,
 Tags,
 region
)
SELECT 
 '{{ ConnectionName }}',
 '{{ ProviderType }}',
 '{{ HostArn }}',
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
  - name: connection
    props:
      - name: ConnectionName
        value: '{{ ConnectionName }}'
      - name: ProviderType
        value: '{{ ProviderType }}'
      - name: HostArn
        value: '{{ HostArn }}'
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
DELETE FROM aws.codestarconnections.connections
WHERE data__Identifier = '<ConnectionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connections</code> resource, the following permissions are required:

### Create
```json
codestar-connections:CreateConnection,
codestar-connections:TagResource
```

### Read
```json
codestar-connections:GetConnection,
codestar-connections:ListTagsForResource
```

### Update
```json
codestar-connections:ListTagsForResource,
codestar-connections:TagResource,
codestar-connections:UntagResource
```

### Delete
```json
codestar-connections:DeleteConnection
```

### List
```json
codestar-connections:ListConnections,
codestar-connections:ListTagsForResource
```
