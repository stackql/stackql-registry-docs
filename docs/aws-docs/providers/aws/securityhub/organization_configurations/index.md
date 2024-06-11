---
title: organization_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_configurations
  - securityhub
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

Creates, updates, deletes or gets an <code>organization_configuration</code> resource or lists <code>organization_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::OrganizationConfiguration resource represents the configuration of your organization in Security Hub. Only the Security Hub administrator account can create Organization Configuration resource in each region and can opt-in to Central Configuration only in the aggregation region of FindingAggregator.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.organization_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auto_enable" /></td><td><code>boolean</code></td><td>Whether to automatically enable Security Hub in new member accounts when they join the organization.</td></tr>
<tr><td><CopyableCode code="auto_enable_standards" /></td><td><code>string</code></td><td>Whether to automatically enable Security Hub default standards in new member accounts when they join the organization.</td></tr>
<tr><td><CopyableCode code="configuration_type" /></td><td><code>string</code></td><td>Indicates whether the organization uses local or central configuration.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Describes whether central configuration could be enabled as the ConfigurationType for the organization.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>Provides an explanation if the value of Status is equal to FAILED when ConfigurationType is equal to CENTRAL.</td></tr>
<tr><td><CopyableCode code="member_account_limit_reached" /></td><td><code>boolean</code></td><td>Whether the maximum number of allowed member accounts are already associated with the Security Hub administrator account.</td></tr>
<tr><td><CopyableCode code="organization_configuration_identifier" /></td><td><code>string</code></td><td>The identifier of the OrganizationConfiguration being created and assigned as the unique identifier.</td></tr>
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
    <td><CopyableCode code="AutoEnable, region" /></td>
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
List all <code>organization_configurations</code> in a region.
```sql
SELECT
region,
organization_configuration_identifier
FROM aws.securityhub.organization_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an <code>organization_configuration</code>.
```sql
SELECT
region,
auto_enable,
auto_enable_standards,
configuration_type,
status,
status_message,
member_account_limit_reached,
organization_configuration_identifier
FROM aws.securityhub.organization_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<OrganizationConfigurationIdentifier>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>organization_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.organization_configurations (
 AutoEnable,
 region
)
SELECT 
'{{ AutoEnable }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.organization_configurations (
 AutoEnable,
 AutoEnableStandards,
 ConfigurationType,
 region
)
SELECT 
 '{{ AutoEnable }}',
 '{{ AutoEnableStandards }}',
 '{{ ConfigurationType }}',
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
  - name: organization_configuration
    props:
      - name: AutoEnable
        value: '{{ AutoEnable }}'
      - name: AutoEnableStandards
        value: '{{ AutoEnableStandards }}'
      - name: ConfigurationType
        value: '{{ ConfigurationType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.organization_configurations
WHERE data__Identifier = '<OrganizationConfigurationIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>organization_configurations</code> resource, the following permissions are required:

### Create
```json
securityhub:UpdateOrganizationConfiguration,
securityhub:DescribeOrganizationConfiguration,
organizations:DescribeOrganization
```

### Read
```json
securityhub:DescribeOrganizationConfiguration
```

### Update
```json
securityhub:UpdateOrganizationConfiguration,
securityhub:DescribeOrganizationConfiguration,
organizations:DescribeOrganization
```

### Delete
```json
securityhub:UpdateOrganizationConfiguration,
securityhub:DescribeOrganizationConfiguration,
securityhub:ListFindingAggregators,
organizations:DescribeOrganization
```

### List
```json
securityhub:DescribeOrganizationConfiguration
```

