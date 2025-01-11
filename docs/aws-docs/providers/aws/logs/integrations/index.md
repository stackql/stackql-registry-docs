---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - logs
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

Creates, updates, deletes or gets an <code>integration</code> resource or lists <code>integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for Logs Integration Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="integration_name" /></td><td><code>string</code></td><td>User provided identifier for integration, unique to the user account.</td></tr>
<tr><td><CopyableCode code="integration_type" /></td><td><code>string</code></td><td>The type of the Integration.</td></tr>
<tr><td><CopyableCode code="resource_config" /></td><td><code>object</code></td><td>OpenSearchResourceConfig for the given Integration</td></tr>
<tr><td><CopyableCode code="integration_status" /></td><td><code>string</code></td><td>Status of creation for the Integration and its resources</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-integration.html"><code>AWS::Logs::Integration</code></a>.

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
    <td><CopyableCode code="IntegrationName, IntegrationType, ResourceConfig, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>integrations</code> in a region.
```sql
SELECT
region,
integration_name,
integration_type,
resource_config,
integration_status
FROM aws.logs.integrations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>integration</code>.
```sql
SELECT
region,
integration_name,
integration_type,
resource_config,
integration_status
FROM aws.logs.integrations
WHERE region = 'us-east-1' AND data__Identifier = '<IntegrationName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.integrations (
 IntegrationName,
 IntegrationType,
 ResourceConfig,
 region
)
SELECT 
'{{ IntegrationName }}',
 '{{ IntegrationType }}',
 '{{ ResourceConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.integrations (
 IntegrationName,
 IntegrationType,
 ResourceConfig,
 region
)
SELECT 
 '{{ IntegrationName }}',
 '{{ IntegrationType }}',
 '{{ ResourceConfig }}',
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
  - name: integration
    props:
      - name: IntegrationName
        value: '{{ IntegrationName }}'
      - name: IntegrationType
        value: '{{ IntegrationType }}'
      - name: ResourceConfig
        value:
          OpenSearchResourceConfig:
            KmsKeyArn: '{{ KmsKeyArn }}'
            DataSourceRoleArn: null
            DashboardViewerPrincipals:
              - null
            ApplicationARN: null
            RetentionDays: '{{ RetentionDays }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.integrations
WHERE data__Identifier = '<IntegrationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>integrations</code> resource, the following permissions are required:

### Create
```json
logs:PutIntegration,
logs:GetIntegration,
aoss:CreateCollection,
aoss:CreateSecurityPolicy,
aoss:CreateAccessPolicy,
aoss:CreateLifeCyclePolicy,
aoss:BatchGetCollection,
aoss:DeleteCollection,
aoss:DeleteSecurityPolicy,
aoss:DeleteAccessPolicy,
aoss:DeleteLifeCyclePolicy,
aoss:GetAccessPolicy,
aoss:GetSecurityPolicy,
aoss:BatchGetLifecyclePolicy,
aoss:TagResource,
aoss:APIAccessAll,
opensearch:AddDirectQueryDataSource,
opensearch:DeleteDirectQueryDataSource,
opensearch:GetDirectQueryDataSource,
opensearch:CreateApplication,
opensearch:GetApplication,
opensearch:UpdateApplication,
opensearch:DeleteApplication,
opensearch:ApplicationAccessAll,
opensearch:DashboardsAccessAll,
opensearch:StartDirectQuery,
opensearch:GetDirectQuery,
iam:PassRole,
iam:CreateServiceLinkedRole,
iam:AttachRolePolicy,
iam:AttachUserPolicy,
es:AddDirectQueryDataSource,
es:CreateApplication,
es:UpdateApplication,
es:GetApplication,
es:DeleteApplication,
es:DeleteDirectQueryDataSource,
es:GetDirectQueryDataSource,
es:AddTags,
es:ListApplications
```

### Read
```json
logs:GetIntegration
```

### Delete
```json
logs:DeleteIntegration
```

### List
```json
logs:ListIntegrations
```
