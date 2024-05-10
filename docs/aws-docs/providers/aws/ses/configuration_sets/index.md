---
title: configuration_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_sets
  - ses
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


Used to retrieve a list of <code>configuration_sets</code> in a region or to create or delete a <code>configuration_sets</code> resource, use <code>configuration_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SES::ConfigurationSet.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.configuration_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the configuration set.</td></tr>
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
name
FROM aws.ses.configuration_sets
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>configuration_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- configuration_set.iql (required properties only)
INSERT INTO aws.ses.configuration_sets (
 Name,
 TrackingOptions,
 DeliveryOptions,
 ReputationOptions,
 SendingOptions,
 SuppressionOptions,
 VdmOptions,
 region
)
SELECT 
'{{ Name }}',
 '{{ TrackingOptions }}',
 '{{ DeliveryOptions }}',
 '{{ ReputationOptions }}',
 '{{ SendingOptions }}',
 '{{ SuppressionOptions }}',
 '{{ VdmOptions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- configuration_set.iql (all properties)
INSERT INTO aws.ses.configuration_sets (
 Name,
 TrackingOptions,
 DeliveryOptions,
 ReputationOptions,
 SendingOptions,
 SuppressionOptions,
 VdmOptions,
 region
)
SELECT 
 '{{ Name }}',
 '{{ TrackingOptions }}',
 '{{ DeliveryOptions }}',
 '{{ ReputationOptions }}',
 '{{ SendingOptions }}',
 '{{ SuppressionOptions }}',
 '{{ VdmOptions }}',
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
  - name: configuration_set
    props:
      - name: Name
        value: '{{ Name }}'
      - name: TrackingOptions
        value:
          CustomRedirectDomain: '{{ CustomRedirectDomain }}'
      - name: DeliveryOptions
        value:
          TlsPolicy: '{{ TlsPolicy }}'
          SendingPoolName: '{{ SendingPoolName }}'
      - name: ReputationOptions
        value:
          ReputationMetricsEnabled: '{{ ReputationMetricsEnabled }}'
      - name: SendingOptions
        value:
          SendingEnabled: '{{ SendingEnabled }}'
      - name: SuppressionOptions
        value:
          SuppressedReasons:
            - '{{ SuppressedReasons[0] }}'
      - name: VdmOptions
        value:
          DashboardOptions:
            EngagementMetrics: '{{ EngagementMetrics }}'
          GuardianOptions:
            OptimizedSharedDelivery: '{{ OptimizedSharedDelivery }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ses.configuration_sets
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configuration_sets</code> resource, the following permissions are required:

### Create
```json
ses:CreateConfigurationSet
```

### Delete
```json
ses:DeleteConfigurationSet
```

### List
```json
ses:ListConfigurationSets
```

