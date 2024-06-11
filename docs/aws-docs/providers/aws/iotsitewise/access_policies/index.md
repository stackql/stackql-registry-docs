---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - iotsitewise
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

Creates, updates, deletes or gets an <code>access_policy</code> resource or lists <code>access_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::AccessPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.access_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_policy_id" /></td><td><code>string</code></td><td>The ID of the access policy.</td></tr>
<tr><td><CopyableCode code="access_policy_arn" /></td><td><code>string</code></td><td>The ARN of the access policy.</td></tr>
<tr><td><CopyableCode code="access_policy_identity" /></td><td><code>object</code></td><td>The identity for this access policy. Choose either a user or a group but not both.</td></tr>
<tr><td><CopyableCode code="access_policy_permission" /></td><td><code>string</code></td><td>The permission level for this access policy. Valid values are ADMINISTRATOR or VIEWER.</td></tr>
<tr><td><CopyableCode code="access_policy_resource" /></td><td><code>object</code></td><td>The AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.</td></tr>
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
    <td><CopyableCode code="AccessPolicyIdentity, AccessPolicyPermission, AccessPolicyResource, region" /></td>
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
List all <code>access_policies</code> in a region.
```sql
SELECT
region,
access_policy_id
FROM aws.iotsitewise.access_policies
WHERE region = 'us-east-1';
```
Gets all properties from an <code>access_policy</code>.
```sql
SELECT
region,
access_policy_id,
access_policy_arn,
access_policy_identity,
access_policy_permission,
access_policy_resource
FROM aws.iotsitewise.access_policies
WHERE region = 'us-east-1' AND data__Identifier = '<AccessPolicyId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotsitewise.access_policies (
 AccessPolicyIdentity,
 AccessPolicyPermission,
 AccessPolicyResource,
 region
)
SELECT 
'{{ AccessPolicyIdentity }}',
 '{{ AccessPolicyPermission }}',
 '{{ AccessPolicyResource }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.access_policies (
 AccessPolicyIdentity,
 AccessPolicyPermission,
 AccessPolicyResource,
 region
)
SELECT 
 '{{ AccessPolicyIdentity }}',
 '{{ AccessPolicyPermission }}',
 '{{ AccessPolicyResource }}',
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
  - name: access_policy
    props:
      - name: AccessPolicyIdentity
        value:
          User:
            id: '{{ id }}'
          IamUser:
            arn: '{{ arn }}'
          IamRole:
            arn: '{{ arn }}'
      - name: AccessPolicyPermission
        value: '{{ AccessPolicyPermission }}'
      - name: AccessPolicyResource
        value:
          Portal:
            PortalAuthMode: '{{ PortalAuthMode }}'
            PortalContactEmail: '{{ PortalContactEmail }}'
            PortalDescription: '{{ PortalDescription }}'
            PortalName: '{{ PortalName }}'
            RoleArn: '{{ RoleArn }}'
            NotificationSenderEmail: '{{ NotificationSenderEmail }}'
            Alarms:
              AlarmRoleArn: '{{ AlarmRoleArn }}'
              NotificationLambdaArn: '{{ NotificationLambdaArn }}'
            Tags:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
          Project:
            PortalId: '{{ PortalId }}'
            ProjectName: '{{ ProjectName }}'
            ProjectDescription: '{{ ProjectDescription }}'
            AssetIds:
              - '{{ AssetIds[0] }}'
            Tags:
              - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotsitewise.access_policies
WHERE data__Identifier = '<AccessPolicyId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_policies</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreateAccessPolicy
```

### Read
```json
iotsitewise:DescribeAccessPolicy
```

### Update
```json
iotsitewise:DescribeAccessPolicy,
iotsitewise:UpdateAccessPolicy
```

### Delete
```json
iotsitewise:DescribeAccessPolicy,
iotsitewise:DeleteAccessPolicy
```

### List
```json
iotsitewise:ListAccessPolicies
```

