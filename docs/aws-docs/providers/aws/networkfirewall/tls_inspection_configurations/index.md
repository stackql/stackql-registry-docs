---
title: tls_inspection_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - tls_inspection_configurations
  - networkfirewall
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

Creates, updates, deletes or gets a <code>tls_inspection_configuration</code> resource or lists <code>tls_inspection_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tls_inspection_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::TLSInspectionConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.tls_inspection_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tls_inspection_configuration_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tls_inspection_configuration_arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="tls_inspection_configuration" /></td><td><code>object</code></td><td>Resource type definition for AWS::NetworkFirewall::TLSInspectionConfiguration</td></tr>
<tr><td><CopyableCode code="tls_inspection_configuration_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="TLSInspectionConfigurationName, TLSInspectionConfiguration, region" /></td>
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
Gets all <code>tls_inspection_configurations</code> in a region.
```sql
SELECT
region,
tls_inspection_configuration_name,
tls_inspection_configuration_arn,
tls_inspection_configuration,
tls_inspection_configuration_id,
description,
tags
FROM aws.networkfirewall.tls_inspection_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>tls_inspection_configuration</code>.
```sql
SELECT
region,
tls_inspection_configuration_name,
tls_inspection_configuration_arn,
tls_inspection_configuration,
tls_inspection_configuration_id,
description,
tags
FROM aws.networkfirewall.tls_inspection_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<TLSInspectionConfigurationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tls_inspection_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.networkfirewall.tls_inspection_configurations (
 TLSInspectionConfigurationName,
 TLSInspectionConfiguration,
 region
)
SELECT 
'{{ TLSInspectionConfigurationName }}',
 '{{ TLSInspectionConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkfirewall.tls_inspection_configurations (
 TLSInspectionConfigurationName,
 TLSInspectionConfiguration,
 Description,
 Tags,
 region
)
SELECT 
 '{{ TLSInspectionConfigurationName }}',
 '{{ TLSInspectionConfiguration }}',
 '{{ Description }}',
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
  - name: tls_inspection_configuration
    props:
      - name: TLSInspectionConfigurationName
        value: '{{ TLSInspectionConfigurationName }}'
      - name: TLSInspectionConfiguration
        value:
          TLSInspectionConfigurationName: '{{ TLSInspectionConfigurationName }}'
          TLSInspectionConfiguration: null
          Description: '{{ Description }}'
          Tags:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkfirewall.tls_inspection_configurations
WHERE data__Identifier = '<TLSInspectionConfigurationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tls_inspection_configurations</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
network-firewall:CreateTLSInspectionConfiguration,
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:TagResource
```

### Read
```json
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:ListTagsForResources
```

### Update
```json
network-firewall:UpdateTLSInspectionConfiguration,
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:TagResource,
network-firewall:UntagResource
```

### Delete
```json
network-firewall:DeleteTLSInspectionConfiguration,
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:UntagResource
```

### List
```json
network-firewall:ListTLSInspectionConfigurations
```

