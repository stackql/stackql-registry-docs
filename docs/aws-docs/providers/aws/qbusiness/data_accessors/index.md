---
title: data_accessors
hide_title: false
hide_table_of_contents: false
keywords:
  - data_accessors
  - qbusiness
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

Creates, updates, deletes or gets a <code>data_accessor</code> resource or lists <code>data_accessors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_accessors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::DataAccessor Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.data_accessors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="action_configurations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_accessor_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_accessor_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="idc_application_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="principal" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html"><code>AWS::QBusiness::DataAccessor</code></a>.

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
    <td><CopyableCode code="ApplicationId, ActionConfigurations, DisplayName, Principal, region" /></td>
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
Gets all <code>data_accessors</code> in a region.
```sql
SELECT
region,
action_configurations,
application_id,
created_at,
data_accessor_arn,
data_accessor_id,
display_name,
idc_application_arn,
principal,
tags,
updated_at
FROM aws.qbusiness.data_accessors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>data_accessor</code>.
```sql
SELECT
region,
action_configurations,
application_id,
created_at,
data_accessor_arn,
data_accessor_id,
display_name,
idc_application_arn,
principal,
tags,
updated_at
FROM aws.qbusiness.data_accessors
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<DataAccessorId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_accessor</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.qbusiness.data_accessors (
 ActionConfigurations,
 ApplicationId,
 DisplayName,
 Principal,
 region
)
SELECT 
'{{ ActionConfigurations }}',
 '{{ ApplicationId }}',
 '{{ DisplayName }}',
 '{{ Principal }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.qbusiness.data_accessors (
 ActionConfigurations,
 ApplicationId,
 DisplayName,
 Principal,
 Tags,
 region
)
SELECT 
 '{{ ActionConfigurations }}',
 '{{ ApplicationId }}',
 '{{ DisplayName }}',
 '{{ Principal }}',
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
  - name: data_accessor
    props:
      - name: ActionConfigurations
        value:
          - Action: '{{ Action }}'
            FilterConfiguration:
              DocumentAttributeFilter:
                AndAllFilters:
                  - null
                OrAllFilters:
                  - null
                NotFilter: null
                EqualsTo:
                  Name: '{{ Name }}'
                  Value: null
                ContainsAll: null
                ContainsAny: null
                GreaterThan: null
                GreaterThanOrEquals: null
                LessThan: null
                LessThanOrEquals: null
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: Principal
        value: '{{ Principal }}'
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
DELETE FROM aws.qbusiness.data_accessors
WHERE data__Identifier = '<ApplicationId|DataAccessorId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_accessors</code> resource, the following permissions are required:

### Create
```json
qbusiness:CreateDataAccessor,
qbusiness:GetDataAccessor,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
sso:CreateApplication,
sso:PutApplicationAuthenticationMethod,
sso:PutApplicationGrant,
sso:PutApplicationAccessScope
```

### Read
```json
qbusiness:GetDataAccessor,
qbusiness:ListTagsForResource
```

### Update
```json
qbusiness:GetDataAccessor,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UntagResource,
qbusiness:UpdateDataAccessor
```

### Delete
```json
qbusiness:DeleteDataAccessor,
qbusiness:GetDataAccessor,
sso:DeleteApplication
```

### List
```json
qbusiness:ListDataAccessors
```
