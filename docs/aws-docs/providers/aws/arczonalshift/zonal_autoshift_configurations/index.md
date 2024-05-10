---
title: zonal_autoshift_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - zonal_autoshift_configurations
  - arczonalshift
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


Used to retrieve a list of <code>zonal_autoshift_configurations</code> in a region or to create or delete a <code>zonal_autoshift_configurations</code> resource, use <code>zonal_autoshift_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zonal_autoshift_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ARCZonalShift::ZonalAutoshiftConfiguration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.arczonalshift.zonal_autoshift_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td></td></tr>
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
resource_identifier
FROM aws.arczonalshift.zonal_autoshift_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>zonal_autoshift_configuration</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- zonal_autoshift_configuration.iql (required properties only)
INSERT INTO aws.arczonalshift.zonal_autoshift_configurations (
 ZonalAutoshiftStatus,
 PracticeRunConfiguration,
 ResourceIdentifier,
 region
)
SELECT 
'{{ ZonalAutoshiftStatus }}',
 '{{ PracticeRunConfiguration }}',
 '{{ ResourceIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- zonal_autoshift_configuration.iql (all properties)
INSERT INTO aws.arczonalshift.zonal_autoshift_configurations (
 ZonalAutoshiftStatus,
 PracticeRunConfiguration,
 ResourceIdentifier,
 region
)
SELECT 
 '{{ ZonalAutoshiftStatus }}',
 '{{ PracticeRunConfiguration }}',
 '{{ ResourceIdentifier }}',
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
  - name: zonal_autoshift_configuration
    props:
      - name: ZonalAutoshiftStatus
        value: '{{ ZonalAutoshiftStatus }}'
      - name: PracticeRunConfiguration
        value:
          BlockingAlarms:
            - Type: '{{ Type }}'
              AlarmIdentifier: '{{ AlarmIdentifier }}'
          OutcomeAlarms:
            - null
          BlockedDates:
            - '{{ BlockedDates[0] }}'
          BlockedWindows:
            - '{{ BlockedWindows[0] }}'
      - name: ResourceIdentifier
        value: '{{ ResourceIdentifier }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.arczonalshift.zonal_autoshift_configurations
WHERE data__Identifier = '<ResourceIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>zonal_autoshift_configurations</code> resource, the following permissions are required:

### Create
```json
arc-zonal-shift:CreatePracticeRunConfiguration,
arc-zonal-shift:GetManagedResource,
arc-zonal-shift:UpdateZonalAutoshiftConfiguration,
cloudwatch:DescribeAlarms,
iam:CreateServiceLinkedRole
```

### Delete
```json
arc-zonal-shift:DeletePracticeRunConfiguration,
arc-zonal-shift:GetManagedResource,
arc-zonal-shift:UpdateZonalAutoshiftConfiguration
```

### List
```json
arc-zonal-shift:ListManagedResources
```

