---
title: cluster_parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_parameter_groups
  - redshift
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

Creates, updates, deletes or gets a <code>cluster_parameter_group</code> resource or lists <code>cluster_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Redshift::ClusterParameterGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.cluster_parameter_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="parameter_group_name" /></td><td><code>string</code></td><td>The name of the cluster parameter group.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the parameter group.</td></tr>
<tr><td><CopyableCode code="parameter_group_family" /></td><td><code>string</code></td><td>The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>array</code></td><td>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="Description, ParameterGroupFamily, region" /></td>
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
Gets all <code>cluster_parameter_groups</code> in a region.
```sql
SELECT
region,
parameter_group_name,
description,
parameter_group_family,
parameters,
tags
FROM aws.redshift.cluster_parameter_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cluster_parameter_group</code>.
```sql
SELECT
region,
parameter_group_name,
description,
parameter_group_family,
parameters,
tags
FROM aws.redshift.cluster_parameter_groups
WHERE region = 'us-east-1' AND data__Identifier = '<ParameterGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster_parameter_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.redshift.cluster_parameter_groups (
 Description,
 ParameterGroupFamily,
 region
)
SELECT 
'{{ Description }}',
 '{{ ParameterGroupFamily }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.redshift.cluster_parameter_groups (
 ParameterGroupName,
 Description,
 ParameterGroupFamily,
 Parameters,
 Tags,
 region
)
SELECT 
 '{{ ParameterGroupName }}',
 '{{ Description }}',
 '{{ ParameterGroupFamily }}',
 '{{ Parameters }}',
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
  - name: cluster_parameter_group
    props:
      - name: ParameterGroupName
        value: '{{ ParameterGroupName }}'
      - name: Description
        value: '{{ Description }}'
      - name: ParameterGroupFamily
        value: '{{ ParameterGroupFamily }}'
      - name: Parameters
        value:
          - ParameterName: '{{ ParameterName }}'
            ParameterValue: '{{ ParameterValue }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.redshift.cluster_parameter_groups
WHERE data__Identifier = '<ParameterGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cluster_parameter_groups</code> resource, the following permissions are required:

### Create
```json
redshift:CreateClusterParameterGroup,
redshift:ModifyClusterParameterGroup,
redshift:DescribeClusterParameterGroups,
redshift:DescribeClusterParameters,
redshift:DescribeTags,
redshift:CreateTags,
ec2:AllocateAddress,
ec2:AssociateAddress,
ec2:AttachNetworkInterface,
ec2:DescribeAccountAttributes,
ec2:DescribeAddresses,
ec2:DescribeAvailabilityZones,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs
```

### Read
```json
redshift:DescribeClusterParameterGroups,
initech:DescribeReport,
redshift:DescribeClusterParameters,
redshift:DescribeTags
```

### Update
```json
redshift:DescribeClusterParameterGroups,
redshift:ResetClusterParameterGroup,
redshift:ModifyClusterParameterGroup,
redshift:DescribeClusterParameters,
redshift:DescribeTags,
redshift:CreateTags,
redshift:DeleteTags,
initech:UpdateReport
```

### Delete
```json
redshift:DescribeTags,
redshift:DescribeClusterParameterGroups,
redshift:DeleteClusterParameterGroup,
redshift:DescribeClusterParameters,
initech:DeleteReport
```

### List
```json
redshift:DescribeTags,
redshift:DescribeClusterParameterGroups,
redshift:DescribeClusterParameters,
initech:ListReports
```

