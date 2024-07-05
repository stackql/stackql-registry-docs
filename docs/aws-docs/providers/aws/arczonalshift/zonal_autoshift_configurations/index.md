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

Creates, updates, deletes or gets a <code>zonal_autoshift_configuration</code> resource or lists <code>zonal_autoshift_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zonal_autoshift_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ARCZonalShift::ZonalAutoshiftConfiguration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.arczonalshift.zonal_autoshift_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="zonal_autoshift_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="practice_run_configuration" /></td><td><code>object</code></td><td></td></tr>
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
Gets all <code>zonal_autoshift_configurations</code> in a region.
```sql
SELECT
region,
zonal_autoshift_status,
practice_run_configuration,
resource_identifier
FROM aws.arczonalshift.zonal_autoshift_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>zonal_autoshift_configuration</code>.
```sql
SELECT
region,
zonal_autoshift_status,
practice_run_configuration,
resource_identifier
FROM aws.arczonalshift.zonal_autoshift_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<ResourceIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>zonal_autoshift_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
arc-zonal-shift:GetManagedResource
```

### Update
```json
arc-zonal-shift:GetManagedResource,
arc-zonal-shift:UpdatePracticeRunConfiguration,
arc-zonal-shift:UpdateZonalAutoshiftConfiguration,
cloudwatch:DescribeAlarms
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

