---
title: dataflow_endpoint_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflow_endpoint_groups
  - groundstation
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

Creates, updates, deletes or gets a <code>dataflow_endpoint_group</code> resource or lists <code>dataflow_endpoint_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataflow_endpoint_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Ground Station DataflowEndpointGroup schema for CloudFormation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.groundstation.dataflow_endpoint_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_details" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="contact_pre_pass_duration_seconds" /></td><td><code>integer</code></td><td>Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.</td></tr>
<tr><td><CopyableCode code="contact_post_pass_duration_seconds" /></td><td><code>integer</code></td><td>Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="EndpointDetails, region" /></td>
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
Gets all <code>dataflow_endpoint_groups</code> in a region.
```sql
SELECT
region,
id,
arn,
endpoint_details,
contact_pre_pass_duration_seconds,
contact_post_pass_duration_seconds,
tags
FROM aws.groundstation.dataflow_endpoint_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dataflow_endpoint_group</code>.
```sql
SELECT
region,
id,
arn,
endpoint_details,
contact_pre_pass_duration_seconds,
contact_post_pass_duration_seconds,
tags
FROM aws.groundstation.dataflow_endpoint_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dataflow_endpoint_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.groundstation.dataflow_endpoint_groups (
 EndpointDetails,
 region
)
SELECT 
'{{ EndpointDetails }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.groundstation.dataflow_endpoint_groups (
 EndpointDetails,
 ContactPrePassDurationSeconds,
 ContactPostPassDurationSeconds,
 Tags,
 region
)
SELECT 
 '{{ EndpointDetails }}',
 '{{ ContactPrePassDurationSeconds }}',
 '{{ ContactPostPassDurationSeconds }}',
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
  - name: dataflow_endpoint_group
    props:
      - name: EndpointDetails
        value:
          - SecurityDetails:
              SubnetIds:
                - '{{ SubnetIds[0] }}'
              SecurityGroupIds:
                - '{{ SecurityGroupIds[0] }}'
              RoleArn: '{{ RoleArn }}'
            Endpoint:
              Name: '{{ Name }}'
              Address:
                Name: '{{ Name }}'
                Port: '{{ Port }}'
              Mtu: '{{ Mtu }}'
            AwsGroundStationAgentEndpoint:
              Name: '{{ Name }}'
              EgressAddress:
                SocketAddress: null
                Mtu: '{{ Mtu }}'
              IngressAddress:
                SocketAddress:
                  Name: '{{ Name }}'
                  PortRange:
                    Minimum: '{{ Minimum }}'
                    Maximum: '{{ Maximum }}'
                Mtu: '{{ Mtu }}'
              AgentStatus: '{{ AgentStatus }}'
              AuditResults: '{{ AuditResults }}'
      - name: ContactPrePassDurationSeconds
        value: '{{ ContactPrePassDurationSeconds }}'
      - name: ContactPostPassDurationSeconds
        value: '{{ ContactPostPassDurationSeconds }}'
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
DELETE FROM aws.groundstation.dataflow_endpoint_groups
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dataflow_endpoint_groups</code> resource, the following permissions are required:

### Create
```json
groundstation:CreateDataflowEndpointGroup,
groundstation:GetDataflowEndpointGroup,
groundstation:TagResource,
iam:PassRole,
ec2:describeAddresses,
ec2:describeNetworkInterfaces,
iam:createServiceLinkedRole
```

### Read
```json
groundstation:GetDataflowEndpointGroup,
groundstation:ListTagsForResource
```

### Delete
```json
groundstation:DeleteDataflowEndpointGroup,
groundstation:GetDataflowEndpointGroup
```

### List
```json
groundstation:ListDataflowEndpointGroups
```

