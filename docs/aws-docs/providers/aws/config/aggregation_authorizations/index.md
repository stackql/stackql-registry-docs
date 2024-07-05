---
title: aggregation_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregation_authorizations
  - config
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

Creates, updates, deletes or gets an <code>aggregation_authorization</code> resource or lists <code>aggregation_authorizations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aggregation_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::AggregationAuthorization</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.aggregation_authorizations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="authorized_account_id" /></td><td><code>string</code></td><td>The 12-digit account ID of the account authorized to aggregate data.</td></tr>
<tr><td><CopyableCode code="authorized_aws_region" /></td><td><code>string</code></td><td>The region authorized to collect aggregated data.</td></tr>
<tr><td><CopyableCode code="aggregation_authorization_arn" /></td><td><code>string</code></td><td>The ARN of the AggregationAuthorization.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the AggregationAuthorization.</td></tr>
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
    <td><CopyableCode code="AuthorizedAccountId, AuthorizedAwsRegion, region" /></td>
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
Gets all <code>aggregation_authorizations</code> in a region.
```sql
SELECT
region,
authorized_account_id,
authorized_aws_region,
aggregation_authorization_arn,
tags
FROM aws.config.aggregation_authorizations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>aggregation_authorization</code>.
```sql
SELECT
region,
authorized_account_id,
authorized_aws_region,
aggregation_authorization_arn,
tags
FROM aws.config.aggregation_authorizations
WHERE region = 'us-east-1' AND data__Identifier = '<AuthorizedAccountId>|<AuthorizedAwsRegion>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>aggregation_authorization</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.config.aggregation_authorizations (
 AuthorizedAccountId,
 AuthorizedAwsRegion,
 region
)
SELECT 
'{{ AuthorizedAccountId }}',
 '{{ AuthorizedAwsRegion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.config.aggregation_authorizations (
 AuthorizedAccountId,
 AuthorizedAwsRegion,
 Tags,
 region
)
SELECT 
 '{{ AuthorizedAccountId }}',
 '{{ AuthorizedAwsRegion }}',
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
  - name: aggregation_authorization
    props:
      - name: AuthorizedAccountId
        value: '{{ AuthorizedAccountId }}'
      - name: AuthorizedAwsRegion
        value: '{{ AuthorizedAwsRegion }}'
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
DELETE FROM aws.config.aggregation_authorizations
WHERE data__Identifier = '<AuthorizedAccountId|AuthorizedAwsRegion>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>aggregation_authorizations</code> resource, the following permissions are required:

### Create
```json
config:DescribeAggregationAuthorizations,
config:PutAggregationAuthorization,
config:TagResource
```

### Update
```json
config:DescribeAggregationAuthorizations,
config:TagResource,
config:UntagResource,
config:ListTagsForResource
```

### Read
```json
config:DescribeAggregationAuthorizations,
config:ListTagsForResource
```

### Delete
```json
config:DescribeAggregationAuthorizations,
config:DeleteAggregationAuthorization,
config:UntagResource
```

### List
```json
config:DescribeAggregationAuthorizations
```

