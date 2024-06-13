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

Creates, updates, deletes or gets a <code>configuration_set</code> resource or lists <code>configuration_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SES::ConfigurationSet.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.configuration_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the configuration set.</td></tr>
<tr><td><CopyableCode code="tracking_options" /></td><td><code>object</code></td><td>An object that defines the open and click tracking options for emails that you send using the configuration set.</td></tr>
<tr><td><CopyableCode code="delivery_options" /></td><td><code>object</code></td><td>An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.</td></tr>
<tr><td><CopyableCode code="reputation_options" /></td><td><code>object</code></td><td>An object that defines whether or not Amazon SES collects reputation metrics for the emails that you send that use the configuration set.</td></tr>
<tr><td><CopyableCode code="sending_options" /></td><td><code>object</code></td><td>An object that defines whether or not Amazon SES can send email that you send using the configuration set.</td></tr>
<tr><td><CopyableCode code="suppression_options" /></td><td><code>object</code></td><td>An object that contains information about the suppression list preferences for your account.</td></tr>
<tr><td><CopyableCode code="vdm_options" /></td><td><code>object</code></td><td>An object that contains Virtual Deliverability Manager (VDM) settings for this configuration set.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>configuration_sets</code> in a region.
```sql
SELECT
region,
name
FROM aws.ses.configuration_sets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>configuration_set</code>.
```sql
SELECT
region,
name,
tracking_options,
delivery_options,
reputation_options,
sending_options,
suppression_options,
vdm_options
FROM aws.ses.configuration_sets
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
ses:GetConfigurationSet,
ses:DescribeConfigurationSet
```

### Update
```json
ses:PutConfigurationSetTrackingOptions,
ses:PutConfigurationSetDeliveryOptions,
ses:PutConfigurationSetReputationOptions,
ses:PutConfigurationSetSendingOptions,
ses:PutConfigurationSetSuppressionOptions,
ses:PutConfigurationSetVdmOptions
```

### Delete
```json
ses:DeleteConfigurationSet
```

### List
```json
ses:ListConfigurationSets
```

