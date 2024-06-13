---
title: configuration_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_policies
  - securityhub
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

Creates, updates, deletes or gets a <code>configuration_policy</code> resource or lists <code>configuration_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::ConfigurationPolicy resource represents the Central Configuration Policy in your account.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.configuration_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the configuration policy.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the configuration policy.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the configuration policy.</td></tr>
<tr><td><CopyableCode code="configuration_policy" /></td><td><code>object</code></td><td>An object that defines how Security Hub is configured.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The universally unique identifier (UUID) of the configuration policy.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time, in UTC and ISO 8601 format.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The date and time, in UTC and ISO 8601 format.</td></tr>
<tr><td><CopyableCode code="service_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the service that the configuration policy applies to is enabled in the policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
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
    <td><CopyableCode code="ConfigurationPolicy, Name, region" /></td>
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
List all <code>configuration_policies</code> in a region.
```sql
SELECT
region,
arn
FROM aws.securityhub.configuration_policies
WHERE region = 'us-east-1';
```
Gets all properties from a <code>configuration_policy</code>.
```sql
SELECT
region,
arn,
name,
description,
configuration_policy,
id,
created_at,
updated_at,
service_enabled,
tags
FROM aws.securityhub.configuration_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.configuration_policies (
 Name,
 ConfigurationPolicy,
 region
)
SELECT 
'{{ Name }}',
 '{{ ConfigurationPolicy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.configuration_policies (
 Name,
 Description,
 ConfigurationPolicy,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ ConfigurationPolicy }}',
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
  - name: configuration_policy
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ConfigurationPolicy
        value:
          SecurityHub:
            EnabledStandardIdentifiers:
              - '{{ EnabledStandardIdentifiers[0] }}'
            ServiceEnabled: '{{ ServiceEnabled }}'
            SecurityControlsConfiguration:
              DisabledSecurityControlIdentifiers:
                - '{{ DisabledSecurityControlIdentifiers[0] }}'
              EnabledSecurityControlIdentifiers:
                - '{{ EnabledSecurityControlIdentifiers[0] }}'
              SecurityControlCustomParameters:
                - Parameters: {}
                  SecurityControlId: '{{ SecurityControlId }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.configuration_policies
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configuration_policies</code> resource, the following permissions are required:

### Create
```json
securityhub:CreateConfigurationPolicy,
securityhub:TagResource,
securityhub:ListTagsForResource
```

### Read
```json
securityhub:GetConfigurationPolicy,
securityhub:ListTagsForResource
```

### Update
```json
securityhub:UpdateConfigurationPolicy,
securityhub:TagResource,
securityhub:UntagResource,
securityhub:ListTagsForResource
```

### Delete
```json
securityhub:GetConfigurationPolicy,
securityhub:DeleteConfigurationPolicy
```

### List
```json
securityhub:ListConfigurationPolicies,
securityhub:ListTagsForResource
```

