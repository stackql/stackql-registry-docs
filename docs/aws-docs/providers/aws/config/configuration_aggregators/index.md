---
title: configuration_aggregators
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_aggregators
  - config
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


Used to retrieve a list of <code>configuration_aggregators</code> in a region or to create or delete a <code>configuration_aggregators</code> resource, use <code>configuration_aggregator</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_aggregators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::ConfigurationAggregator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.configuration_aggregators" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configuration_aggregator_name" /></td><td><code>string</code></td><td>The name of the aggregator.</td></tr>
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
configuration_aggregator_name
FROM aws.config.configuration_aggregators
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>configuration_aggregator</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- configuration_aggregator.iql (required properties only)
INSERT INTO aws.config.configuration_aggregators (
 AccountAggregationSources,
 ConfigurationAggregatorName,
 OrganizationAggregationSource,
 Tags,
 region
)
SELECT 
'{{ AccountAggregationSources }}',
 '{{ ConfigurationAggregatorName }}',
 '{{ OrganizationAggregationSource }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- configuration_aggregator.iql (all properties)
INSERT INTO aws.config.configuration_aggregators (
 AccountAggregationSources,
 ConfigurationAggregatorName,
 OrganizationAggregationSource,
 Tags,
 region
)
SELECT 
 '{{ AccountAggregationSources }}',
 '{{ ConfigurationAggregatorName }}',
 '{{ OrganizationAggregationSource }}',
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
  - name: configuration_aggregator
    props:
      - name: AccountAggregationSources
        value:
          - AllAwsRegions: '{{ AllAwsRegions }}'
            AwsRegions:
              - '{{ AwsRegions[0] }}'
            AccountIds:
              - '{{ AccountIds[0] }}'
      - name: ConfigurationAggregatorName
        value: '{{ ConfigurationAggregatorName }}'
      - name: OrganizationAggregationSource
        value:
          AllAwsRegions: '{{ AllAwsRegions }}'
          AwsRegions:
            - '{{ AwsRegions[0] }}'
          RoleArn: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.config.configuration_aggregators
WHERE data__Identifier = '<ConfigurationAggregatorName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configuration_aggregators</code> resource, the following permissions are required:

### Create
```json
config:PutConfigurationAggregator,
config:DescribeConfigurationAggregators,
config:TagResource,
iam:PassRole,
organizations:EnableAWSServiceAccess,
organizations:ListDelegatedAdministrators
```

### Delete
```json
config:DeleteConfigurationAggregator,
config:UntagResource
```

### List
```json
config:DescribeConfigurationAggregators
```

