---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - systemsmanagersap
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

Creates, updates, deletes or gets an <code>application</code> resource or lists <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SystemsManagerSAP::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.systemsmanagersap.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the SSM-SAP application</td></tr>
<tr><td><CopyableCode code="credentials" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="instances" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sap_instance_number" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sid" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags of a SystemsManagerSAP application.</td></tr>
<tr><td><CopyableCode code="database_arn" /></td><td><code>string</code></td><td>The ARN of the SAP HANA database</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-systemsmanagersap-application.html"><code>AWS::SystemsManagerSAP::Application</code></a>.

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
    <td><CopyableCode code="ApplicationId, ApplicationType, region" /></td>
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
Gets all <code>applications</code> in a region.
```sql
SELECT
region,
application_id,
application_type,
arn,
credentials,
instances,
sap_instance_number,
sid,
tags,
database_arn
FROM aws.systemsmanagersap.applications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application</code>.
```sql
SELECT
region,
application_id,
application_type,
arn,
credentials,
instances,
sap_instance_number,
sid,
tags,
database_arn
FROM aws.systemsmanagersap.applications
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.systemsmanagersap.applications (
 ApplicationId,
 ApplicationType,
 region
)
SELECT 
'{{ ApplicationId }}',
 '{{ ApplicationType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.systemsmanagersap.applications (
 ApplicationId,
 ApplicationType,
 Credentials,
 Instances,
 SapInstanceNumber,
 Sid,
 Tags,
 DatabaseArn,
 region
)
SELECT 
 '{{ ApplicationId }}',
 '{{ ApplicationType }}',
 '{{ Credentials }}',
 '{{ Instances }}',
 '{{ SapInstanceNumber }}',
 '{{ Sid }}',
 '{{ Tags }}',
 '{{ DatabaseArn }}',
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
  - name: application
    props:
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: ApplicationType
        value: '{{ ApplicationType }}'
      - name: Credentials
        value:
          - DatabaseName: '{{ DatabaseName }}'
            CredentialType: '{{ CredentialType }}'
            SecretId: '{{ SecretId }}'
      - name: Instances
        value:
          - '{{ Instances[0] }}'
      - name: SapInstanceNumber
        value: '{{ SapInstanceNumber }}'
      - name: Sid
        value: '{{ Sid }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: DatabaseArn
        value: '{{ DatabaseArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.systemsmanagersap.applications
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
ssm-sap:RegisterApplication,
ssm-sap:GetApplication,
ssm-sap:TagResource,
ssm-sap:ListTagsForResource,
iam:CreateServiceLinkedRole
```

### Read
```json
ssm-sap:GetApplication,
ssm-sap:ListTagsForResource
```

### Update
```json
ssm-sap:TagResource,
ssm-sap:UntagResource,
ssm-sap:ListTagsForResource,
ssm-sap:GetApplication
```

### Delete
```json
ssm-sap:DeregisterApplication,
ssm-sap:GetApplication
```

### List
```json
ssm-sap:ListApplications
```
