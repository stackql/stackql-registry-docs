---
title: configuration_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_managers
  - ssmquicksetup
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

Creates, updates, deletes or gets a <code>configuration_manager</code> resource or lists <code>configuration_managers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::SSMQuickSetup::ConfigurationManager Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmquicksetup.configuration_managers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration_definitions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manager_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_summaries" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmquicksetup-configurationmanager.html"><code>AWS::SSMQuickSetup::ConfigurationManager</code></a>.

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
    <td><CopyableCode code="ConfigurationDefinitions, region" /></td>
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
Gets all <code>configuration_managers</code> in a region.
```sql
SELECT
region,
configuration_definitions,
created_at,
description,
last_modified_at,
manager_arn,
name,
status_summaries,
tags
FROM aws.ssmquicksetup.configuration_managers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>configuration_manager</code>.
```sql
SELECT
region,
configuration_definitions,
created_at,
description,
last_modified_at,
manager_arn,
name,
status_summaries,
tags
FROM aws.ssmquicksetup.configuration_managers
WHERE region = 'us-east-1' AND data__Identifier = '<ManagerArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_manager</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ssmquicksetup.configuration_managers (
 ConfigurationDefinitions,
 region
)
SELECT 
'{{ ConfigurationDefinitions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ssmquicksetup.configuration_managers (
 ConfigurationDefinitions,
 Description,
 Name,
 Tags,
 region
)
SELECT 
 '{{ ConfigurationDefinitions }}',
 '{{ Description }}',
 '{{ Name }}',
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
  - name: configuration_manager
    props:
      - name: ConfigurationDefinitions
        value:
          - Type: '{{ Type }}'
            Parameters: {}
            TypeVersion: '{{ TypeVersion }}'
            LocalDeploymentExecutionRoleName: '{{ LocalDeploymentExecutionRoleName }}'
            LocalDeploymentAdministrationRoleArn: '{{ LocalDeploymentAdministrationRoleArn }}'
            id: '{{ id }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ssmquicksetup.configuration_managers
WHERE data__Identifier = '<ManagerArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configuration_managers</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:CreateServiceLinkedRole,
iam:ListRoles,
iam:PassRole,
ssm-quicksetup:CreateConfigurationManager,
ssm-quicksetup:GetConfigurationManager,
ssm-quicksetup:TagResource,
ssm-quicksetup:UntagResource,
ssm-quicksetup:UpdateConfigurationManager,
ssm:Describe*,
ssm:Get*,
ssm:List*,
ssm:DeleteAssociation,
ssm:CreateResourceDataSync,
ssm:UpdateResourceDataSync,
ssm:StartAutomationExecution,
ssm:CreateAssociation,
ssm:StartAssociationsOnce,
cloudformation:List*,
cloudformation:Describe*,
cloudformation:CreateStack,
cloudformation:CreateStackInstances,
cloudformation:CreateStackSet,
cloudformation:DeleteStack,
cloudformation:DeleteStackInstances,
cloudformation:DeleteStackSet,
cloudformation:UpdateStack,
cloudformation:UpdateStackSet,
cloudformation:StopStackSetOperation,
cloudformation:GetTemplate,
cloudformation:RollbackStack,
cloudformation:TagResource,
cloudformation:UntagResource,
organizations:Describe*,
organizations:List*,
organizations:RegisterDelegatedAdministrator,
organizations:DeregisterDelegatedAdministrator,
organizations:EnableAWSServiceAccess
```

### Read
```json
ssm-quicksetup:GetConfigurationManager,
iam:GetRole,
iam:PassRole,
iam:ListRoles,
ssm:DescribeDocument,
ssm:GetDocument
```

### Update
```json
iam:GetRole,
iam:CreateServiceLinkedRole,
iam:ListRoles,
iam:PassRole,
ssm-quicksetup:GetConfigurationManager,
ssm-quicksetup:TagResource,
ssm-quicksetup:UntagResource,
ssm-quicksetup:UpdateConfigurationManager,
ssm-quicksetup:UpdateConfigurationDefinition,
ssm:Describe*,
ssm:Get*,
ssm:List*,
ssm:DeleteAssociation,
ssm:CreateResourceDataSync,
ssm:UpdateResourceDataSync,
ssm:StartAutomationExecution,
ssm:CreateAssociation,
ssm:StartAssociationsOnce,
cloudformation:List*,
cloudformation:Describe*,
cloudformation:CreateStack,
cloudformation:CreateStackInstances,
cloudformation:CreateStackSet,
cloudformation:DeleteStack,
cloudformation:DeleteStackInstances,
cloudformation:DeleteStackSet,
cloudformation:UpdateStack,
cloudformation:UpdateStackSet,
cloudformation:StopStackSetOperation,
cloudformation:GetTemplate,
cloudformation:RollbackStack,
cloudformation:TagResource,
cloudformation:UntagResource,
organizations:Describe*,
organizations:List*,
organizations:RegisterDelegatedAdministrator,
organizations:DeregisterDelegatedAdministrator,
organizations:EnableAWSServiceAccess
```

### Delete
```json
ssm-quicksetup:DeleteConfigurationManager,
iam:GetRole,
iam:CreateServiceLinkedRole,
iam:ListRoles,
iam:PassRole,
ssm-quicksetup:GetConfigurationManager,
ssm-quicksetup:ListConfigurationManagers,
ssm-quicksetup:TagResource,
ssm-quicksetup:UntagResource,
ssm-quicksetup:UpdateConfigurationManager,
ssm:Describe*,
ssm:Get*,
ssm:List*,
ssm:DeleteAssociation,
ssm:CreateResourceDataSync,
ssm:UpdateResourceDataSync,
ssm:StartAutomationExecution,
ssm:CreateAssociation,
ssm:StartAssociationsOnce,
cloudformation:List*,
cloudformation:Describe*,
cloudformation:CreateStack,
cloudformation:CreateStackInstances,
cloudformation:CreateStackSet,
cloudformation:DeleteStack,
cloudformation:DeleteStackInstances,
cloudformation:DeleteStackSet,
cloudformation:UpdateStack,
cloudformation:UpdateStackSet,
cloudformation:StopStackSetOperation,
cloudformation:GetTemplate,
cloudformation:RollbackStack,
cloudformation:TagResource,
cloudformation:UntagResource,
organizations:Describe*,
organizations:List*,
organizations:RegisterDelegatedAdministrator,
organizations:DeregisterDelegatedAdministrator,
organizations:EnableAWSServiceAccess
```

### List
```json
ssm-quicksetup:ListConfigurationManagers
```
