---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - customerprofiles
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


Used to retrieve a list of <code>integrations</code> in a region or to create or delete a <code>integrations</code> resource, use <code>integration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema for creating an Amazon Connect Customer Profiles Integration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The URI of the S3 bucket or any other type of data source.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
domain_name,
uri
FROM aws.customerprofiles.integrations
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- integration.iql (required properties only)
INSERT INTO aws.customerprofiles.integrations (
 DomainName,
 region
)
SELECT 
'{{ DomainName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- integration.iql (all properties)
INSERT INTO aws.customerprofiles.integrations (
 DomainName,
 Uri,
 FlowDefinition,
 ObjectTypeName,
 Tags,
 ObjectTypeNames,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ Uri }}',
 '{{ FlowDefinition }}',
 '{{ ObjectTypeName }}',
 '{{ Tags }}',
 '{{ ObjectTypeNames }}',
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
      - name: DomainName
        value: '{{ DomainName }}'
      - name: Uri
        value: '{{ Uri }}'
      - name: FlowDefinition
        value:
          FlowName: '{{ FlowName }}'
          Description: '{{ Description }}'
          KmsArn: '{{ KmsArn }}'
          Tasks:
            - ConnectorOperator:
                Marketo: '{{ Marketo }}'
                S3: '{{ S3 }}'
                Salesforce: '{{ Salesforce }}'
                ServiceNow: '{{ ServiceNow }}'
                Zendesk: '{{ Zendesk }}'
              SourceFields:
                - '{{ SourceFields[0] }}'
              DestinationField: '{{ DestinationField }}'
              TaskType: '{{ TaskType }}'
              TaskProperties:
                - OperatorPropertyKey: '{{ OperatorPropertyKey }}'
                  Property: '{{ Property }}'
          TriggerConfig:
            TriggerType: '{{ TriggerType }}'
            TriggerProperties:
              Scheduled:
                ScheduleExpression: '{{ ScheduleExpression }}'
                DataPullMode: '{{ DataPullMode }}'
                ScheduleStartTime: null
                ScheduleEndTime: null
                Timezone: '{{ Timezone }}'
                ScheduleOffset: '{{ ScheduleOffset }}'
                FirstExecutionFrom: null
          SourceFlowConfig:
            ConnectorType: '{{ ConnectorType }}'
            ConnectorProfileName: '{{ ConnectorProfileName }}'
            IncrementalPullConfig:
              DatetimeTypeFieldName: '{{ DatetimeTypeFieldName }}'
            SourceConnectorProperties:
              Marketo:
                Object: '{{ Object }}'
              S3:
                BucketName: '{{ BucketName }}'
                BucketPrefix: '{{ BucketPrefix }}'
              Salesforce:
                Object: null
                EnableDynamicFieldUpdate: '{{ EnableDynamicFieldUpdate }}'
                IncludeDeletedRecords: '{{ IncludeDeletedRecords }}'
              ServiceNow:
                Object: null
              Zendesk:
                Object: null
      - name: ObjectTypeName
        value: '{{ ObjectTypeName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ObjectTypeNames
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.customerprofiles.integrations
WHERE data__Identifier = '<DomainName|Uri>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>integrations</code> resource, the following permissions are required:

### Create
```json
profile:GetIntegration,
profile:PutIntegration,
appflow:CreateFlow,
app-integrations:CreateEventIntegrationAssociation,
app-integrations:GetEventIntegration,
events:ListTargetsByRule,
events:PutRule,
events:PutTargets,
events:PutEvents,
profile:TagResource
```

### Delete
```json
profile:DeleteIntegration,
appflow:DeleteFlow,
app-integrations:ListEventIntegrationAssociations,
app-integrations:DeleteEventIntegrationAssociation,
events:RemoveTargets,
events:ListTargetsByRule,
events:DeleteRule
```

### List
```json
profile:ListIntegrations
```

