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

Creates, updates, deletes or gets an <code>integration</code> resource or lists <code>integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema for creating an Amazon Connect Customer Profiles Integration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The URI of the S3 bucket or any other type of data source.</td></tr>
<tr><td><CopyableCode code="flow_definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="object_type_name" /></td><td><code>string</code></td><td>The name of the ObjectType defined for the 3rd party data in Profile Service</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the integration</td></tr>
<tr><td><CopyableCode code="object_type_names" /></td><td><code>array</code></td><td>The mapping between 3rd party event types and ObjectType names</td></tr>
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
    <td><CopyableCode code="DomainName, region" /></td>
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
List all <code>integrations</code> in a region.
```sql
SELECT
region,
domain_name,
uri
FROM aws.customerprofiles.integrations
WHERE region = 'us-east-1';
```
Gets all properties from an <code>integration</code>.
```sql
SELECT
region,
domain_name,
uri,
flow_definition,
object_type_name,
created_at,
last_updated_at,
tags,
object_type_names
FROM aws.customerprofiles.integrations
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>|<Uri>';
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
profile:GetIntegration
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

### Update
```json
profile:PutIntegration,
profile:GetIntegration,
appflow:CreateFlow,
app-integrations:GetEventIntegration,
app-integrations:CreateEventIntegrationAssociation,
app-integrations:ListEventIntegrationAssociations,
app-integrations:DeleteEventIntegrationAssociation,
events:ListTargetsByRule,
events:RemoveTargets,
events:DeleteRule,
events:PutRule,
events:PutTargets,
events:PutEvents,
profile:UntagResource,
profile:TagResource
```

### List
```json
profile:ListIntegrations
```

